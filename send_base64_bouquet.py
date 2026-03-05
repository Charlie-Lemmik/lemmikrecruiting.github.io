#!/usr/bin/env python3

import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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

def image_to_base64(image_path):
    """Convert image to base64 data URI"""
    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
        encoded_string = base64.b64encode(image_data).decode()
        return f"data:image/jpeg;base64,{encoded_string}"
    except Exception as e:
        print(f"❌ Error encoding image: {e}")
        return None

def send_html_email_with_base64_image(service, to, subject, html_content):
    """Send HTML email with base64 encoded image via Gmail API"""
    try:
        # Get authenticated email to format the From header properly
        sender_email = get_user_email(service)
        sender_header = f"Charles Lemmik <{sender_email}>" if sender_email else "Charles Lemmik"

        # Create message
        message = MIMEMultipart('alternative')
        message['to'] = to
        message['from'] = sender_header
        message['subject'] = subject
        
        # Add HTML content
        html_part = MIMEText(html_content, 'html')
        message.attach(html_part)
        
        # Encode and send
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        send_message = service.users().messages().send(
            userId="me", 
            body={'raw': raw_message}
        ).execute()
        
        print(f"✅ Base64 image email sent successfully! Message ID: {send_message['id']}")
        return send_message
        
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return None

def main():
    # Authenticate Gmail
    service = authenticate_gmail()
    if not service:
        return
    
    # Convert image to base64 (using the properly downloaded image)
    image_path = '/home/charl/.openclaw/workspace/beautiful_bouquet_new.jpg'
    base64_image = image_to_base64(image_path)
    
    if not base64_image:
        print("❌ Failed to convert image to base64")
        return
    
    print("🌸 Image converted to base64 successfully!")
    
    # Compose the beautiful HTML message with traditional styling
    subject = 'A Bouquet of Joy for You'
    
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                font-family: "Aptos", "Calibri", "Segoe UI", "Arial", sans-serif;
                line-height: 1.6;
                color: #2c3e50;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fefefe;
            }}
            .header {{
                text-align: center;
                margin-bottom: 30px;
            }}
            .bouquet-container {{
                text-align: center;
                margin: 30px 0;
                padding: 15px;
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                border-radius: 12px;
            }}
            .bouquet-image {{
                max-width: 100%;
                width: 400px;
                height: auto;
                border-radius: 12px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.15);
                border: 3px solid white;
            }}
            .poem-section {{
                background: linear-gradient(135deg, #fff5f5 0%, #fed7d7 100%);
                padding: 25px;
                border-radius: 10px;
                border-left: 4px solid #e53e3e;
                margin: 25px 0;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            .poem-title {{
                font-size: 20px;
                font-weight: 700;
                color: #c53030;
                margin-bottom: 15px;
                text-align: center;
                text-decoration: underline;
                text-decoration-color: #fed7d7;
            }}
            .poem-text {{
                font-style: italic;
                text-align: center;
                font-size: 17px;
                line-height: 1.9;
                color: #2d3748;
                font-weight: 500;
            }}
            .quote-section {{
                background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
                padding: 25px;
                border-radius: 10px;
                border-left: 4px solid #d69e2e;
                margin: 25px 0;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            .quote-title {{
                font-size: 20px;
                font-weight: 700;
                color: #b7791f;
                margin-bottom: 15px;
                text-align: center;
                text-decoration: underline;
                text-decoration-color: #fef3c7;
            }}
            .quote-text {{
                font-style: italic;
                text-align: center;
                font-size: 17px;
                line-height: 1.8;
                color: #744210;
                font-weight: 500;
            }}
            .quote-author {{
                text-align: right;
                font-weight: 700;
                margin-top: 15px;
                color: #975a16;
                font-size: 16px;
            }}
            .closing {{
                margin-top: 35px;
                padding: 25px;
                text-align: center;
                background: linear-gradient(135deg, #f0fff4 0%, #c6f6d5 100%);
                border-radius: 12px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            .signature {{
                color: #4a5568;
                font-size: 15px;
                margin-top: 15px;
                font-style: italic;
                font-weight: 500;
            }}
            .greeting {{
                font-size: 22px;
                margin-bottom: 25px;
                color: #2d3748;
                font-weight: 600;
            }}
            .sun-text {{
                font-size: 18px; 
                color: #d69e2e;
                font-weight: 600;
                margin-bottom: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="greeting">Dear Charles,</div>
            <p class="sun-text">A little burst of sunshine for your day! 🌞</p>
        </div>

        <div class="bouquet-container">
            <img src="{base64_image}" alt="Beautiful Bouquet of Flowers" class="bouquet-image">
            <p style="margin-top: 10px; font-style: italic; color: #718096; font-size: 14px;">
                Fresh flowers to brighten your day 🌸
            </p>
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
            <p style="font-size: 18px; margin-bottom: 15px; color: #2d3748;">
                May your day be filled with the same beauty and warmth these flowers represent.
            </p>
            
            <p style="font-weight: 600; color: #2d3748; font-size: 17px;">
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
    
    # Send the enhanced email to Gmail
    result = send_html_email_with_base64_image(
        service=service,
        to='charleskimmel86@gmail.com',
        subject=subject,
        html_content=html_content
    )
    
    if result:
        print("🌸 Base64 bouquet email sent successfully!")
    else:
        print("❌ Failed to send base64 bouquet email")

if __name__ == "__main__":
    main()