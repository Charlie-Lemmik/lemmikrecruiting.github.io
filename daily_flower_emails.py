#!/usr/bin/env python3

import os
import base64
import random
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime

# Gmail API Scopes
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/gmail.modify'
]

# Beautiful inspirational quotes
QUOTES = [
    {"text": "Happiness is not something ready-made. It comes from your own actions.", "author": "Dalai Lama"},
    {"text": "The best time to plant a tree was 20 years ago. The second best time is now.", "author": "Chinese Proverb"},
    {"text": "Life is like a garden, you reap what you sow.", "author": "Unknown"},
    {"text": "Where flowers bloom, so does hope.", "author": "Lady Bird Johnson"},
    {"text": "Every flower must grow through dirt.", "author": "Laurie Jean Sennott"},
    {"text": "Be like a flower and turn your face to the sun.", "author": "Kahlil Gibran"},
    {"text": "A flower does not think of competing with the flower next to it. It just blooms.", "author": "Zen Shin"},
    {"text": "The earth laughs in flowers.", "author": "Ralph Waldo Emerson"},
    {"text": "In every walk with nature, one receives far more than they seek.", "author": "John Muir"},
    {"text": "Keep your face always toward the sunshine—and shadows will fall behind you.", "author": "Walt Whitman"},
    {"text": "What lies behind us and what lies before us are tiny matters compared to what lies within us.", "author": "Ralph Waldo Emerson"},
    {"text": "The flower that blooms in adversity is the rarest and most beautiful of all.", "author": "Mulan"},
    {"text": "Life is a succession of lessons which must be lived to be understood.", "author": "Helen Keller"},
    {"text": "Every day is a new beginning. Take a breath, smile, and start again.", "author": "Unknown"},
    {"text": "Beauty begins the moment you decide to be yourself.", "author": "Coco Chanel"},
    {"text": "The most wasted of days is one without laughter.", "author": "E.E. Cummings"},
    {"text": "Kindness is a language which the deaf can hear and the blind can see.", "author": "Mark Twain"},
    {"text": "The purpose of life is to live it, to taste experience to the utmost.", "author": "Eleanor Roosevelt"},
    {"text": "Yesterday is history, tomorrow is a mystery, today is a gift.", "author": "Eleanor Roosevelt"},
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"}
]

# Beautiful poems about flowers/nature
POEMS = [
    {
        "title": "Morning Bloom",
        "lines": [
            "Petals dance in morning light,",
            "Colors bold and faces bright,",
            "Joy blooms where kindness grows,",
            "Beauty in the smallest shows."
        ]
    },
    {
        "title": "Garden Dreams",
        "lines": [
            "In gardens where the flowers sway,",
            "Hope whispers through each passing day,",
            "Each bloom a promise, soft and true,",
            "Of beautiful things that wait for you."
        ]
    },
    {
        "title": "Sunshine Song",
        "lines": [
            "Golden rays kiss petals sweet,",
            "Making every day complete,",
            "Nature's gift so pure and free,",
            "Reminds us what life's meant to be."
        ]
    },
    {
        "title": "Spring's Promise",
        "lines": [
            "Through winter's cold and frosty ground,",
            "New life and beauty can be found,",
            "Each flower tells us to believe,",
            "In magic we can achieve."
        ]
    },
    {
        "title": "Simple Joy",
        "lines": [
            "A single flower by the road,",
            "Lightens life's heaviest load,",
            "Small wonders all around us grow,",
            "If we just pause and let them show."
        ]
    },
    {
        "title": "Heart's Garden",
        "lines": [
            "Plant seeds of kindness every day,",
            "Watch love and laughter find their way,",
            "Your heart's a garden, tend it well,",
            "Beautiful stories it will tell."
        ]
    }
]

# Unsplash flower image URLs (different types)
FLOWER_IMAGES = [
    "https://images.unsplash.com/photo-1563241527-3004b7be0ffd?q=80&w=600&auto=format&fit=crop",  # Mixed bouquet
    "https://images.unsplash.com/photo-1490750967868-88aa4486c946?q=80&w=600&auto=format&fit=crop",  # Sunflowers
    "https://images.unsplash.com/photo-1518709268805-4e9042af2176?q=80&w=600&auto=format&fit=crop",  # Pink roses  
    "https://images.unsplash.com/photo-1574684891174-df6d347ef6e4?q=80&w=600&auto=format&fit=crop",  # Tulips
    "https://images.unsplash.com/photo-1571204829887-3b8d69e80649?q=80&w=600&auto=format&fit=crop",  # Daisies
    "https://images.unsplash.com/photo-1584464491033-06628f3a6b7b?q=80&w=600&auto=format&fit=crop",  # Peonies
    "https://images.unsplash.com/photo-1595113316349-9fa4eb24f884?q=80&w=600&auto=format&fit=crop",  # Lavender
    "https://images.unsplash.com/photo-1606041008023-472dfb5e530f?q=80&w=600&auto=format&fit=crop",  # Cherry blossoms
    "https://images.unsplash.com/photo-1582794543139-8ac9cb0f7b11?q=80&w=600&auto=format&fit=crop",  # Wildflowers
    "https://images.unsplash.com/photo-1517517039394-64d4b8c78d85?q=80&w=600&auto=format&fit=crop",  # Orchids
]

def authenticate_gmail():
    """Authenticate with Gmail API using OAuth2"""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
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

def download_flower_image():
    """Download a random flower image"""
    try:
        image_url = random.choice(FLOWER_IMAGES)
        response = requests.get(image_url)
        
        # Use timestamp to make unique filename
        timestamp = int(datetime.now().timestamp())
        filename = f"flower_{timestamp}.jpg"
        
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        print(f"🌸 Downloaded flower image: {filename}")
        return filename
        
    except Exception as e:
        print(f"❌ Error downloading image: {e}")
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

def send_daily_flower_email(service, time_of_day):
    """Send beautiful flower email to Suze"""
    try:
        # Get authenticated email
        sender_email = get_user_email(service)
        sender_header = f"Charles Lemmik <{sender_email}>" if sender_email else "Charles Lemmik"

        # Download random flower image
        image_path = download_flower_image()
        if not image_path:
            return False
        
        # Convert to base64
        base64_image = image_to_base64(image_path)
        if not base64_image:
            return False

        # Select random content
        quote = random.choice(QUOTES)
        poem = random.choice(POEMS)
        
        # Time-specific greetings
        if time_of_day == "morning":
            greeting = "Good morning, Suze!"
            time_message = "A beautiful start to your day! 🌅"
            subject = "Morning Flowers for You"
        else:  # afternoon
            greeting = "Good afternoon, Suze!"
            time_message = "A lovely moment to pause and smile! 🌤️"
            subject = "Afternoon Beauty for You"
        
        # Create HTML email content
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
                .greeting {{
                    font-size: 22px;
                    margin-bottom: 25px;
                    color: #2d3748;
                    font-weight: 600;
                }}
                .time-message {{
                    font-size: 18px;
                    color: #d69e2e;
                    font-weight: 600;
                    margin-bottom: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <div class="greeting">{greeting}</div>
                <p class="time-message">{time_message}</p>
            </div>

            <div class="bouquet-container">
                <img src="{base64_image}" alt="Beautiful Flowers" class="bouquet-image">
                <p style="margin-top: 10px; font-style: italic; color: #718096; font-size: 14px;">
                    Fresh flowers to brighten your day
                </p>
            </div>

            <div class="poem-section">
                <div class="poem-title">{poem['title']}</div>
                <div class="poem-text">
                    {'<br>'.join(poem['lines'])}
                </div>
            </div>

            <div class="quote-section">
                <div class="quote-title">A Quote to Carry:</div>
                <div class="quote-text">
                    "{quote['text']}"
                    <div class="quote-author">— {quote['author']}</div>
                </div>
            </div>

            <div class="closing">
                <p style="font-size: 18px; margin-bottom: 15px; color: #2d3748;">
                    Wishing you a day filled with beauty, joy, and wonderful moments.
                </p>
                
                <p style="font-weight: 600; color: #2d3748; font-size: 17px;">
                    With warmth,<br>
                    Charles
                </p>
            </div>
        </body>
        </html>
        '''
        
        # Create message with BCC
        message = MIMEMultipart('alternative')
        message['to'] = 'kamanning8@gmail.com'
        message['bcc'] = 'charleskimmel86@gmail.com'
        message['from'] = sender_header
        message['subject'] = subject
        
        # Add HTML content
        html_part = MIMEText(html_content, 'html')
        message.attach(html_part)
        
        # Send email
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        send_message = service.users().messages().send(
            userId="me", 
            body={'raw': raw_message}
        ).execute()
        
        print(f"✅ {time_of_day.title()} flower email sent! Message ID: {send_message['id']}")
        
        # Cleanup temp image file
        if os.path.exists(image_path):
            os.remove(image_path)
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to send {time_of_day} email: {e}")
        return False

def main():
    """Main function to send flower email"""
    import sys
    
    # Get time of day from command line argument
    time_of_day = sys.argv[1] if len(sys.argv) > 1 else "morning"
    
    # Authenticate and send
    service = authenticate_gmail()
    if service:
        success = send_daily_flower_email(service, time_of_day)
        if success:
            print(f"🌸 Daily {time_of_day} flower email sent to Suze!")
        else:
            print(f"❌ Failed to send {time_of_day} flower email")
    else:
        print("❌ Gmail authentication failed")

if __name__ == "__main__":
    main()