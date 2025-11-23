"""
Slack Notification Service
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

class SlackService:
    def __init__(self):
        self.webhook_url = os.getenv('SLACK_WEBHOOK_URL')
        self.bot_token = os.getenv('SLACK_BOT_TOKEN')

    def send_escape_notification(self, excuse_text):
        if not self.webhook_url:
            print("⚠️  SLACK_WEBHOOK_URL not configured")
            return False

        message = {
            "text": "🚨 *Urgent Alert*",
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "🚨 Urgent: Immediate Attention Required"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Alert:* {excuse_text}"
                    }
                }
            ]
        }

        try:
            response = requests.post(self.webhook_url, json=message)
            return response.status_code == 200
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

    def send_meeting_declined_notification(self, meeting_title, reason):
        if not self.webhook_url:
            return False

        message = {
            "text": f"Meeting declined: {meeting_title}",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"✅ *Meeting Declined*\n*{meeting_title}*\nReason: {reason}"
                    }
                }
            ]
        }

        try:
            response = requests.post(self.webhook_url, json=message)
            return response.status_code == 200
        except:
            return False
