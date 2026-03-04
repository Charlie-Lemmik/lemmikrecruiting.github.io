#!/usr/bin/env python3

import imaplib
import email
from email.header import decode_header
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env.email')

def clean_subject(subject):
    """Clean and decode email subject"""
    if subject is None:
        return "No Subject"
    
    # Decode subject if it's encoded
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

def get_email_preview(msg, max_length=200):
    """Extract a preview of the email content"""
    try:
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    if body:
                        text = body.decode('utf-8', errors='ignore')
                        return text[:max_length] + "..." if len(text) > max_length else text
        else:
            body = msg.get_payload(decode=True)
            if body:
                text = body.decode('utf-8', errors='ignore')
                return text[:max_length] + "..." if len(text) > max_length else text
    except:
        pass
    
    return "Preview not available"

def categorize_email(sender, subject, preview):
    """Simple email categorization"""
    subject_lower = subject.lower()
    sender_lower = sender.lower()
    preview_lower = preview.lower()
    
    # Recruiting keywords
    recruiting_keywords = ['resume', 'cv', 'application', 'job', 'position', 'hire', 'candidate', 'interview', 'employment', 'career', 'talent', 'recruiting', 'construction', 'estimator', 'project manager']
    
    # Business keywords  
    business_keywords = ['proposal', 'contract', 'meeting', 'project', 'client', 'partnership', 'business']
    
    # Check for recruiting content
    if any(keyword in subject_lower or keyword in preview_lower for keyword in recruiting_keywords):
        return "🎯 RECRUITING"
    
    # Check for business content
    if any(keyword in subject_lower or keyword in preview_lower for keyword in business_keywords):
        return "💼 BUSINESS"
    
    # Check if it's promotional/spam
    if any(word in subject_lower for word in ['unsubscribe', 'offer', 'deal', 'sale', 'discount', 'free']):
        return "📧 PROMOTIONAL"
    
    return "📬 GENERAL"

def read_protonmail_emails():
    """Read emails from ProtonMail using IMAP"""
    try:
        # Get credentials from environment
        email_address = os.getenv('EMAIL_ADDRESS')
        password = os.getenv('EMAIL_PASSWORD')
        imap_server = os.getenv('IMAP_SERVER', 'mail.protonmail.ch')
        imap_port = int(os.getenv('IMAP_PORT', '993'))
        
        if not email_address or not password:
            print("❌ Missing email credentials in .env.email file")
            print("Please set EMAIL_ADDRESS and EMAIL_PASSWORD")
            return
        
        print(f"🔐 Connecting to {email_address}...")
        
        # Connect to ProtonMail IMAP
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)
        mail.login(email_address, password)
        
        # Select inbox
        mail.select('inbox')
        
        # Search for recent emails (last 10)
        print("📧 Fetching recent emails...")
        _, messages = mail.search(None, 'ALL')
        
        if not messages[0]:
            print("No emails found")
            return
        
        email_ids = messages[0].split()
        recent_emails = email_ids[-10:]  # Get last 10 emails
        recent_emails.reverse()  # Show newest first
        
        print(f"\n📬 Found {len(recent_emails)} recent emails:\n")
        print("=" * 80)
        
        for i, email_id in enumerate(recent_emails, 1):
            try:
                # Fetch email
                _, msg_data = mail.fetch(email_id, '(RFC822)')
                email_body = msg_data[0][1]
                msg = email.message_from_bytes(email_body)
                
                # Extract email details
                sender = msg.get('From', 'Unknown Sender')
                subject = clean_subject(msg.get('Subject'))
                date = msg.get('Date', 'Unknown Date')
                
                # Get preview
                preview = get_email_preview(msg)
                
                # Categorize
                category = categorize_email(sender, subject, preview)
                
                # Display
                print(f"📧 Email #{i}")
                print(f"Category: {category}")
                print(f"From: {sender}")
                print(f"Subject: {subject}")
                print(f"Date: {date}")
                print(f"Preview: {preview}")
                print("-" * 80)
                
            except Exception as e:
                print(f"❌ Error processing email {i}: {str(e)}")
        
        # Close connection
        mail.close()
        mail.logout()
        print("\n✅ Email reading complete!")
        
    except Exception as e:
        print(f"❌ Error connecting to ProtonMail: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure IMAP is enabled in ProtonMail settings")
        print("2. Check your credentials in .env.email")
        print("3. You might need ProtonMail Bridge for desktop access")

if __name__ == "__main__":
    read_protonmail_emails()