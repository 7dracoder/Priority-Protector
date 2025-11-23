"""
Slack Notification Service
Handles sending notifications to Slack
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
        """Send fake 'urgent' notification to Slack"""
        if not self.webhook_url:
            print("⚠️  SLACK_WEBHOOK_URL not configured in .env")
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
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": "Priority Protector • Just now"
                        }
                    ]
                }
            ]
        }

        try:
            response = requests.post(self.webhook_url, json=message)
            if response.status_code == 200:
                print("✅ Slack notification sent successfully!")
                return True
            else:
                print(f"❌ Slack notification failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Error sending Slack notification: {e}")
            return False

    def send_meeting_declined_notification(self, meeting_title, reason):
        """Send notification when meeting is auto-declined"""
        if not self.webhook_url:
            print("⚠️  SLACK_WEBHOOK_URL not configured in .env")
            return False

        message = {
            "text": f"Meeting declined: {meeting_title}",
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"✅ *Meeting Declined*\n\n*{meeting_title}*\n\nReason: {reason}"
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
