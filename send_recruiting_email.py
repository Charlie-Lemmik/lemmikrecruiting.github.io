#!/usr/bin/env python3

import os
from email.mime.text import MIMEText
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env.gmail')

def authenticate_gmail():
    """Authenticate with Gmail API using existing credentials"""
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("❌ No valid credentials found. Run gmail_manager.py first.")
            return None
    
    return build('gmail', 'v1', credentials=creds)

def send_recruiting_email():
    """Send a recruiting email for Heavy Civil Project Manager position"""
    
    service = authenticate_gmail()
    if not service:
        return
    
    # Email content
    to_email = "charles.lemmik@proton.me"
    subject = "Exciting Heavy Civil Project Manager Opportunity - Lemmik Construction Recruiting"
    
    email_body = """Hello Charles,

I hope this email finds you well. My name is [Your Name] from Lemmik Construction Recruiting, and I came across your profile while researching top talent in the heavy civil construction industry.

I'm reaching out because we have an exceptional opportunity for a Heavy Civil Project Manager that I believe would be a perfect match for your experience and expertise.

**Position Details:**
• Role: Senior Heavy Civil Project Manager
• Industry: Infrastructure & Heavy Civil Construction  
• Location: [Location to be discussed]
• Salary: Competitive package commensurate with experience
• Projects: Multi-million dollar infrastructure projects including bridges, highways, and major earthwork

**What We're Looking For:**
✓ 5+ years of heavy civil project management experience
✓ Experience with large-scale infrastructure projects ($10M+)
✓ Strong background in earthwork, utilities, and roadway construction
✓ Proven track record of delivering projects on time and under budget
✓ Professional Engineer (PE) license preferred
✓ Experience with project management software and scheduling tools

**Why This Opportunity Stands Out:**
• Work on landmark infrastructure projects that shape communities
• Competitive compensation package with performance bonuses  
• Comprehensive benefits including health, dental, vision, and 401(k)
• Clear path for career advancement and leadership development
• Collaborative team environment with industry-leading professionals

**About Lemmik Construction Recruiting:**
We specialize in connecting top-tier construction professionals with premier opportunities in the heavy civil sector. Our deep industry knowledge and extensive network allow us to match exceptional talent with projects that matter.

I'd love to schedule a brief 15-minute conversation to discuss this opportunity in more detail and learn about your career goals. Are you available for a quick call this week?

Even if you're not actively looking, I'm always happy to connect with outstanding professionals in the industry. Building relationships is what we do best.

Looking forward to hearing from you!

Best regards,

[Your Name]  
Senior Recruitment Consultant  
Lemmik Construction Recruiting

📧 Email: [your-email]@lemmikrecruiting.com  
📱 Direct: (555) 123-4567  
🌐 Web: www.lemmikrecruiting.com

P.S. All conversations are confidential. I respect your time and current commitments.

---
This message was sent by Lemmik Construction Recruiting's AI-powered recruitment system."""

    try:
        # Create the email message
        message = MIMEText(email_body)
        message['to'] = to_email
        message['subject'] = subject
        
        # Encode the message
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        # Send the email
        send_message = service.users().messages().send(
            userId="me", 
            body={'raw': raw_message}
        ).execute()
        
        print("✅ Recruiting email sent successfully!")
        print(f"📧 To: {to_email}")
        print(f"📄 Subject: {subject}")
        print(f"🆔 Message ID: {send_message['id']}")
        print("\n📋 Email Preview:")
        print("-" * 50)
        print(f"To: {to_email}")
        print(f"Subject: {subject}")
        print("\nFirst 200 characters:")
        print(email_body[:200] + "...")
        
    except Exception as e:
        print(f"❌ Failed to send recruiting email: {e}")

if __name__ == "__main__":
    send_recruiting_email()