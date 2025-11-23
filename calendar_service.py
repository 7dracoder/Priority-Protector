"""
Google Calendar Service
Handles authentication and meeting analysis
"""

import os
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly',
    'https://www.googleapis.com/auth/calendar.events'
]

class CalendarService:
    def __init__(self):
        self.creds = None
        self.service = None
        self.authenticate()

    def authenticate(self):
        """Authenticate with Google Calendar API"""
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())

        self.service = build('calendar', 'v3', credentials=self.creds)

    def get_upcoming_meetings(self, days=7):
        """Get all meetings for next N days"""
        try:
            now = datetime.datetime.utcnow().isoformat() + 'Z'
            future = (datetime.datetime.utcnow() + datetime.timedelta(days=days)).isoformat() + 'Z'

            events_result = self.service.events().list(
                calendarId='primary',
                timeMin=now,
                timeMax=future,
                singleEvents=True,
                orderBy='startTime'
            ).execute()

            events = events_result.get('items', [])
            return events

        except HttpError as error:
            print(f'An error occurred: {error}')
            return []

    def analyze_meeting_value(self, event):
        """Score meeting from 0-10 based on value signals"""
        score = 10
        title = event.get('summary', '').lower()
        description = event.get('description', '').lower()
        attendees = event.get('attendees', [])

        low_value_keywords = ['sync', 'catch-up', 'catchup', 'status', 'touch base', 'circle back', 'check-in', 'checkin']
        for keyword in low_value_keywords:
            if keyword in title:
                score -= 2

        if not description or len(description) < 20:
            score -= 2

        if len(attendees) > 8:
            score -= 2

        if 'recurrence' in event:
            score -= 1

        for attendee in attendees:
            if attendee.get('optional', False):
                score -= 1
                break

        start = event.get('start', {}).get('dateTime')
        end = event.get('end', {}).get('dateTime')
        if start and end:
            try:
                start_dt = datetime.datetime.fromisoformat(start.replace('Z', '+00:00'))
                end_dt = datetime.datetime.fromisoformat(end.replace('Z', '+00:00'))
                duration = (end_dt - start_dt).total_seconds() / 3600
                if duration > 1.5:
                    score -= 1
            except:
                pass

        return max(0, min(10, score))

    def get_analyzed_meetings(self):
        """Get meetings with value scores"""
        meetings = self.get_upcoming_meetings()
        analyzed = []

        for meeting in meetings:
            score = self.analyze_meeting_value(meeting)
            start_time = meeting.get('start', {}).get('dateTime', meeting.get('start', {}).get('date', ''))
            end_time = meeting.get('end', {}).get('dateTime', meeting.get('end', {}).get('date', ''))

            analyzed.append({
                'id': meeting.get('id'),
                'title': meeting.get('summary', 'No Title'),
                'start': start_time,
                'end': end_time,
                'attendees': len(meeting.get('attendees', [])),
                'score': score,
                'description': meeting.get('description', 'No description'),
                'organizer': meeting.get('organizer', {}).get('email', 'Unknown')
            })

        return analyzed
