#!/usr/bin/env python3

import os
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime

# Google Sheets API Scopes
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

def authenticate_sheets():
    """Authenticate with Google Sheets API"""
    creds = None
    
    # Load existing credentials
    if os.path.exists('sheets_token.json'):
        creds = Credentials.from_authorized_user_file('sheets_token.json', SCOPES)
    
    # If no valid credentials, start OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                print("❌ Missing credentials.json file!")
                print("📋 Setup Instructions:")
                print("1. Go to Google Cloud Console")
                print("2. Enable Google Sheets API and Google Drive API")
                print("3. Create OAuth2 credentials")
                print("4. Download as 'credentials.json'")
                return None, None
            
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save credentials for next run
        with open('sheets_token.json', 'w') as token:
            token.write(creds.to_json())
    
    sheets_service = build('sheets', 'v4', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    
    return sheets_service, drive_service

def create_recruiting_crm(sheets_service, drive_service):
    """Create the complete Lemmik Recruiting CRM in Google Sheets"""
    
    print("🏗️ Building Lemmik Recruiting CRM...")
    
    # Create new spreadsheet
    spreadsheet = {
        'properties': {
            'title': 'Lemmik Recruiting CRM',
            'timeZone': 'America/New_York'
        },
        'sheets': [
            {'properties': {'title': 'CANDIDATES', 'index': 0}},
            {'properties': {'title': 'CLIENTS', 'index': 1}},
            {'properties': {'title': 'JOB_ORDERS', 'index': 2}},
            {'properties': {'title': 'PIPELINE', 'index': 3}},
            {'properties': {'title': 'COMMUNICATIONS', 'index': 4}},
            {'properties': {'title': 'DASHBOARD', 'index': 5}}
        ]
    }
    
    result = sheets_service.spreadsheets().create(body=spreadsheet).execute()
    spreadsheet_id = result['spreadsheetId']
    spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}"
    
    print(f"✅ Created spreadsheet: {spreadsheet_url}")
    
    # CANDIDATES Sheet Structure
    candidates_headers = [
        ['ID', 'First Name', 'Last Name', 'Email', 'Phone', 'LinkedIn', 'Current Company', 
         'Current Title', 'Years Experience', 'Construction Focus', 'Skills', 'Location', 
         'Open to Relocate?', 'Current Salary', 'Target Salary', 'Availability', 'Resume Link',
         'Source', 'Quality Score', 'Status', 'Last Contact', 'Notes', 'Date Added']
    ]
    
    # CLIENTS Sheet Structure  
    clients_headers = [
        ['Client ID', 'Company Name', 'Website', 'Industry Focus', 'Company Size', 
         'Primary Contact', 'Contact Title', 'Contact Email', 'Contact Phone',
         'Secondary Contact', 'Secondary Email', 'Secondary Phone', 'Address',
         'City', 'State', 'Relationship Status', 'Lead Source', 'Last Contact',
         'Next Follow-up', 'Contract Signed?', 'Fee Agreement', 'Notes', 'Date Added']
    ]
    
    # JOB ORDERS Sheet Structure
    job_orders_headers = [
        ['Job ID', 'Client ID', 'Company Name', 'Position Title', 'Department', 
         'Employment Type', 'Location', 'Remote OK?', 'Salary Min', 'Salary Max',
         'Bonus Structure', 'Benefits', 'Required Experience', 'Required Skills',
         'Preferred Skills', 'Start Date', 'Urgency', 'Job Description',
         'Candidates Submitted', 'Interviews', 'Offers', 'Status', 'Fee Amount',
         'Date Created', 'Target Fill Date', 'Notes']
    ]
    
    # PIPELINE Sheet Structure
    pipeline_headers = [
        ['Deal ID', 'Job ID', 'Company', 'Position', 'Stage', 'Candidate Name',
         'Submitted Date', 'Interview Date', 'Feedback', 'Next Steps', 'Close Probability',
         'Fee Amount', 'Expected Close Date', 'Status', 'Notes', 'Last Updated']
    ]
    
    # COMMUNICATIONS Sheet Structure
    communications_headers = [
        ['Comm ID', 'Type', 'Contact Type', 'Contact ID', 'Contact Name', 'Company',
         'Date/Time', 'Subject', 'Content/Notes', 'Follow-up Required?', 
         'Follow-up Date', 'Status', 'Created By']
    ]
    
    # DASHBOARD Sheet Structure
    dashboard_headers = [
        ['METRIC', 'VALUE', 'TARGET', 'VARIANCE', 'LAST_UPDATED'],
        ['Total Candidates', '=COUNTA(CANDIDATES!A:A)-1', '1000', '', '=NOW()'],
        ['Active Candidates', '=COUNTIF(CANDIDATES!T:T,"Active")', '500', '', ''],
        ['Total Clients', '=COUNTA(CLIENTS!A:A)-1', '50', '', ''],
        ['Active Job Orders', '=COUNTIF(JOB_ORDERS!V:V,"Open")', '10', '', ''],
        ['Pipeline Value', '=SUMIF(PIPELINE!E:E,"Open",PIPELINE!L:L)', '$50,000', '', ''],
        ['This Month Placements', '=COUNTIFS(PIPELINE!N:N,"Placed",PIPELINE!P:P,">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1))', '5', '', ''],
        ['Revenue This Month', '=SUMIFS(PIPELINE!L:L,PIPELINE!N:N,"Placed",PIPELINE!P:P,">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1))', '$25,000', '', '']
    ]
    
    # Prepare batch update
    requests = []
    
    # Add headers for each sheet
    sheet_data = [
        ('CANDIDATES', candidates_headers),
        ('CLIENTS', clients_headers), 
        ('JOB_ORDERS', job_orders_headers),
        ('PIPELINE', pipeline_headers),
        ('COMMUNICATIONS', communications_headers),
        ('DASHBOARD', dashboard_headers)
    ]
    
    for sheet_name, headers in sheet_data:
        requests.append({
            'updateCells': {
                'range': {
                    'sheetId': get_sheet_id(result, sheet_name),
                    'startRowIndex': 0,
                    'endRowIndex': len(headers),
                    'startColumnIndex': 0,
                    'endColumnIndex': len(headers[0]) if headers else 0
                },
                'rows': [{
                    'values': [{'userEnteredValue': {'stringValue': cell}} for cell in row]
                } for row in headers],
                'fields': 'userEnteredValue'
            }
        })
        
        # Format headers (bold, background color)
        requests.append({
            'repeatCell': {
                'range': {
                    'sheetId': get_sheet_id(result, sheet_name),
                    'startRowIndex': 0,
                    'endRowIndex': 1,
                    'startColumnIndex': 0,
                    'endColumnIndex': len(headers[0]) if headers else 0
                },
                'cell': {
                    'userEnteredFormat': {
                        'backgroundColor': {'red': 0.2, 'green': 0.6, 'blue': 0.9},
                        'textFormat': {'bold': True, 'foregroundColor': {'red': 1.0, 'green': 1.0, 'blue': 1.0}}
                    }
                },
                'fields': 'userEnteredFormat(backgroundColor,textFormat)'
            }
        })
        
        # Freeze header row
        requests.append({
            'updateSheetProperties': {
                'properties': {
                    'sheetId': get_sheet_id(result, sheet_name),
                    'gridProperties': {
                        'frozenRowCount': 1
                    }
                },
                'fields': 'gridProperties.frozenRowCount'
            }
        })
    
    # Add data validation for specific columns
    # Status dropdown for CANDIDATES
    requests.append({
        'setDataValidation': {
            'range': {
                'sheetId': get_sheet_id(result, 'CANDIDATES'),
                'startRowIndex': 1,
                'endRowIndex': 1000,
                'startColumnIndex': 19,  # Status column
                'endColumnIndex': 20
            },
            'rule': {
                'condition': {
                    'type': 'ONE_OF_LIST',
                    'values': [
                        {'userEnteredValue': 'New'},
                        {'userEnteredValue': 'Active'},
                        {'userEnteredValue': 'Passive'},
                        {'userEnteredValue': 'Interviewing'},
                        {'userEnteredValue': 'Placed'},
                        {'userEnteredValue': 'Inactive'}
                    ]
                },
                'showCustomUi': True
            }
        }
    })
    
    # Stage dropdown for PIPELINE
    requests.append({
        'setDataValidation': {
            'range': {
                'sheetId': get_sheet_id(result, 'PIPELINE'),
                'startRowIndex': 1,
                'endRowIndex': 1000,
                'startColumnIndex': 4,  # Stage column
                'endColumnIndex': 5
            },
            'rule': {
                'condition': {
                    'type': 'ONE_OF_LIST',
                    'values': [
                        {'userEnteredValue': 'New Lead'},
                        {'userEnteredValue': 'Qualified'},
                        {'userEnteredValue': 'Submitted'},
                        {'userEnteredValue': 'Interview Scheduled'},
                        {'userEnteredValue': 'Interview Complete'},
                        {'userEnteredValue': 'Reference Check'},
                        {'userEnteredValue': 'Offer Made'},
                        {'userEnteredValue': 'Offer Accepted'},
                        {'userEnteredValue': 'Placed'},
                        {'userEnteredValue': 'Lost'}
                    ]
                },
                'showCustomUi': True
            }
        }
    })
    
    # Execute all requests
    if requests:
        sheets_service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={'requests': requests}
        ).execute()
    
    # Make spreadsheet shareable
    drive_service.permissions().create(
        fileId=spreadsheet_id,
        body={
            'role': 'writer',
            'type': 'anyone'
        }
    ).execute()
    
    print("✅ CRM structure created successfully!")
    print("✅ Headers added and formatted")
    print("✅ Data validation rules applied")
    print("✅ Dashboard with live metrics created")
    print("✅ Made shareable with write access")
    
    return spreadsheet_id, spreadsheet_url

def get_sheet_id(spreadsheet_result, sheet_name):
    """Get sheet ID by name"""
    for sheet in spreadsheet_result['sheets']:
        if sheet['properties']['title'] == sheet_name:
            return sheet['properties']['sheetId']
    return 0

def add_sample_data(sheets_service, spreadsheet_id):
    """Add some sample data to demonstrate the CRM"""
    
    print("📝 Adding sample data...")
    
    # Sample candidate data
    sample_candidates = [
        ['C001', 'John', 'Smith', 'john.smith@email.com', '(555) 123-4567', 
         'linkedin.com/in/johnsmith', 'ABC Construction', 'Project Manager', '8', 
         'Commercial', 'Scheduling, Budgeting, Team Leadership', 'Dallas, TX', 'Yes', 
         '$85,000', '$95,000', 'Immediate', 'resume_link', 'LinkedIn', '8.5', 
         'Active', '2026-03-01', 'Strong PM with commercial experience', '2026-03-01'],
        
        ['C002', 'Sarah', 'Johnson', 'sarah.j@email.com', '(555) 234-5678',
         'linkedin.com/in/sarahjohnson', 'XYZ Builders', 'Superintendent', '12',
         'Residential', 'Quality Control, Safety, Scheduling', 'Austin, TX', 'No',
         '$92,000', '$105,000', '2 weeks', 'resume_link', 'Referral', '9.2',
         'Active', '2026-03-02', 'Excellent superintendent, safety focused', '2026-03-02']
    ]
    
    # Sample client data
    sample_clients = [
        ['CL001', 'BuildCorp Inc', 'buildcorp.com', 'Commercial Construction', '250-500',
         'Mike Wilson', 'VP Operations', 'mike.wilson@buildcorp.com', '(555) 345-6789',
         'Lisa Chen', 'lisa.chen@buildcorp.com', '(555) 345-6790', '123 Main St',
         'Houston', 'TX', 'Active Client', 'Referral', '2026-03-01', '2026-03-15',
         'Yes', '$5,000 flat fee', 'Great relationship, multiple searches', '2026-02-15'],
        
        ['CL002', 'Premier Construction', 'premierconstruction.com', 'Infrastructure', '100-250',
         'David Brown', 'Owner', 'david@premierconstruction.com', '(555) 456-7890',
         '', '', '', '456 Oak Ave',
         'Dallas', 'TX', 'Prospect', 'Cold Outreach', '2026-03-03', '2026-03-10',
         'No', 'TBD', 'Initial interest shown', '2026-03-03']
    ]
    
    # Sample job order
    sample_jobs = [
        ['J001', 'CL001', 'BuildCorp Inc', 'Senior Project Manager', 'Operations',
         'Full-time', 'Houston, TX', 'No', '90000', '110000',
         '10% annual bonus', 'Full health, dental, 401k match', '5+ years commercial PM',
         'Scheduling, Budgeting, P6', 'LEED certification preferred', '2026-04-01',
         'Standard', 'Seeking experienced PM for $50M mixed-use project...',
         '2', '1', '0', 'Open', '5000', '2026-03-01', '2026-03-30', 'High priority search']
    ]
    
    # Add sample data
    ranges_data = [
        ('CANDIDATES!A2:W3', sample_candidates),
        ('CLIENTS!A2:W3', sample_clients),
        ('JOB_ORDERS!A2:Z2', [sample_jobs[0]])
    ]
    
    for range_name, data in ranges_data:
        sheets_service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='USER_ENTERED',
            body={'values': data}
        ).execute()
    
    print("✅ Sample data added!")

def main():
    """Main function to build the CRM"""
    print("🚀 Lemmik Recruiting CRM Builder Starting...")
    
    # Authenticate
    sheets_service, drive_service = authenticate_sheets()
    if not sheets_service:
        return
    
    # Create CRM
    spreadsheet_id, spreadsheet_url = create_recruiting_crm(sheets_service, drive_service)
    
    # Add sample data
    add_sample_data(sheets_service, spreadsheet_id)
    
    print(f"\n🎉 LEMMIK RECRUITING CRM IS READY!")
    print(f"📊 Access your CRM: {spreadsheet_url}")
    print(f"🆔 Spreadsheet ID: {spreadsheet_id}")
    
    # Save details for future use
    crm_details = {
        'spreadsheet_id': spreadsheet_id,
        'spreadsheet_url': spreadsheet_url,
        'created_date': datetime.now().isoformat(),
        'sheets': ['CANDIDATES', 'CLIENTS', 'JOB_ORDERS', 'PIPELINE', 'COMMUNICATIONS', 'DASHBOARD']
    }
    
    with open('lemmik_crm_details.json', 'w') as f:
        json.dump(crm_details, f, indent=2)
    
    print(f"💾 CRM details saved to: lemmik_crm_details.json")
    
    print(f"\n📋 NEXT STEPS:")
    print(f"1. Open the CRM and explore the structure")
    print(f"2. Customize fields as needed") 
    print(f"3. Start adding your candidate and client data")
    print(f"4. Use the DASHBOARD sheet to track your metrics")
    print(f"5. Ready to integrate with scraping and email systems!")

if __name__ == "__main__":
    main()