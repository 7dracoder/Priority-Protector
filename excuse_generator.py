"""
Excuse Generator
"""

import random

class ExcuseGenerator:
    def __init__(self):
        self.templates = {
            'technical': [
                "I'm getting alerts about a production issue that needs immediate attention.",
                "There's an urgent server incident I need to look into right away.",
                "Our monitoring system flagged a critical issue I need to investigate.",
            ],
            'manager': [
                "An urgent matter just came up that requires my immediate attention.",
                "I have a time-sensitive issue I need to address right away.",
                "Something unexpected has come up that I need to handle immediately.",
            ],
            'designer': [
                "A client needs urgent feedback on designs before their deadline.",
                "There's a time-sensitive design review I need to attend.",
                "A stakeholder needs immediate design input.",
            ],
            'data_scientist': [
                "I'm getting alerts about a model performance issue in production.",
                "There's an urgent data pipeline failure I need to investigate.",
                "I'm seeing anomalies in the data that need immediate attention.",
            ],
            'generic': [
                "I apologize, but something urgent has come up.",
                "I need to step away for an urgent matter.",
                "An unexpected priority requires my immediate attention.",
            ]
        }

    def generate_excuse(self, user_role='generic', meeting_context=None):
        role = user_role if user_role in self.templates else 'generic'
        excuse = random.choice(self.templates[role])

        return {
            'excuse': excuse,
            'follow_up': "I'll review the notes and follow up on any action items.",
            'apology': "Sorry for the inconvenience!"
        }

    def generate_decline_message(self, meeting_title, reason='schedule_conflict'):
        messages = {
            'schedule_conflict': f"Thank you for the invitation to '{meeting_title}'. Unfortunately, I have a conflicting priority. Could someone share the notes afterward?",
            'low_priority': f"I appreciate the invitation to '{meeting_title}'. After reviewing my priorities, I don't think my attendance is critical.",
        }
        return messages.get(reason, messages['schedule_conflict'])

    def get_all_roles(self):
        return list(self.templates.keys())
