#!/usr/bin/env python3

import json
from datetime import datetime, timedelta

def create_airtable_crm_structure():
    """Create optimized Airtable base structure for construction recruiting"""
    
    crm_structure = {
        "base_name": "Lemmik Construction Recruiting CRM",
        "description": "Complete CRM for $5K flat-fee construction recruiting business",
        "tables": {
            
            "CANDIDATES": {
                "description": "Construction professionals database",
                "primary_field": "Full Name",
                "fields": [
                    {"name": "Full Name", "type": "singleLineText", "description": "First + Last name"},
                    {"name": "Email", "type": "email", "description": "Primary email address"},
                    {"name": "Phone", "type": "phoneNumber", "description": "Mobile phone"},
                    {"name": "LinkedIn", "type": "url", "description": "LinkedIn profile URL"},
                    {"name": "Current Company", "type": "singleLineText", "description": "Current employer"},
                    {"name": "Current Title", "type": "singleLineText", "description": "Current job title"},
                    {"name": "Years Experience", "type": "number", "description": "Total years in construction"},
                    {"name": "Construction Focus", "type": "singleSelect", "options": [
                        "Commercial", "Residential", "Industrial", "Infrastructure", 
                        "Heavy Civil", "Specialty", "Mixed"
                    ]},
                    {"name": "Skills", "type": "multipleSelects", "options": [
                        "Project Management", "Scheduling", "Budgeting", "Estimating", 
                        "Safety Management", "Quality Control", "Team Leadership", 
                        "P6 Primavera", "Procore", "AutoCAD", "BIM/Revit", "OSHA 30",
                        "LEED Certified", "PMP Certified"
                    ]},
                    {"name": "Location", "type": "singleLineText", "description": "Current location"},
                    {"name": "Open to Relocate", "type": "checkbox", "description": "Willing to relocate"},
                    {"name": "Current Salary", "type": "currency", "description": "Current base salary"},
                    {"name": "Target Salary", "type": "currency", "description": "Desired salary"},
                    {"name": "Availability", "type": "singleSelect", "options": [
                        "Immediate", "2 weeks", "1 month", "2-3 months", "Passive"
                    ]},
                    {"name": "Resume", "type": "attachment", "description": "Resume file"},
                    {"name": "Source", "type": "singleSelect", "options": [
                        "LinkedIn Scraping", "ZoomInfo", "Company Website", "Referral", 
                        "Job Board", "Cold Outreach", "Networking"
                    ]},
                    {"name": "Quality Score", "type": "number", "description": "1-10 candidate rating"},
                    {"name": "Status", "type": "singleSelect", "options": [
                        "New", "Active", "Passive", "Interviewing", "Placed", "Inactive"
                    ]},
                    {"name": "Last Contact", "type": "date", "description": "Last communication date"},
                    {"name": "Next Follow-up", "type": "date", "description": "Scheduled follow-up"},
                    {"name": "Notes", "type": "longText", "description": "Internal notes"},
                    {"name": "Tags", "type": "multipleSelects", "options": [
                        "Hot Lead", "Top Performer", "Executive Level", "Seeking Growth",
                        "Underpaid", "Remote OK", "Travel OK", "Security Clearance"
                    ]},
                    {"name": "Job Orders", "type": "linkToAnotherRecord", "linkedTable": "JOB_ORDERS"},
                    {"name": "Communications", "type": "linkToAnotherRecord", "linkedTable": "COMMUNICATIONS"},
                    {"name": "Date Added", "type": "createdTime"}
                ]
            },

            "CLIENTS": {
                "description": "Construction companies who hire talent",
                "primary_field": "Company Name",
                "fields": [
                    {"name": "Company Name", "type": "singleLineText", "description": "Client company name"},
                    {"name": "Website", "type": "url", "description": "Company website"},
                    {"name": "Industry Focus", "type": "multipleSelects", "options": [
                        "Commercial Construction", "Residential", "Industrial", "Infrastructure",
                        "Heavy Civil", "Specialty Contracting", "Design-Build", "CM/GC"
                    ]},
                    {"name": "Company Size", "type": "singleSelect", "options": [
                        "1-10 employees", "11-50", "51-200", "201-500", "500-1000", "1000+"
                    ]},
                    {"name": "Revenue Range", "type": "singleSelect", "options": [
                        "Under $10M", "$10-50M", "$50-100M", "$100-250M", "$250M-1B", "$1B+"
                    ]},
                    {"name": "Primary Contact", "type": "singleLineText", "description": "Main decision maker"},
                    {"name": "Contact Title", "type": "singleLineText", "description": "Primary contact job title"},
                    {"name": "Contact Email", "type": "email", "description": "Primary contact email"},
                    {"name": "Contact Phone", "type": "phoneNumber", "description": "Primary contact phone"},
                    {"name": "Address", "type": "singleLineText", "description": "Company address"},
                    {"name": "City", "type": "singleLineText", "description": "City"},
                    {"name": "State", "type": "singleSelect", "options": [
                        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", 
                        "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", 
                        "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", 
                        "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
                    ]},
                    {"name": "Relationship Status", "type": "singleSelect", "options": [
                        "Cold Lead", "Warm Lead", "Active Prospect", "Active Client", "Past Client", "Inactive"
                    ]},
                    {"name": "Lead Source", "type": "singleSelect", "options": [
                        "Cold Outreach", "LinkedIn", "Referral", "Website Inquiry", "Networking", "Previous Relationship"
                    ]},
                    {"name": "Last Contact", "type": "date", "description": "Last communication"},
                    {"name": "Next Follow-up", "type": "date", "description": "Scheduled follow-up"},
                    {"name": "Contract Signed", "type": "checkbox", "description": "Signed service agreement"},
                    {"name": "Fee Agreement", "type": "singleSelect", "options": [
                        "$5,000 Flat Fee", "Negotiated Rate", "Retainer + Fee", "TBD"
                    ]},
                    {"name": "Client Health Score", "type": "number", "description": "1-10 relationship strength"},
                    {"name": "Notes", "type": "longText", "description": "Client relationship notes"},
                    {"name": "Job Orders", "type": "linkToAnotherRecord", "linkedTable": "JOB_ORDERS"},
                    {"name": "Communications", "type": "linkToAnotherRecord", "linkedTable": "COMMUNICATIONS"},
                    {"name": "Date Added", "type": "createdTime"}
                ]
            },

            "JOB_ORDERS": {
                "description": "Active construction searches",
                "primary_field": "Position Title",
                "fields": [
                    {"name": "Position Title", "type": "singleLineText", "description": "Job title"},
                    {"name": "Client", "type": "linkToAnotherRecord", "linkedTable": "CLIENTS"},
                    {"name": "Department", "type": "singleSelect", "options": [
                        "Executive/C-Suite", "Project Management", "Operations", "Estimating",
                        "Business Development", "Safety", "Quality", "Finance", "HR", "Field Operations"
                    ]},
                    {"name": "Employment Type", "type": "singleSelect", "options": [
                        "Full-time", "Contract", "Contract-to-hire", "Part-time"
                    ]},
                    {"name": "Location", "type": "singleLineText", "description": "Job location"},
                    {"name": "Remote OK", "type": "checkbox", "description": "Remote work allowed"},
                    {"name": "Salary Min", "type": "currency", "description": "Minimum salary"},
                    {"name": "Salary Max", "type": "currency", "description": "Maximum salary"},
                    {"name": "Bonus Structure", "type": "singleLineText", "description": "Bonus/incentive details"},
                    {"name": "Benefits", "type": "longText", "description": "Benefits package"},
                    {"name": "Required Experience", "type": "longText", "description": "Must-have experience"},
                    {"name": "Required Skills", "type": "multipleSelects", "options": [
                        "Project Management", "Scheduling", "Budgeting", "Estimating", 
                        "Safety Management", "Quality Control", "Team Leadership", 
                        "P6 Primavera", "Procore", "AutoCAD", "BIM/Revit", "OSHA 30"
                    ]},
                    {"name": "Preferred Skills", "type": "longText", "description": "Nice-to-have skills"},
                    {"name": "Start Date", "type": "date", "description": "Desired start date"},
                    {"name": "Urgency", "type": "singleSelect", "options": [
                        "ASAP (1-2 weeks)", "Urgent (2-4 weeks)", "Standard (4-6 weeks)", "Flexible (6+ weeks)"
                    ]},
                    {"name": "Job Description", "type": "longText", "description": "Full job description"},
                    {"name": "Candidates Submitted", "type": "number", "description": "Total candidates submitted"},
                    {"name": "Interviews", "type": "number", "description": "Candidates interviewed"},
                    {"name": "Offers", "type": "number", "description": "Offers made"},
                    {"name": "Status", "type": "singleSelect", "options": [
                        "Open", "On Hold", "Filled", "Cancelled", "Lost"
                    ]},
                    {"name": "Fee Amount", "type": "currency", "description": "Search fee amount"},
                    {"name": "Target Fill Date", "type": "date", "description": "Goal completion date"},
                    {"name": "Priority", "type": "singleSelect", "options": ["Low", "Medium", "High", "Critical"]},
                    {"name": "Notes", "type": "longText", "description": "Search notes"},
                    {"name": "Pipeline Deals", "type": "linkToAnotherRecord", "linkedTable": "PIPELINE"},
                    {"name": "Date Created", "type": "createdTime"}
                ]
            },

            "PIPELINE": {
                "description": "Deal tracking and revenue forecasting",
                "primary_field": "Deal Name",
                "fields": [
                    {"name": "Deal Name", "type": "formula", "formula": "{Job Order} & ' - ' & {Candidate}"},
                    {"name": "Job Order", "type": "linkToAnotherRecord", "linkedTable": "JOB_ORDERS"},
                    {"name": "Candidate", "type": "linkToAnotherRecord", "linkedTable": "CANDIDATES"},
                    {"name": "Stage", "type": "singleSelect", "options": [
                        "New Lead", "Qualified", "Submitted", "Phone Screen", 
                        "Interview Scheduled", "Interview Complete", "Reference Check", 
                        "Offer Pending", "Offer Made", "Offer Accepted", "Placed", "Lost"
                    ]},
                    {"name": "Submitted Date", "type": "date", "description": "Date candidate submitted"},
                    {"name": "Interview Date", "type": "date", "description": "Interview date"},
                    {"name": "Client Feedback", "type": "longText", "description": "Client interview feedback"},
                    {"name": "Next Steps", "type": "singleLineText", "description": "Action items"},
                    {"name": "Close Probability", "type": "singleSelect", "options": [
                        "10%", "25%", "50%", "75%", "90%", "100%", "0% - Lost"
                    ]},
                    {"name": "Fee Amount", "type": "currency", "description": "Expected revenue"},
                    {"name": "Expected Close Date", "type": "date", "description": "Estimated placement date"},
                    {"name": "Weighted Value", "type": "formula", "formula": "IF({Close Probability} = '100%', {Fee Amount}, IF({Close Probability} = '90%', {Fee Amount} * 0.9, IF({Close Probability} = '75%', {Fee Amount} * 0.75, IF({Close Probability} = '50%', {Fee Amount} * 0.5, IF({Close Probability} = '25%', {Fee Amount} * 0.25, IF({Close Probability} = '10%', {Fee Amount} * 0.1, 0))))))"},
                    {"name": "Days in Stage", "type": "formula", "formula": "DATETIME_DIFF(TODAY(), {Last Updated}, 'days')"},
                    {"name": "Status", "type": "singleSelect", "options": [
                        "Active", "Placed", "Lost", "On Hold"
                    ]},
                    {"name": "Lost Reason", "type": "singleSelect", "options": [
                        "Salary Mismatch", "Location", "Not Interested", "Counter Offer", 
                        "Skills Gap", "Cultural Fit", "Reference Issue", "Other"
                    ]},
                    {"name": "Notes", "type": "longText", "description": "Deal notes"},
                    {"name": "Communications", "type": "linkToAnotherRecord", "linkedTable": "COMMUNICATIONS"},
                    {"name": "Last Updated", "type": "lastModifiedTime"}
                ]
            },

            "COMMUNICATIONS": {
                "description": "All touchpoints with candidates and clients",
                "primary_field": "Subject",
                "fields": [
                    {"name": "Subject", "type": "singleLineText", "description": "Communication subject"},
                    {"name": "Type", "type": "singleSelect", "options": [
                        "Email", "Phone Call", "Text/SMS", "LinkedIn Message", "In-Person Meeting", 
                        "Video Call", "Voicemail", "Letter"
                    ]},
                    {"name": "Direction", "type": "singleSelect", "options": ["Outbound", "Inbound"]},
                    {"name": "Contact Type", "type": "singleSelect", "options": ["Candidate", "Client", "Reference", "Other"]},
                    {"name": "Candidate", "type": "linkToAnotherRecord", "linkedTable": "CANDIDATES"},
                    {"name": "Client", "type": "linkToAnotherRecord", "linkedTable": "CLIENTS"},
                    {"name": "Pipeline Deal", "type": "linkToAnotherRecord", "linkedTable": "PIPELINE"},
                    {"name": "Content", "type": "longText", "description": "Communication content/notes"},
                    {"name": "Outcome", "type": "singleSelect", "options": [
                        "Successful", "No Response", "Left Voicemail", "Scheduled Follow-up", 
                        "Not Interested", "Interested", "Need More Info"
                    ]},
                    {"name": "Follow-up Required", "type": "checkbox", "description": "Needs follow-up"},
                    {"name": "Follow-up Date", "type": "date", "description": "Scheduled follow-up"},
                    {"name": "Priority", "type": "singleSelect", "options": ["Low", "Medium", "High", "Urgent"]},
                    {"name": "Created By", "type": "singleLineText", "description": "Team member name"},
                    {"name": "Date Created", "type": "createdTime"}
                ]
            }
        },
        
        "views": {
            "CANDIDATES": [
                {"name": "All Candidates", "type": "grid"},
                {"name": "Active Candidates", "type": "grid", "filter": "Status = 'Active'"},
                {"name": "Top Performers", "type": "grid", "filter": "Quality Score >= 8"},
                {"name": "Available Now", "type": "grid", "filter": "Availability = 'Immediate'"},
                {"name": "By Location", "type": "grid", "group": "Location"},
                {"name": "Need Follow-up", "type": "grid", "filter": "Next Follow-up <= TODAY()"},
                {"name": "Candidate Cards", "type": "gallery", "cover": "Resume"}
            ],
            "CLIENTS": [
                {"name": "All Clients", "type": "grid"},
                {"name": "Active Clients", "type": "grid", "filter": "Relationship Status = 'Active Client'"},
                {"name": "Prospects", "type": "grid", "filter": "Relationship Status IN ('Warm Lead', 'Active Prospect')"},
                {"name": "Need Follow-up", "type": "grid", "filter": "Next Follow-up <= TODAY()"},
                {"name": "By State", "type": "grid", "group": "State"},
                {"name": "Client Health", "type": "grid", "sort": "Client Health Score DESC"}
            ],
            "JOB_ORDERS": [
                {"name": "All Jobs", "type": "grid"},
                {"name": "Open Jobs", "type": "grid", "filter": "Status = 'Open'"},
                {"name": "Urgent Jobs", "type": "grid", "filter": "Urgency IN ('ASAP (1-2 weeks)', 'Urgent (2-4 weeks)')"},
                {"name": "By Client", "type": "grid", "group": "Client"},
                {"name": "Calendar View", "type": "calendar", "date": "Target Fill Date"}
            ],
            "PIPELINE": [
                {"name": "All Deals", "type": "grid"},
                {"name": "Active Pipeline", "type": "grid", "filter": "Status = 'Active'"},
                {"name": "Kanban Board", "type": "kanban", "group": "Stage"},
                {"name": "High Probability", "type": "grid", "filter": "Close Probability IN ('75%', '90%', '100%')"},
                {"name": "This Month Closes", "type": "grid", "filter": "Expected Close Date THIS_MONTH()"},
                {"name": "Overdue Deals", "type": "grid", "filter": "Expected Close Date < TODAY()"}
            ],
            "COMMUNICATIONS": [
                {"name": "All Communications", "type": "grid"},
                {"name": "Need Follow-up", "type": "grid", "filter": "Follow-up Required = TRUE"},
                {"name": "This Week", "type": "grid", "filter": "Date Created THIS_WEEK()"},
                {"name": "By Type", "type": "grid", "group": "Type"},
                {"name": "Calendar View", "type": "calendar", "date": "Follow-up Date"}
            ]
        },
        
        "automations": [
            {
                "name": "New Candidate Welcome Email",
                "trigger": "Record created in CANDIDATES",
                "actions": ["Send email to candidate with company info and next steps"]
            },
            {
                "name": "Follow-up Reminders", 
                "trigger": "Daily at 9 AM",
                "condition": "Follow-up Date = TODAY()",
                "actions": ["Send notification with list of follow-ups due"]
            },
            {
                "name": "Pipeline Stage Updates",
                "trigger": "Pipeline Stage changes",
                "actions": ["Update Job Order statistics", "Log activity in Communications"]
            },
            {
                "name": "Quality Score Calculator",
                "trigger": "Candidate record updated",
                "actions": ["Auto-calculate quality score based on experience, availability, location match"]
            }
        ]
    }
    
    return crm_structure

def create_sample_data():
    """Create sample data for testing the CRM"""
    
    sample_data = {
        "CANDIDATES": [
            {
                "Full Name": "John Smith",
                "Email": "john.smith@email.com",
                "Phone": "(555) 123-4567",
                "LinkedIn": "https://linkedin.com/in/johnsmith",
                "Current Company": "ABC Construction",
                "Current Title": "Project Manager",
                "Years Experience": 8,
                "Construction Focus": "Commercial",
                "Skills": ["Project Management", "Scheduling", "Budgeting", "Team Leadership"],
                "Location": "Dallas, TX",
                "Open to Relocate": True,
                "Current Salary": 85000,
                "Target Salary": 95000,
                "Availability": "Immediate",
                "Source": "LinkedIn Scraping",
                "Quality Score": 8.5,
                "Status": "Active",
                "Last Contact": "2026-03-01",
                "Notes": "Strong PM with commercial experience. Very interested in growth opportunities.",
                "Tags": ["Hot Lead", "Top Performer"]
            },
            {
                "Full Name": "Sarah Johnson", 
                "Email": "sarah.j@email.com",
                "Phone": "(555) 234-5678",
                "LinkedIn": "https://linkedin.com/in/sarahjohnson",
                "Current Company": "XYZ Builders",
                "Current Title": "Superintendent",
                "Years Experience": 12,
                "Construction Focus": "Residential",
                "Skills": ["Quality Control", "Safety Management", "Scheduling", "OSHA 30"],
                "Location": "Austin, TX", 
                "Open to Relocate": False,
                "Current Salary": 92000,
                "Target Salary": 105000,
                "Availability": "2 weeks",
                "Source": "Referral",
                "Quality Score": 9.2,
                "Status": "Active",
                "Last Contact": "2026-03-02",
                "Notes": "Excellent superintendent with strong safety focus. Not willing to relocate.",
                "Tags": ["Top Performer", "Safety Expert"]
            }
        ],
        
        "CLIENTS": [
            {
                "Company Name": "BuildCorp Inc",
                "Website": "https://buildcorp.com",
                "Industry Focus": ["Commercial Construction", "Design-Build"],
                "Company Size": "250-500",
                "Revenue Range": "$100-250M",
                "Primary Contact": "Mike Wilson",
                "Contact Title": "VP Operations",
                "Contact Email": "mike.wilson@buildcorp.com",
                "Contact Phone": "(555) 345-6789",
                "Address": "123 Main St",
                "City": "Houston",
                "State": "TX",
                "Relationship Status": "Active Client",
                "Lead Source": "Referral",
                "Last Contact": "2026-03-01",
                "Next Follow-up": "2026-03-15",
                "Contract Signed": True,
                "Fee Agreement": "$5,000 Flat Fee",
                "Client Health Score": 9,
                "Notes": "Great relationship. Multiple successful searches. Always pays on time."
            }
        ]
    }
    
    return sample_data

def main():
    """Generate Airtable CRM structure and instructions"""
    
    print("🚀 Building Lemmik Recruiting CRM for Airtable...")
    
    # Create structure
    crm_structure = create_airtable_crm_structure()
    sample_data = create_sample_data()
    
    # Save to files
    with open('airtable_crm_structure.json', 'w') as f:
        json.dump(crm_structure, f, indent=2)
    
    with open('airtable_sample_data.json', 'w') as f:
        json.dump(sample_data, f, indent=2)
    
    print("✅ Airtable CRM structure saved to airtable_crm_structure.json")
    print("✅ Sample data saved to airtable_sample_data.json")
    
    print(f"\n🏗️ LEMMIK RECRUITING CRM - AIRTABLE SETUP")
    print("=" * 60)
    
    print(f"\n📋 BASE STRUCTURE:")
    print(f"Base Name: {crm_structure['base_name']}")
    print(f"Tables: {len(crm_structure['tables'])}")
    print(f"Total Views: {sum(len(views) for views in crm_structure['views'].values())}")
    print(f"Automations: {len(crm_structure['automations'])}")
    
    print(f"\n📊 TABLES TO CREATE:")
    for table_name, table_info in crm_structure['tables'].items():
        print(f"• {table_name}: {len(table_info['fields'])} fields - {table_info['description']}")
    
    print(f"\n🚀 NEXT STEPS:")
    print(f"1. Go to airtable.com and create a new base")
    print(f"2. Use the structure in airtable_crm_structure.json") 
    print(f"3. Import sample data from airtable_sample_data.json")
    print(f"4. Set up views and automations")
    print(f"5. Ready to integrate with web scraping!")
    
    print(f"\n💰 COST: $20/month for Pro plan (needed for automations)")
    print(f"🎯 ROI: One $5K placement pays for 25 months of Airtable!")

if __name__ == "__main__":
    main()