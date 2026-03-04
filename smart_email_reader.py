#!/usr/bin/env python3

import imaplib
import email
from email.header import decode_header
import os
import json
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv('.env.email')

def setup_gemini():
    """Initialize Gemini AI"""
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ Missing GOOGLE_API_KEY in environment")
        return None
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro-latest')

def clean_subject(subject):
    """Clean and decode email subject"""
    if subject is None:
        return "No Subject"
    
    decoded = decode_header(subject)
    subject_parts = []
    
    for part, encoding in decoded:
        if isinstance(part, bytes):
            try:
                if encoding:
                    subject_parts.append(part.decode(encoding))
                else:
                    subject_parts.append(part.decode('utf-8'))
            except:
                subject_parts.append(part.decode('utf-8', errors='ignore'))
        else:
            subject_parts.append(str(part))
    
    return ''.join(subject_parts)

def get_email_content(msg, max_length=1000):
    """Extract email content for AI analysis"""
    try:
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    if body:
                        text = body.decode('utf-8', errors='ignore')
                        return text[:max_length]
        else:
            body = msg.get_payload(decode=True)
            if body:
                text = body.decode('utf-8', errors='ignore')
                return text[:max_length]
    except:
        pass
    
    return "Content not available"

def analyze_email_with_ai(model, sender, subject, content):
    """Use Gemini to analyze and categorize email"""
    try:
        prompt = f"""
Analyze this email for Lemmik Construction Recruiting and provide a JSON response:

FROM: {sender}
SUBJECT: {subject}
CONTENT: {content[:500]}...

Categorize and analyze this email. Return JSON with:
{{
    "category": "RECRUITING" | "BUSINESS" | "SPAM" | "PERSONAL",
    "priority": "HIGH" | "MEDIUM" | "LOW",
    "action_needed": "IMMEDIATE" | "RESPOND_SOON" | "REVIEW" | "IGNORE",
    "summary": "Brief one-line description",
    "recruiting_relevance": "Description if it's recruiting-related, or null"
}}

Categories:
- RECRUITING: Job applications, candidate inquiries, resume submissions
- BUSINESS: Client inquiries, partnership opportunities, project discussions  
- SPAM: Marketing, promotions, unsubscribes
- PERSONAL: Non-business personal emails

Consider construction industry context and recruiting business priorities.
"""
        
        response = model.generate_content(prompt)
        
        # Try to parse JSON from response
        response_text = response.text.strip()
        
        # Clean up response if it has markdown formatting
        if response_text.startswith('```json'):
            response_text = response_text.split('```json')[1]
        if response_text.endswith('```'):
            response_text = response_text.split('```')[0]
            
        analysis = json.loads(response_text.strip())
        return analysis
        
    except Exception as e:
        print(f"⚠️ AI analysis failed: {str(e)}")
        return {
            "category": "UNKNOWN",
            "priority": "MEDIUM", 
            "action_needed": "REVIEW",
            "summary": "AI analysis failed - manual review needed",
            "recruiting_relevance": None
        }

def get_category_emoji(category):
    """Get emoji for category"""
    emojis = {
        "RECRUITING": "🎯",
        "BUSINESS": "💼", 
        "SPAM": "🗑️",
        "PERSONAL": "👤",
        "UNKNOWN": "❓"
    }
    return emojis.get(category, "📧")

def get_priority_indicator(priority):
    """Get indicator for priority"""
    indicators = {
        "HIGH": "🔥",
        "MEDIUM": "📋", 
        "LOW": "📄"
    }
    return indicators.get(priority, "📧")

def read_and_analyze_emails():
    """Read emails and analyze with Gemini"""
    # Setup AI
    model = setup_gemini()
    if not model:
        print("❌ Cannot initialize Gemini - check GOOGLE_API_KEY")
        return
    
    try:
        # Get credentials
        email_address = os.getenv('EMAIL_ADDRESS')
        password = os.getenv('EMAIL_PASSWORD') 
        imap_server = os.getenv('IMAP_SERVER', 'imap.zoho.com')
        imap_port = int(os.getenv('IMAP_PORT', '993'))
        
        if not email_address or not password:
            print("❌ Missing email credentials in .env.email file")
            return
        
        print(f"🔐 Connecting to {email_address}...")
        print("🤖 AI-powered email analysis with Gemini")
        
        # Connect to Zoho Mail IMAP
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(email_address, password)
        mail.select('inbox')
        
        # Get recent emails
        print("📧 Fetching and analyzing emails...")
        _, messages = mail.search(None, 'ALL')
        
        if not messages[0]:
            print("No emails found")
            return
        
        email_ids = messages[0].split()
        recent_emails = email_ids[-10:]  # Last 10 emails
        recent_emails.reverse()  # Newest first
        
        print(f"\n🧠 AI Analysis Results ({len(recent_emails)} emails):")
        print("=" * 90)
        
        high_priority_count = 0
        recruiting_count = 0
        
        for i, email_id in enumerate(recent_emails, 1):
            try:
                # Fetch email
                _, msg_data = mail.fetch(email_id, '(RFC822)')
                email_body = msg_data[0][1]
                msg = email.message_from_bytes(email_body)
                
                # Extract details
                sender = msg.get('From', 'Unknown')
                subject = clean_subject(msg.get('Subject'))
                content = get_email_content(msg)
                
                # AI Analysis
                print(f"🤖 Analyzing email #{i}...")
                analysis = analyze_email_with_ai(model, sender, subject, content)
                
                # Track stats
                if analysis['priority'] == 'HIGH':
                    high_priority_count += 1
                if analysis['category'] == 'RECRUITING':
                    recruiting_count += 1
                
                # Display results
                category_emoji = get_category_emoji(analysis['category'])
                priority_emoji = get_priority_indicator(analysis['priority'])
                
                print(f"\n📧 Email #{i}")
                print(f"Category: {category_emoji} {analysis['category']}")
                print(f"Priority: {priority_emoji} {analysis['priority']}")
                print(f"Action: {analysis['action_needed']}")
                print(f"From: {sender}")
                print(f"Subject: {subject}")
                print(f"AI Summary: {analysis['summary']}")
                
                if analysis['recruiting_relevance']:
                    print(f"🎯 Recruiting Notes: {analysis['recruiting_relevance']}")
                
                print("-" * 80)
                
            except Exception as e:
                print(f"❌ Error processing email {i}: {str(e)}")
        
        # Summary
        print(f"\n📊 ANALYSIS SUMMARY:")
        print(f"🔥 High Priority: {high_priority_count}")
        print(f"🎯 Recruiting Related: {recruiting_count}")
        print(f"📧 Total Analyzed: {len(recent_emails)}")
        
        mail.close()
        mail.logout()
        print("\n✅ Smart email analysis complete!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("\nMake sure Zoho Mail IMAP is enabled and credentials are correct!")

if __name__ == "__main__":
    read_and_analyze_emails()