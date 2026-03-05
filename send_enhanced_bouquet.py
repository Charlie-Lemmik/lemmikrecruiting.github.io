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

def send_html_email_with_embedded_image(service, to, subject, html_content, image_path):
    """Send HTML email with embedded image via Gmail API"""
    try:
        # Get authenticated email to format the From header properly
        sender_email = get_user_email(service)
        sender_header = f"Charles Lemmik <{sender_email}>" if sender_email else "Charles Lemmik"

        # Create multipart message
        message = MIMEMultipart('related')
        message['to'] = to
        message['from'] = sender_header
        message['subject'] = subject
        
        # Create alternative container for text/html
        msg_alternative = MIMEMultipart('alternative')
        message.attach(msg_alternative)
        
        # Add HTML content
        html_part = MIMEText(html_content, 'html')
        msg_alternative.attach(html_part)
        
        # Embed image
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                image_data = f.read()
            
            image = MIMEImage(image_data, _subtype='jpeg')
            image.add_header('Content-ID', '<bouquet_image>')
            image.add_header('Content-Disposition', 'inline', filename='beautiful_bouquet.jpg')
            message.attach(image)
            print("🌸 Image embedded successfully!")
        else:
            print("⚠️ Image file not found, sending HTML without image")
        
        # Encode and send
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        send_message = service.users().messages().send(
            userId="me", 
            body={'raw': raw_message}
        ).execute()
        
        print(f"✅ Enhanced email sent successfully! Message ID: {send_message['id']}")
        return send_message
        
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return None

def main():
    # Authenticate Gmail
    service = authenticate_gmail()
    if not service:
        return
    
    # Compose the beautiful HTML message with traditional styling
    subject = '🌸 A Bouquet of Joy for You'
    
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {
                font-family: "Aptos", "Calibri", "Segoe UI", "Arial", sans-serif;
                line-height: 1.6;
                color: #2c3e50;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fefefe;
            }
            .header {
                text-align: center;
                margin-bottom: 30px;
            }
            .bouquet-container {
                text-align: center;
                margin: 30px 0;
            }
            .bouquet-image {
                max-width: 100%;
                height: auto;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            }
            .poem-section {
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                padding: 25px;
                border-radius: 10px;
                border-left: 4px solid #e74c3c;
                margin: 25px 0;
            }
            .poem-title {
                font-size: 18px;
                font-weight: 600;
                color: #c0392b;
                margin-bottom: 15px;
                text-align: center;
            }
            .poem-text {
                font-style: italic;
                text-align: center;
                font-size: 16px;
                line-height: 1.8;
                color: #34495e;
            }
            .quote-section {
                background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
                padding: 25px;
                border-radius: 10px;
                border-left: 4px solid #f39c12;
                margin: 25px 0;
            }
            .quote-title {
                font-size: 18px;
                font-weight: 600;
                color: #d68910;
                margin-bottom: 15px;
                text-align: center;
            }
            .quote-text {
                font-style: italic;
                text-align: center;
                font-size: 16px;
                line-height: 1.8;
                color: #7d6608;
            }
            .quote-author {
                text-align: right;
                font-weight: 600;
                margin-top: 10px;
                color: #b7950b;
            }
            .closing {
                margin-top: 35px;
                padding: 20px;
                text-align: center;
                background: #f8f9fa;
                border-radius: 8px;
            }
            .signature {
                color: #7f8c8d;
                font-size: 14px;
                margin-top: 15px;
                font-style: italic;
            }
            .greeting {
                font-size: 18px;
                margin-bottom: 25px;
                color: #2c3e50;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <div class="greeting">Dear Charles,</div>
            <p style="font-size: 16px; color: #e74c3c;">A little burst of sunshine for your day! 🌞</p>
        </div>

        <div class="bouquet-container">
            <img src="cid:bouquet_image" alt="Beautiful Bouquet" class="bouquet-image">
        </div>

        <div class="poem-section">
            <div class="poem-title">A Small Poem:</div>
            <div class="poem-text">
                Petals dance in morning light,<br>
                Colors bold and faces bright,<br>
                Joy blooms where kindness grows,<br>
                Beauty in the smallest shows.
            </div>
        </div>

        <div class="quote-section">
            <div class="quote-title">A Quote to Carry:</div>
            <div class="quote-text">
                "Happiness is not something ready-made. It comes from your own actions."
                <div class="quote-author">— Dalai Lama</div>
            </div>
        </div>

        <div class="closing">
            <p style="font-size: 16px; margin-bottom: 15px;">
                May your day be filled with the same beauty and warmth these flowers represent.
            </p>
            
            <p style="font-weight: 600; color: #2c3e50;">
                With joy,<br>
                Your Digital Assistant 🤖🌸
            </p>
            
            <div class="signature">
                P.S. Sometimes we all need a reminder that beauty exists in simple moments.
            </div>
        </div>
    </body>
    </html>
    '''
    
    # Send the enhanced email
    result = send_html_email_with_embedded_image(
        service=service,
        to='charles.lemmik@proton.me',
        subject=subject,
        html_content=html_content,
        image_path='/home/charl/.openclaw/workspace/beautiful_bouquet.jpg'
    )
    
    if result:
        print("🌸 Enhanced bouquet email sent successfully!")
    else:
        print("❌ Failed to send enhanced bouquet email")

if __name__ == "__main__":
    main()