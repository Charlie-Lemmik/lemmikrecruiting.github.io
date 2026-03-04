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

def create_recruiting_email(recipient_email):
    """Create personalized recruiting email content"""
    
    # Extract first name from email for personalization
    first_name = recipient_email.split('@')[0].replace('.', ' ').title()
    if first_name.lower() in ['jwilkins', 'j.wilkins']:
        first_name = "J. Wilkins"
    elif first_name.lower() in ['skerschen', 's.kerschen']:
        first_name = "S. Kerschen"
    elif first_name.lower() in ['charles', 'charles.lemmik']:
        first_name = "Charles"
    elif first_name.lower() in ['justinw', 'justin.w']:
        first_name = "Justin"
    
    subject = "Exceptional Heavy Civil Project Manager Opportunity - Lemmik Construction Recruiting"
    
    email_body = f"""Hello {first_name},

I hope this email finds you well. My name is Charlie from Lemmik Construction Recruiting, and I came across your profile while researching top talent in the heavy civil construction industry.

I'm reaching out because we have several exceptional opportunities for Heavy Civil Project Managers that I believe would be perfect matches for experienced professionals like yourself.

**Featured Position: Senior Heavy Civil Project Manager**
• Industry: Infrastructure & Heavy Civil Construction  
• Location: Multiple locations available
• Salary: $85,000 - $140,000+ based on experience
• Projects: Multi-million dollar infrastructure projects including bridges, highways, utilities, and major earthwork

**What Our Clients Are Seeking:**
✓ 5+ years of heavy civil project management experience
✓ Experience with large-scale infrastructure projects ($5M - $50M+)
✓ Strong background in earthwork, utilities, roadway, and bridge construction
✓ Proven track record of delivering projects on time and under budget
✓ Professional Engineer (PE) license strongly preferred
✓ Experience with Primavera P6, Procore, or similar project management software
✓ DOT experience highly valued

**Why These Opportunities Stand Out:**
🏗️ Work on landmark infrastructure projects that shape communities
💰 Competitive compensation packages with performance bonuses  
🏥 Comprehensive benefits: health, dental, vision, 401(k) with matching
📈 Clear paths for career advancement to senior leadership roles
👥 Collaborative environments with industry-leading professionals
🚧 Diverse project portfolio: bridges, highways, site development, utilities

**About Lemmik Construction Recruiting:**
We specialize exclusively in connecting top-tier construction professionals with premier opportunities in the heavy civil and infrastructure sectors. Our deep industry knowledge and extensive network of premier contractors allow us to match exceptional talent with career-defining projects.

**Why Work With Us:**
• **Industry Expertise:** We understand heavy civil construction inside and out
• **Confidential Process:** All conversations are strictly confidential
• **No Cost to You:** Our services are completely free for candidates
• **Long-term Relationships:** We're here for your entire career journey
• **Speed & Efficiency:** We respect your time and move quickly

I'd love to schedule a brief 15-minute conversation to discuss these opportunities in more detail and learn about your career goals and project interests.

**Are you available for a quick call this week?** I have openings:
• Tuesday 2-4 PM
• Wednesday 10-12 PM  
• Thursday 1-3 PM
• Friday morning

Even if you're not actively looking, I'm always happy to connect with outstanding professionals in the industry. The best opportunities often come when you're not expecting them.

**Next Steps:**
Simply reply to this email or give me a call directly. I'd be happy to share more details about specific projects and discuss how we can advance your career in heavy civil construction.

Looking forward to hearing from you!

Best regards,

Charlie Kimmel
Senior Recruitment Consultant  
Lemmik Construction Recruiting

📧 Email: charlie@lemmikrecruiting.com  
📱 Direct: (555) 123-JOBS  
🌐 Web: www.lemmikrecruiting.com
📍 Serving nationwide heavy civil construction markets

P.S. All conversations are completely confidential. I respect your time, current commitments, and professional relationships.

---
This message was sent by Lemmik Construction Recruiting's AI-powered recruitment system.
Specializing in Heavy Civil • Infrastructure • Project Management • Engineering"""

    return subject, email_body

def send_recruiting_email(service, recipient_email):
    """Send recruiting email to a specific recipient"""
    
    subject, email_body = create_recruiting_email(recipient_email)
    
    try:
        # Create the email message
        message = MIMEText(email_body)
        message['to'] = recipient_email
        message['subject'] = subject
        
        # Encode the message
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        # Send the email
        send_message = service.users().messages().send(
            userId="me", 
            body={'raw': raw_message}
        ).execute()
        
        return send_message['id'], subject, email_body
        
    except Exception as e:
        print(f"❌ Failed to send email to {recipient_email}: {e}")
        return None, None, None

def send_multiple_recruiting_emails():
    """Send recruiting emails to multiple recipients"""
    
    # List of recipients
    recipients = [
        "charles.lemmik@proton.me",
        "jwilkins@kimmel.com", 
        "skerschen@kimmel.com",
        "justinw@kimmel.com"
    ]
    
    service = authenticate_gmail()
    if not service:
        return
    
    print("🤖 Lemmik Construction Recruiting - AI Email Campaign")
    print("=" * 60)
    print(f"📧 Sending recruiting emails to {len(recipients)} recipients...")
    print()
    
    successful_sends = 0
    
    for recipient in recipients:
        print(f"📤 Sending to: {recipient}")
        
        message_id, subject, email_body = send_recruiting_email(service, recipient)
        
        if message_id:
            print(f"✅ Successfully sent!")
            print(f"🆔 Message ID: {message_id}")
            print(f"📄 Subject: {subject[:50]}...")
            successful_sends += 1
        else:
            print(f"❌ Failed to send to {recipient}")
        
        print("-" * 40)
    
    print(f"\n📊 CAMPAIGN SUMMARY:")
    print(f"✅ Successfully sent: {successful_sends}/{len(recipients)}")
    print(f"📧 Total emails sent: {successful_sends}")
    
    if successful_sends == len(recipients):
        print("\n🎉 All recruiting emails sent successfully!")
        print("💼 Your AI-powered recruitment campaign is now active!")
    
    return successful_sends

if __name__ == "__main__":
    send_multiple_recruiting_emails()