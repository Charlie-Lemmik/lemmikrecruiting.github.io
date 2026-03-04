# Gmail AI Manager Setup Guide

## 🎯 What This Does
Complete email management with AI:
- **Read** and analyze emails with Gemini
- **Categorize** by type and priority  
- **Draft responses** automatically
- **Send emails** on your behalf
- **Flag urgent** items needing attention

## 📋 Setup Steps

### 1. Install Required Packages
```bash
# Install Gmail API packages
python3 -m pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

# If pip not available, install it first:
sudo apt update && sudo apt install python3-pip
# Then run the pip install command above
```

### 2. Create Free Gmail Account
- **Go to:** https://gmail.com  
- **Create account** for testing (e.g., lemmikrecruiting.test@gmail.com)
- **Verify** the account

### 3. Google Cloud Console Setup
- **Go to:** https://console.cloud.google.com/
- **Create new project** (name it "Lemmik Email Manager")
- **Enable Gmail API:**
  - APIs & Services → Library  
  - Search "Gmail API"
  - Click Enable

### 4. Create OAuth2 Credentials  
- **APIs & Services → Credentials**
- **Create Credentials → OAuth client ID**
- **Application type:** Desktop application
- **Name:** "Gmail Manager"
- **Download** the credentials.json file
- **Move** credentials.json to your workspace folder

### 5. Get Google API Key (for Gemini)
- **Same Google Console project**
- **APIs & Services → Credentials**  
- **Create Credentials → API Key**
- **Copy the key** and add to .env.gmail

### 6. Configure Environment
Edit `.env.gmail`:
```bash
GOOGLE_API_KEY=your_actual_google_api_key_here
```

### 7. Test the System
```bash
python3 gmail_manager.py
```

**First run will:**
- Open browser for Google OAuth
- Ask for Gmail permissions
- Save credentials for future runs

## 🚀 What You'll See

**AI Analysis Output:**
```
🤖 Gmail AI Manager Starting...
📧 Fetching recent emails...
🧠 Analyzing 10 emails with AI...

📧 Email #1
Category: 🎯 RECRUITING  
Priority: ⚡ HIGH
Action: RESPOND_TODAY
From: john.smith@email.com
Subject: Construction Project Manager Position
Summary: Experienced PM seeking new role, strong background
🎯 Recruiting: Qualified candidate, 8+ years experience
💬 Suggested Response: Thank you for your interest...
```

## 🔧 Features

**Email Analysis:**
- **Smart categorization** (Recruiting, Client, Business, Spam)
- **Priority scoring** (Urgent, High, Medium, Low)  
- **Action recommendations** (Respond Today, This Week, etc.)
- **AI-generated summaries**
- **Suggested responses**

**Email Actions:**
- **Read emails** (unread + recent)
- **Send responses** via Gmail API
- **Mark as read/unread**
- **Organize into labels**

## 🎯 Next Steps After Testing

Once working with free Gmail:
1. **Upgrade to Google Workspace** 
2. **Use custom domain** (your-name@lemmikrecruiting.com)
3. **Add automation rules** for common responses
4. **Connect to CRM system**

## ❓ Troubleshooting

**"No module named google":**
- Install packages: `python3 -m pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib`

**"Missing credentials.json":**
- Download OAuth2 credentials from Google Console
- Place in workspace folder

**"Permission denied":**
- Check Gmail API is enabled
- Verify OAuth2 scopes in credentials

Ready to revolutionize your email management! 🚀