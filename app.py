"""
Priority Protector - Main Flask Application
The AI Agent That Saves You From Useless Meetings
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from calendar_service import CalendarService
from excuse_generator import ExcuseGenerator
from slack_service import SlackService
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize services
print("🚀 Initializing Priority Protector...")

try:
    calendar_service = CalendarService()
    print("✅ Calendar service initialized")
except Exception as e:
    print(f"⚠️  Calendar service failed: {e}")
    calendar_service = None

excuse_gen = ExcuseGenerator()
print("✅ Excuse generator ready")

slack_service = SlackService()
print("✅ Slack service ready")

print("\n🛡️  Priority Protector is running!\n")


@app.route('/')
def index():
    """Serve main dashboard"""
    return render_template('index.html')


@app.route('/api/meetings')
def get_meetings():
    """Get analyzed meetings from Google Calendar"""
    if not calendar_service:
        return jsonify({
            'success': False,
            'error': 'Calendar service not initialized. Check your credentials.json file.'
        }), 500

    try:
        meetings = calendar_service.get_analyzed_meetings()
        return jsonify({
            'success': True,
            'meetings': meetings,
            'count': len(meetings)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/generate-excuse', methods=['POST'])
def generate_excuse():
    """Generate excuse and send notification to Slack"""
    data = request.json
    user_role = data.get('role', 'generic')
    meeting_title = data.get('meeting_title', 'this meeting')

    # Generate excuse based on user role
    excuse = excuse_gen.generate_excuse(user_role)

    # Send to Slack
    slack_sent = slack_service.send_escape_notification(excuse['excuse'])

    return jsonify({
        'success': True,
        'excuse': excuse,
        'slack_sent': slack_sent
    })


@app.route('/api/decline-meeting', methods=['POST'])
def decline_meeting():
    """Auto-decline a meeting with professional message"""
    data = request.json
    meeting_id = data.get('meeting_id')
    meeting_title = data.get('meeting_title', 'the meeting')
    reason = data.get('reason', 'schedule_conflict')

    # Generate professional decline message
    message = excuse_gen.generate_decline_message(meeting_title, reason)

    # Send notification to Slack
    slack_service.send_meeting_declined_notification(meeting_title, reason)

    return jsonify({
        'success': True,
        'message': message,
        'declined': True,
        'meeting_id': meeting_id
    })


@app.route('/api/stats')
def get_stats():
    """Get time savings statistics"""
    if not calendar_service:
        return jsonify({
            'success': False,
            'error': 'Calendar service not initialized'
        }), 500

    try:
        meetings = calendar_service.get_analyzed_meetings()

        # Calculate statistics
        total_meetings = len(meetings)
        low_value_meetings = [m for m in meetings if m['score'] < 5]
        medium_value_meetings = [m for m in meetings if 5 <= m['score'] < 7]
        high_value_meetings = [m for m in meetings if m['score'] >= 7]

        # Assume 1 hour average per meeting
        total_hours_wasted = len(low_value_meetings) * 1.0

        # Calculate cost at $150/hour average salary
        total_cost = total_hours_wasted * 150

        # Calculate average score
        avg_score = sum(m['score'] for m in meetings) / total_meetings if total_meetings > 0 else 0

        return jsonify({
            'success': True,
            'stats': {
                'total_meetings': total_meetings,
                'low_value_meetings': len(low_value_meetings),
                'medium_value_meetings': len(medium_value_meetings),
                'high_value_meetings': len(high_value_meetings),
                'hours_wasted': round(total_hours_wasted, 1),
                'estimated_cost': int(total_cost),
                'avg_meeting_score': round(avg_score, 1)
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/roles')
def get_roles():
    """Get available user role types for excuse generation"""
    roles = excuse_gen.get_all_roles()
    return jsonify({
        'success': True,
        'roles': roles
    })


@app.route('/api/test-slack')
def test_slack():
    """Test Slack integration"""
    success = slack_service.send_escape_notification(
        "This is a test notification from Priority Protector!"
    )
    return jsonify({
        'success': success,
        'message': 'Check your Slack workspace for the test notification'
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'calendar_connected': calendar_service is not None,
        'slack_configured': slack_service.webhook_url is not None
    })


if __name__ == '__main__':
    print("\n" + "="*50)
    print("🛡️  PRIORITY PROTECTOR")
    print("   Your AI-Powered Meeting Escape Assistant")
    print("="*50)
    print("\n📍 Dashboard: http://localhost:5000")
    print("📍 API endpoints: http://localhost:5000/api/")
    print("\n💡 IBM watsonx Integration:")
    print("   → Agent 'LabLabAI' configured in Slack")
    print("   → Use @Priority_Protector in Slack to interact!")
    print("\n" + "="*50 + "\n")

    app.run(debug=True, port=5000, host='0.0.0.0')
