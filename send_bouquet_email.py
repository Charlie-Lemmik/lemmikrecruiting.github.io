#!/usr/bin/env python3

import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail API Scopes
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify'
]

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
            print("❌ Need to authenticate first. Run gmail_manager.py first.")
            return None
    
    return build('gmail', 'v1', credentials=creds)

def get_user_email(service):
    """Get authenticated user's email address"""
    try:
        profile = service.users().getProfile(userId='me').execute()
        return profile['emailAddress']
    except Exception:
        return None

def send_email_with_image(service, to, subject, message_text, image_path):
    """Send email with image attachment via Gmail API"""
    try:
        # Get authenticated email to format the From header properly
        sender_email = get_user_email(service)
        sender_header = f"Charles Lemmik <{sender_email}>" if sender_email else "Charles Lemmik"

        # Create multipart message
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender_header
        message['subject'] = subject
        
        # Add text content
        message.attach(MIMEText(message_text, 'plain'))
        
        # Add image attachment
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                image_data = f.read()
            
            image = MIMEImage(image_data, _subtype='jpeg')
            image.add_header('Content-Disposition', f'attachment; filename="beautiful_bouquet.jpg"')
            message.attach(image)
            print("🌸 Image attached successfully!")
        else:
            print("⚠️ Image file not found, sending text only")
        
        # Encode and send
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

def main():
    # Authenticate Gmail
    service = authenticate_gmail()
    if not service:
        return
    
    # Compose the beautiful message
    subject = '🌸 A Bouquet of Joy for You'
    
    message = '''Dear Charles,

A little burst of sunshine for your day! 🌞

**A Small Poem:**

Petals dance in morning light,
Colors bold and faces bright,
Joy blooms where kindness grows,
Beauty in the smallest shows.

**A Quote to Carry:**
"Happiness is not something ready-made. It comes from your own actions." - Dalai Lama

May your day be filled with the same beauty and warmth these flowers represent.

With joy,
Your Digital Assistant 🤖🌸

P.S. Sometimes we all need a reminder that beauty exists in simple moments.'''
    
    # Send the email
    result = send_email_with_image(
        service=service,
        to='charles.lemmik@proton.me',
        subject=subject,
        message_text=message,
        image_path='/home/charl/.openclaw/workspace/beautiful_bouquet.jpg'
    )
    
    if result:
        print("🌸 Beautiful bouquet email sent successfully!")
    else:
        print("❌ Failed to send bouquet email")

if __name__ == "__main__":
    main()