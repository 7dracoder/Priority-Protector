# Setup Instructions

Complete setup guide for Priority Protector.

## Prerequisites

- Python 3.11 or higher
- Git
- Google Cloud account
- IBM watsonx Orchestrate account
- Slack workspace

---

## Step 1: Clone Repository

\`\`\`bash
git clone https://github.com/YOUR_USERNAME/priority-protector.git
cd priority-protector
\`\`\`

---

## Step 2: Python Environment

### Create Virtual Environment

\`\`\`bash
python -m venv venv
\`\`\`

### Activate Virtual Environment

**Windows:**
\`\`\`bash
venv\\Scripts\\activate
\`\`\`

**Mac/Linux:**
\`\`\`bash
source venv/bin/activate
\`\`\`

### Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## Step 3: Google Calendar API Setup

### Create Google Cloud Project

1. Go to https://console.cloud.google.com
2. Click "New Project"
3. Name: `Priority-Protector`
4. Click "Create"

### Enable Calendar API

1. In your project, go to "APIs & Services" → "Library"
2. Search for "Google Calendar API"
3. Click "Enable"

### Create OAuth Credentials

1. Go to "APIs & Services" → "Credentials"
2. Click "Configure Consent Screen"
   - User Type: External
   - App name: Priority Protector
   - Add your email
   - Save
3. Click "Create Credentials" → "OAuth client ID"
   - Application type: Desktop app
   - Name: Priority Protector
   - Click "Create"
4. **Download JSON** → Rename to `credentials.json`
5. Move `credentials.json` to project root

---

## Step 4: Environment Variables

### Copy Template

\`\`\`bash
cp .env.example .env
\`\`\`

### Edit .env

Open `.env` and fill in:

\`\`\`bash
# From Google Cloud Console OAuth credentials
GOOGLE_CLIENT_ID=your_client_id_here
GOOGLE_CLIENT_SECRET=your_client_secret_here

# From IBM watsonx Orchestrate
WO_INSTANCE=your_watsonx_instance_url
WO_API_KEY=your_watsonx_api_key

# From Slack API
SLACK_WEBHOOK_URL=your_slack_webhook_url
SLACK_BOT_TOKEN=your_slack_bot_token
\`\`\`

---

## Step 5: IBM watsonx Orchestrate Setup

### Create Agent

1. Go to IBM watsonx Orchestrate
2. Create new agent: "Priority Protector"
3. Configure instructions (see IBM_WATSONX_AGENT_CONFIG.txt)
4. Add guidelines for professional tone
5. Deploy to Slack channel

### Get API Credentials

1. In your agent settings, find API credentials
2. Copy instance URL and API key
3. Add to `.env` file

---

## Step 6: Slack Integration

### Create Slack App

1. Go to https://api.slack.com/apps
2. Click "Create New App" → "From scratch"
3. Name: Priority Protector
4. Choose your workspace

### Enable Webhooks

1. Click "Incoming Webhooks"
2. Toggle "On"
3. Click "Add New Webhook to Workspace"
4. Choose channel
5. Copy webhook URL → Add to `.env`

### Connect IBM Agent

1. In IBM watsonx, go to Channels
2. Click "Slack"
3. Follow connection wizard
4. Test: `@Priority_Protector hello`

---

## Step 7: Run Application

\`\`\`bash
python app.py
\`\`\`

Open browser: http://localhost:5000

**First time:** Google will ask for calendar authorization

---

## Step 8: Verify Everything Works

- [ ] Dashboard loads
- [ ] Meetings display from Google Calendar
- [ ] Stats show correct numbers
- [ ] "Emergency Escape" generates excuse
- [ ] Slack notification received
- [ ] IBM watsonx agent responds in Slack

---

## Troubleshooting

### Calendar not loading

\`\`\`bash
# Delete token and re-authorize
rm token.json
python app.py
\`\`\`

### Port 5000 in use

Edit `app.py`, change last line:
\`\`\`python
app.run(debug=True, port=5001)
\`\`\`

### Slack not working

Test webhook:
\`\`\`bash
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"Test"}' \
  YOUR_WEBHOOK_URL
\`\`\`

---

## Next Steps

- Add test meetings to Google Calendar
- Practice demo with Slack bot
- Deploy to Vercel (see README.md)

---

For detailed API documentation, see README.md
