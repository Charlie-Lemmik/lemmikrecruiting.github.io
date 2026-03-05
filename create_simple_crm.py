#!/usr/bin/env python3

import json
import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

def authenticate_sheets():
    """Use existing Gmail token for Sheets access"""
    try:
        # Try to use existing Gmail token but expand scopes
        if os.path.exists('token.json'):
            with open('token.json', 'r') as f:
                token_data = json.load(f)
            
            # Create credentials from existing token
            creds = Credentials(
                token=token_data.get('token'),
                refresh_token=token_data.get('refresh_token'),
                token_uri=token_data.get('token_uri'),
                client_id=token_data.get('client_id'),
                client_secret=token_data.get('client_secret'),
                scopes=['https://www.googleapis.com/auth/spreadsheets', 
                       'https://www.googleapis.com/auth/drive']
            )
            
            # Refresh if needed
            if not creds.valid and creds.refresh_token:
                creds.refresh(Request())
            
            sheets_service = build('sheets', 'v4', credentials=creds)
            drive_service = build('drive', 'v3', credentials=creds)
            
            return sheets_service, drive_service
            
    except Exception as e:
        print(f"❌ Authentication error: {e}")
        return None, None

def create_crm_manually():
    """Create CRM structure manually for now"""
    
    crm_structure = {
        "spreadsheet_name": "Lemmik Recruiting CRM",
        "sheets": {
            "CANDIDATES": {
                "headers": [
                    "ID", "First Name", "Last Name", "Email", "Phone", "LinkedIn", 
                    "Current Company", "Current Title", "Years Experience", "Construction Focus", 
                    "Skills", "Location", "Open to Relocate?", "Current Salary", "Target Salary", 
                    "Availability", "Resume Link", "Source", "Quality Score", "Status", 
                    "Last Contact", "Notes", "Date Added"
                ],
                "sample_data": [
                    ["C001", "John", "Smith", "john.smith@email.com", "(555) 123-4567", 
                     "linkedin.com/in/johnsmith", "ABC Construction", "Project Manager", "8", 
                     "Commercial", "Scheduling, Budgeting, Team Leadership", "Dallas, TX", "Yes", 
                     "$85,000", "$95,000", "Immediate", "resume_link", "LinkedIn", "8.5", 
                     "Active", "2026-03-01", "Strong PM with commercial experience", "2026-03-01"]
                ]
            },
            
            "CLIENTS": {
                "headers": [
                    "Client ID", "Company Name", "Website", "Industry Focus", "Company Size", 
                    "Primary Contact", "Contact Title", "Contact Email", "Contact Phone",
                    "Secondary Contact", "Secondary Email", "Secondary Phone", "Address",
                    "City", "State", "Relationship Status", "Lead Source", "Last Contact",
                    "Next Follow-up", "Contract Signed?", "Fee Agreement", "Notes", "Date Added"
                ],
                "sample_data": [
                    ["CL001", "BuildCorp Inc", "buildcorp.com", "Commercial Construction", "250-500",
                     "Mike Wilson", "VP Operations", "mike.wilson@buildcorp.com", "(555) 345-6789",
                     "Lisa Chen", "lisa.chen@buildcorp.com", "(555) 345-6790", "123 Main St",
                     "Houston", "TX", "Active Client", "Referral", "2026-03-01", "2026-03-15",
                     "Yes", "$5,000 flat fee", "Great relationship, multiple searches", "2026-02-15"]
                ]
            },
            
            "JOB_ORDERS": {
                "headers": [
                    "Job ID", "Client ID", "Company Name", "Position Title", "Department", 
                    "Employment Type", "Location", "Remote OK?", "Salary Min", "Salary Max",
                    "Bonus Structure", "Benefits", "Required Experience", "Required Skills",
                    "Preferred Skills", "Start Date", "Urgency", "Job Description",
                    "Candidates Submitted", "Interviews", "Offers", "Status", "Fee Amount",
                    "Date Created", "Target Fill Date", "Notes"
                ],
                "sample_data": [
                    ["J001", "CL001", "BuildCorp Inc", "Senior Project Manager", "Operations",
                     "Full-time", "Houston, TX", "No", "90000", "110000",
                     "10% annual bonus", "Full health, dental, 401k match", "5+ years commercial PM",
                     "Scheduling, Budgeting, P6", "LEED certification preferred", "2026-04-01",
                     "Standard", "Seeking experienced PM for $50M mixed-use project...",
                     "2", "1", "0", "Open", "5000", "2026-03-01", "2026-03-30", "High priority search"]
                ]
            },
            
            "PIPELINE": {
                "headers": [
                    "Deal ID", "Job ID", "Company", "Position", "Stage", "Candidate Name",
                    "Submitted Date", "Interview Date", "Feedback", "Next Steps", "Close Probability",
                    "Fee Amount", "Expected Close Date", "Status", "Notes", "Last Updated"
                ],
                "sample_data": [
                    ["D001", "J001", "BuildCorp Inc", "Senior Project Manager", "Interview Scheduled", 
                     "John Smith", "2026-03-01", "2026-03-05", "Strong technical skills", 
                     "Follow up post-interview", "75%", "5000", "2026-03-15", "Active", 
                     "Great fit for role", "2026-03-04"]
                ]
            },
            
            "COMMUNICATIONS": {
                "headers": [
                    "Comm ID", "Type", "Contact Type", "Contact ID", "Contact Name", "Company",
                    "Date/Time", "Subject", "Content/Notes", "Follow-up Required?", 
                    "Follow-up Date", "Status", "Created By"
                ],
                "sample_data": [
                    ["CM001", "Email", "Candidate", "C001", "John Smith", "ABC Construction",
                     "2026-03-01 10:30", "PM opportunity at BuildCorp", 
                     "Sent details about senior PM role, waiting for response", "Yes",
                     "2026-03-03", "Sent", "Charles Lemmik"]
                ]
            }
        }
    }
    
    # Save structure to file
    with open('crm_structure.json', 'w') as f:
        json.dump(crm_structure, f, indent=2)
    
    print("✅ CRM structure saved to crm_structure.json")
    return crm_structure

def print_crm_instructions(crm_structure):
    """Print manual setup instructions"""
    
    print("\n🏗️ LEMMIK RECRUITING CRM SETUP INSTRUCTIONS")
    print("=" * 60)
    
    print(f"\n1. Create a new Google Sheet named: '{crm_structure['spreadsheet_name']}'")
    print("2. Create the following tabs/sheets:")
    
    for sheet_name, sheet_data in crm_structure['sheets'].items():
        print(f"\n📊 SHEET: {sheet_name}")
        print(f"   Headers (Row 1): {', '.join(sheet_data['headers'])}")
        print(f"   Sample data provided below...")
    
    print(f"\n3. Format each sheet:")
    print(f"   - Make Row 1 headers BOLD with blue background")
    print(f"   - Freeze Row 1 (View > Freeze > 1 row)")
    print(f"   - Add data validation dropdowns for Status columns")
    
    print(f"\n4. Add these data validation rules:")
    print(f"   CANDIDATES Status column: New, Active, Passive, Interviewing, Placed, Inactive")
    print(f"   PIPELINE Stage column: New Lead, Qualified, Submitted, Interview Scheduled, etc.")
    
    return f"https://docs.google.com/spreadsheets/create"

def main():
    """Main function"""
    print("🚀 Lemmik Recruiting CRM Setup Starting...")
    
    # Try automatic creation first
    sheets_service, drive_service = authenticate_sheets()
    
    if sheets_service and drive_service:
        print("✅ Google Sheets authentication successful!")
        print("🚧 Automated creation coming next...")
    else:
        print("⚠️ Automatic creation not available in this environment")
    
    # Create manual structure regardless
    crm_structure = create_crm_manually()
    
    # Provide instructions
    sheets_url = print_crm_instructions(crm_structure)
    
    print(f"\n🎯 QUICK START:")
    print(f"1. Go to: {sheets_url}")
    print(f"2. Follow the structure in 'crm_structure.json'")
    print(f"3. Copy the sample data to test it out")
    print(f"4. Start adding your real candidates and clients!")
    
    print(f"\n💡 NEXT STEPS AFTER CRM IS READY:")
    print(f"✅ Build web scraping for candidate discovery")
    print(f"✅ Create email outreach templates") 
    print(f"✅ Set up resume parsing system")
    print(f"✅ Build candidate scoring algorithm")
    print(f"✅ Create client submission portal")

if __name__ == "__main__":
    main()