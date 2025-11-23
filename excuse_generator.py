"""
Excuse Generator
Generates professional exit strategies and decline messages
"""

import random

class ExcuseGenerator:
    """Generates professional exit strategies"""

    def __init__(self):
        self.templates = {
            'technical': [
                "I'm getting alerts about a production issue that needs immediate attention.",
                "There's an urgent server incident I need to look into right away.",
                "Our monitoring system flagged a critical issue I need to investigate.",
                "I'm being paged about a database performance problem.",
                "There's an urgent deployment issue I need to address immediately."
            ],
            'manager': [
                "An urgent matter just came up that requires my immediate attention.",
                "I have a time-sensitive issue I need to address right away.",
                "Something unexpected has come up that I need to handle immediately.",
                "I need to jump on another call that just became urgent.",
                "There's a critical decision that needs my input right now."
            ],
            'designer': [
                "A client needs urgent feedback on designs before their deadline.",
                "There's a time-sensitive design review I need to attend.",
                "I have an urgent creative approval that can't wait.",
                "A stakeholder needs immediate design input.",
                "There's a critical design decision that needs my attention now."
            ],
            'data_scientist': [
                "I'm getting alerts about a model performance issue in production.",
                "There's an urgent data pipeline failure I need to investigate.",
                "A critical analysis deadline just moved up and I need to focus on it.",
                "I'm seeing anomalies in the data that need immediate attention.",
                "There's an urgent stakeholder request for data insights."
            ],
            'generic': [
                "I apologize, but something urgent has come up.",
                "I need to step away for an urgent matter.",
                "An unexpected priority requires my immediate attention.",
                "I have a conflicting urgent commitment I need to address.",
                "Something time-sensitive just came up that I need to handle."
            ]
        }

    def generate_excuse(self, user_role='generic', meeting_context=None):
        """Generate contextually appropriate excuse"""
        role = user_role if user_role in self.templates else 'generic'
        excuse = random.choice(self.templates[role])

        return {
            'excuse': excuse,
            'follow_up': "I'll review the notes and follow up on any action items.",
            'apology': "Sorry for the inconvenience!"
        }

    def generate_decline_message(self, meeting_title, reason='schedule_conflict'):
        """Generate professional meeting decline message"""
        messages = {
            'schedule_conflict': f"Thank you for the invitation to '{meeting_title}'. Unfortunately, I have a conflicting priority during this time. Could someone share the notes afterward?",
            'low_priority': f"I appreciate the invitation to '{meeting_title}'. After reviewing my priorities, I don't think my attendance is critical. Please proceed without me and share any relevant outcomes.",
            'optional': f"Thanks for including me in '{meeting_title}'. Since I'm marked as optional, I'll skip this one to focus on other commitments. Happy to review notes later!",
            'too_many': f"I see '{meeting_title}' has many attendees. To keep the meeting efficient, I'll opt out and catch up via notes. Please loop me in if my input is specifically needed.",
            'no_agenda': f"I'd love to attend '{meeting_title}', but I don't see an agenda. Could we reschedule once we have clear objectives? That way I can prepare and add more value.",
            'recurring_low_value': f"I've been thinking about '{meeting_title}' and I'm not sure I'm adding much value. Would it make sense for me to attend bi-weekly instead? I'll stay informed via notes."
        }

        return messages.get(reason, messages['schedule_conflict'])

    def get_all_roles(self):
        """Return list of available role types"""
        return list(self.templates.keys())
