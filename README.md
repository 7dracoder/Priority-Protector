# 🛡️ Priority Protector

**The AI Agent That Saves You From Useless Meetings**

[![IBM watsonx](https://img.shields.io/badge/IBM-watsonx-blue)](https://www.ibm.com/watsonx)
[![Python](https://img.shields.io/badge/Python-3.11+-green)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Built for IBM watsonx Orchestrate Agentic AI Hackathon - November 2025

---

## 🌐 Live Demo

**🚀 Deployed App:** [Coming Soon]

**💬 Slack Bot:** @Priority_Protector (in our workspace)

**🎥 Video Demo:** [Coming Soon]

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Architecture](#architecture)
- [Quick Start](#quick-start)
- [IBM watsonx Integration](#ibm-watsonx-integration)
- [Demo](#demo)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 About

Priority Protector is an AI-powered meeting assistant that helps employees reclaim their time by:

- 🔍 **Analyzing** meeting value using intelligent scoring
- 🚨 **Generating** professional escape excuses based on context
- 📧 **Creating** polite decline messages
- 📊 **Tracking** time and money saved
- 🤖 **Integrating** with IBM watsonx Orchestrate via Slack

### The Problem

- Average employee: **23 hours/week** in meetings
- **40% add little to no value** = 9.2 hours wasted
- For 100-person company = **$7.2 MILLION lost annually**

### The Solution

Priority Protector uses IBM watsonx Orchestrate to coordinate intelligent agents that help people escape low-value meetings professionally.

---

## ✨ Features

### 🎯 Meeting Analysis
- Scores meetings 0-10 based on value signals
- Considers: title keywords, attendee count, agenda presence, duration
- Color-coded dashboard (red = low value, yellow = medium, green = high)

### 🚨 Emergency Escape
Context-aware professional excuses based on your role:
- **Data Scientist**: "Model performance issue in production"
- **Technical/Engineer**: "Server incident needs attention"
- **Manager**: "Urgent matter requires immediate attention"
- **Designer**: "Client needs urgent feedback"
- **Generic**: Professional universal excuses

### 🤖 IBM watsonx Integration
- Agent deployed to Slack for natural conversation
- Context-aware response generation
- Real agentic AI orchestration

### 📊 Analytics Dashboard
- Total meetings tracked
- Low-value meeting identification
- Hours at risk calculation
- Estimated cost savings ($150/hour)

---

## 🏗️ Architecture

\`\`\`
┌──────────────────────────────────────────┐
│   IBM watsonx Orchestrate Agent          │
│   "Priority Protector" / "LabLabAI"      │
│   (Hosted on IBM Cloud)                  │
└──────────────────────────────────────────┘
              ↓
       ┌──────┴──────┐
       ↓             ↓
┌────────────┐  ┌─────────────────┐
│   Slack    │  │  Web Dashboard  │
│  Channel   │  │   (Flask App)   │
└────────────┘  └─────────────────┘
       ↓             ↓
┌────────────┐  ┌─────────────────┐
│   Webhook  │  │ Google Calendar │
│   Alerts   │  │   Integration   │
└────────────┘  └─────────────────┘
\`\`\`

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Google Cloud account (for Calendar API)
- IBM watsonx Orchestrate account
- Slack workspace (for bot integration)

### Installation

1. **Clone the repository**
\`\`\`bash
git clone https://github.com/YOUR_USERNAME/priority-protector.git
cd priority-protector
\`\`\`

2. **Create virtual environment**
\`\`\`bash
python -m venv venv

# Activate it
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
\`\`\`

3. **Install dependencies**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. **Setup credentials**

Copy \`.env.example\` to \`.env\`:
\`\`\`bash
cp .env.example .env
\`\`\`

Edit \`.env\` with your credentials:
- IBM watsonx API key and instance URL
- Google Calendar OAuth credentials
- Slack bot token and webhook URL

Download \`credentials.json\` from Google Cloud Console and place in project root.

5. **Run the application**
\`\`\`bash
python app.py
\`\`\`

6. **Open in browser**
\`\`\`
http://localhost:5000
\`\`\`

First time: Google will ask for calendar authorization.

---

## 🤖 IBM watsonx Integration

### Agent Configuration

The Priority Protector agent is configured in IBM watsonx Orchestrate with:

**Profile:**
- AI meeting assistant that helps escape low-value meetings
- Generates context-aware professional excuses
- Provides role-specific responses

**Capabilities:**
- Meeting value analysis
- Excuse generation (5 role types)
- Decline message creation
- Time savings calculation

**Channel:**
- Integrated with Slack
- Natural language conversation
- Real-time responses

### Using the Slack Bot

In your Slack workspace:

\`\`\`
@Priority_Protector I need to escape my 2pm status meeting. I'm a data scientist.
\`\`\`

The agent will respond with a contextually appropriate professional excuse.

---

## 🎬 Demo

### 3-Minute Demo Script

**Minute 1: The Problem**
> "23 hours/week in meetings, 40% are useless = $7.2M lost for 100-person company"

**Minute 2: Live Demo**
1. Show dashboard with meeting scores
2. Click "Emergency Escape" → show generated excuse
3. Switch to Slack → interact with IBM watsonx agent
4. Show Slack notification

**Minute 3: Business Impact**
> "Saves 9.2 hours/person/week. For 100-person company: $1.56M saved annually."

---

## 📚 API Documentation

### Endpoints

#### \`GET /\`
Serves the main dashboard interface

#### \`GET /api/meetings\`
Returns analyzed meetings from Google Calendar
\`\`\`json
{
  "success": true,
  "meetings": [
    {
      "id": "event_id",
      "title": "Weekly Sync",
      "start": "2025-11-22T14:00:00",
      "score": 4,
      "attendees": 12
    }
  ],
  "count": 1
}
\`\`\`

#### \`POST /api/generate-excuse\`
Generates context-aware excuse
\`\`\`json
{
  "role": "data_scientist",
  "meeting_title": "Status Meeting"
}
\`\`\`

#### \`POST /api/decline-meeting\`
Creates professional decline message
\`\`\`json
{
  "meeting_id": "event_id",
  "meeting_title": "Sync Call",
  "reason": "low_priority"
}
\`\`\`

#### \`GET /api/stats\`
Returns time savings statistics

#### \`GET /api/test-slack\`
Tests Slack integration

#### \`GET /health\`
Health check endpoint

---

## 🌍 Deployment

### Deploy to Vercel

1. **Push to GitHub**
\`\`\`bash
git add .
git commit -m "Initial commit"
git push origin main
\`\`\`

2. **Import to Vercel**
- Go to [vercel.com](https://vercel.com)
- Import your GitHub repository
- Add environment variables from \`.env\`

3. **Configure OAuth**
Update Google Cloud Console with Vercel redirect URI:
\`\`\`
https://your-app.vercel.app/oauth2callback
\`\`\`

### Environment Variables

Set these in Vercel (or your deployment platform):
- \`WO_INSTANCE\`
- \`WO_API_KEY\`
- \`GOOGLE_CLIENT_ID\`
- \`GOOGLE_CLIENT_SECRET\`
- \`SLACK_BOT_TOKEN\`
- \`SLACK_WEBHOOK_URL\`
- \`FLASK_ENV=production\`

---

## 📁 Project Structure

\`\`\`
priority-protector/
├── app.py                    # Main Flask application
├── calendar_service.py       # Google Calendar integration
├── excuse_generator.py       # Excuse generation logic
├── slack_service.py          # Slack integration
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel deployment config
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── templates/
│   └── index.html           # Dashboard UI
├── README.md                # This file
└── LICENSE                  # MIT License
\`\`\`

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (\`git checkout -b feature/AmazingFeature\`)
3. Commit your changes (\`git commit -m 'Add some AmazingFeature'\`)
4. Push to the branch (\`git push origin feature/AmazingFeature\`)
5. Open a Pull Request

---

## 🏆 Hackathon

Built for **IBM watsonx Orchestrate Agentic AI Hackathon** - November 2025

**Technologies:**
- IBM Watsonx Orchestrate (agent orchestration)
- Google Calendar API (meeting data)
- Slack API (notifications & bot)
- Flask (web framework)
- Python 3.11+

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- IBM Watsonx Orchestrate team for the amazing platform
- LabLab.ai for organizing the hackathon
- All contributors and testers

---

## 📧 Contact

**Project Link:** [https://github.com/YOUR_USERNAME/priority-protector](https://github.com/7dracoder/priority-protector)

**Demo Video:** [Coming Soon]

---

**⭐ If you found this project helpful, please give it a star!**
