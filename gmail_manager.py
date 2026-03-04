#!/usr/bin/env python3

import os
import json
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import google.generativeai as genai
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv('.env.gmail')

# Gmail API Scopes
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify'
]

def setup_gemini():
    """Initialize Gemini AI"""
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing GOOGLE_API_KEY in .env.gmail")
        return None
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro-latest')

def authenticate_gmail():
    """Authenticate with Gmail API using OAuth2"""
    creds = None
    
    # Load existing credentials
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If no valid credentials, start OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("❌ Missing credentials.json file!")
                print("📋 Setup Instructions:")
                print("1. Go to Google Cloud Console")
                print("2. Create project and enable Gmail API") 
                print("3. Create OAuth2 credentials")
                print("4. Download as 'credentials.json'")
                return None
            
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials for next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return build('gmail', 'v1', credentials=creds)

def decode_email_content(data):
    """Decode base64 email content"""
    try:
        if 'data' in data:
            return base64.urlsafe_b64decode(data['data']).decode('utf-8')
    except Exception:
        pass
    return ""

def get_email_body(payload):
    """Extract email body from Gmail message payload"""
    body = ""
    
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                body += decode_email_content(part['body'])
            elif part['mimeType'] == 'multipart/alternative' and 'parts' in part:
                for subpart in part['parts']:
                    if subpart['mimeType'] == 'text/plain':
                        body += decode_email_content(subpart['body'])
    else:
        if payload['mimeType'] == 'text/plain':
            body = decode_email_content(payload['body'])
    
    return body

def analyze_email_with_ai(model, sender, subject, body):
    """Analyze email with Gemini and suggest actions"""
    try:
        prompt = f"""
Analyze this email for Lemmik Construction Recruiting business:

FROM: {sender}
SUBJECT: {subject}
CONTENT: {body[:800]}...

Provide JSON analysis:
{{
    "category": "RECRUITING" | "CLIENT" | "BUSINESS" | "SPAM" | "PERSONAL",
    "priority": "URGENT" | "HIGH" | "MEDIUM" | "LOW",
    "action_needed": "IMMEDIATE_RESPONSE" | "RESPOND_TODAY" | "RESPOND_WEEK" | "ACKNOWLEDGE" | "IGNORE",
    "sentiment": "POSITIVE" | "NEUTRAL" | "NEGATIVE" | "INQUIRY",
    "summary": "One-line description",
    "key_points": ["key point 1", "key point 2"],
    "suggested_response": "Brief suggested response or null if no response needed",
    "recruiting_notes": "Recruiting-specific insights or null"
}}

Categories:
- RECRUITING: Job applications, candidate inquiries, resumes
- CLIENT: Existing client communications, project discussions
- BUSINESS: New business inquiries, partnerships, vendors
- SPAM: Marketing, promotions, automated messages
- PERSONAL: Non-business emails

Focus on construction industry context and recruiting business priorities.
"""
        
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        
        # Clean JSON response
        if response_text.startswith('```json'):
            response_text = response_text.split('```json')[1].split('```')[0]
        
        return json.loads(response_text.strip())
        
    except Exception as e:
        print(f"⚠️ AI analysis failed: {e}")
        return {
            "category": "UNKNOWN",
            "priority": "MEDIUM",
            "action_needed": "MANUAL_REVIEW",
            "sentiment": "NEUTRAL", 
            "summary": "Analysis failed - manual review needed",
            "key_points": [],
            "suggested_response": None,
            "recruiting_notes": None
        }

def get_user_email(service):
    """Get authenticated user's email address"""
    try:
        profile = service.users().getProfile(userId='me').execute()
        return profile['emailAddress']
    except Exception:
        return None

def send_email(service, to, subject, message_text):
    """Send email via Gmail API"""
    try:
        # Get authenticated email to format the From header properly
        sender_email = get_user_email(service)
        sender_header = f"Charles Lemmik <{sender_email}>" if sender_email else "Charles Lemmik"

        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender_header
        message['subject'] = subject
        
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        send_message = service.users().messages().send(
            userId="me", 
            body={'raw': raw_message}
        ).execute()
        
        print(f"✅ Email sent successfully! Message ID: {send_message['id']}")
        return send_message
        
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return None

def manage_gmail_with_ai():
    """Full Gmail management with AI analysis"""
    # Setup
    model = setup_gemini()
    if not model:
        return
    
    service = authenticate_gmail()
    if not service:
        return
    
    try:
        print("🤖 Gmail AI Manager Starting...")
        print("📧 Fetching recent emails...")
        
        # Get recent messages
        results = service.users().messages().list(
            userId='me', 
            maxResults=10,
            q='is:unread OR newer_than:3d'  # Unread or from last 3 days
        ).execute()
        
        messages = results.get('messages', [])
        
        if not messages:
            print("No recent emails found")
            return
        
        print(f"🧠 Analyzing {len(messages)} emails with AI...")
        print("=" * 90)
        
        urgent_count = 0
        recruiting_count = 0
        action_needed = []
        
        for i, message in enumerate(messages, 1):
            try:
                # Get full message
                msg = service.users().messages().get(
                    userId='me', 
                    id=message['id']
                ).execute()
                
                # Extract email details
                payload = msg['payload']
                headers = payload.get('headers', [])
                
                sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
                subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
                
                body = get_email_body(payload)
                
                # AI Analysis
                print(f"🤖 Analyzing email #{i}...")
                analysis = analyze_email_with_ai(model, sender, subject, body)
                
                # Track stats
                if analysis['priority'] in ['URGENT', 'HIGH']:
                    urgent_count += 1
                if analysis['category'] == 'RECRUITING':
                    recruiting_count += 1
                if analysis['action_needed'] in ['IMMEDIATE_RESPONSE', 'RESPOND_TODAY']:
                    action_needed.append({
                        'email_id': message['id'],
                        'sender': sender,
                        'subject': subject,
                        'action': analysis['action_needed'],
                        'suggested_response': analysis['suggested_response']
                    })
                
                # Display results
                priority_emoji = {"URGENT": "🔥", "HIGH": "⚡", "MEDIUM": "📋", "LOW": "📄"}.get(analysis['priority'], "📧")
                category_emoji = {"RECRUITING": "🎯", "CLIENT": "👔", "BUSINESS": "💼", "SPAM": "🗑️", "PERSONAL": "👤"}.get(analysis['category'], "❓")
                
                print(f"\n📧 Email #{i}")
                print(f"Category: {category_emoji} {analysis['category']}")
                print(f"Priority: {priority_emoji} {analysis['priority']}")
                print(f"Action: {analysis['action_needed']}")
                print(f"Sentiment: {analysis['sentiment']}")
                print(f"From: {sender}")
                print(f"Subject: {subject}")
                print(f"Summary: {analysis['summary']}")
                
                if analysis['key_points']:
                    print(f"Key Points: {', '.join(analysis['key_points'])}")
                
                if analysis['recruiting_notes']:
                    print(f"🎯 Recruiting: {analysis['recruiting_notes']}")
                
                if analysis['suggested_response']:
                    print(f"💬 Suggested Response: {analysis['suggested_response']}")
                
                print("-" * 80)
                
            except Exception as e:
                print(f"❌ Error processing email {i}: {e}")
        
        # Action Summary
        print(f"\n📊 ANALYSIS SUMMARY:")
        print(f"🔥 Urgent/High Priority: {urgent_count}")
        print(f"🎯 Recruiting Related: {recruiting_count}")
        print(f"⚡ Need Action Today: {len([a for a in action_needed if a['action'] in ['IMMEDIATE_RESPONSE', 'RESPOND_TODAY']])}")
        print(f"📧 Total Analyzed: {len(messages)}")
        
        if action_needed:
            print(f"\n⚡ EMAILS NEEDING IMMEDIATE ATTENTION:")
            for email in action_needed:
                print(f"• {email['subject']} - {email['sender']}")
        
        print("\n✅ Gmail AI analysis complete!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    manage_gmail_with_ai()