# 🚀 LEMMIK RECRUITING CRM - AIRTABLE SETUP GUIDE

## 🎯 QUICK START (15 Minutes)

### Step 1: Create Airtable Account & Base
1. **Go to:** [airtable.com](https://airtable.com)
2. **Sign up** for free account
3. **Create new base** → "Start from scratch"
4. **Name:** "Lemmik Construction Recruiting CRM"
5. **Upgrade to Pro:** $20/month (needed for automations)

### Step 2: Create Tables & Fields

#### 🧑‍💼 TABLE 1: CANDIDATES
**Delete default fields, create these:**

| Field Name | Field Type | Options/Description |
|------------|------------|---------------------|
| Full Name | Single line text | Primary field |
| Email | Email | |
| Phone | Phone number | |
| LinkedIn | URL | |
| Current Company | Single line text | |
| Current Title | Single line text | |
| Years Experience | Number | |
| Construction Focus | Single select | Commercial, Residential, Industrial, Infrastructure, Heavy Civil, Specialty, Mixed |
| Skills | Multiple select | Project Management, Scheduling, Budgeting, Estimating, Safety Management, Quality Control, Team Leadership, P6 Primavera, Procore, AutoCAD, BIM/Revit, OSHA 30, LEED Certified, PMP Certified |
| Location | Single line text | |
| Open to Relocate | Checkbox | |
| Current Salary | Currency | |
| Target Salary | Currency | |
| Availability | Single select | Immediate, 2 weeks, 1 month, 2-3 months, Passive |
| Resume | Attachment | |
| Source | Single select | LinkedIn Scraping, ZoomInfo, Company Website, Referral, Job Board, Cold Outreach, Networking |
| Quality Score | Number | 1-10 rating |
| Status | Single select | New, Active, Passive, Interviewing, Placed, Inactive |
| Last Contact | Date | |
| Next Follow-up | Date | |
| Notes | Long text | |
| Tags | Multiple select | Hot Lead, Top Performer, Executive Level, Seeking Growth, Underpaid, Remote OK, Travel OK, Security Clearance |
| Job Orders | Link to another record | Link to JOB_ORDERS table |
| Communications | Link to another record | Link to COMMUNICATIONS table |
| Date Added | Created time | |

#### 🏢 TABLE 2: CLIENTS
**Create new table called "CLIENTS":**

| Field Name | Field Type | Options/Description |
|------------|------------|---------------------|
| Company Name | Single line text | Primary field |
| Website | URL | |
| Industry Focus | Multiple select | Commercial Construction, Residential, Industrial, Infrastructure, Heavy Civil, Specialty Contracting, Design-Build, CM/GC |
| Company Size | Single select | 1-10 employees, 11-50, 51-200, 201-500, 500-1000, 1000+ |
| Revenue Range | Single select | Under $10M, $10-50M, $50-100M, $100-250M, $250M-1B, $1B+ |
| Primary Contact | Single line text | |
| Contact Title | Single line text | |
| Contact Email | Email | |
| Contact Phone | Phone number | |
| Address | Single line text | |
| City | Single line text | |
| State | Single select | All 50 states |
| Relationship Status | Single select | Cold Lead, Warm Lead, Active Prospect, Active Client, Past Client, Inactive |
| Lead Source | Single select | Cold Outreach, LinkedIn, Referral, Website Inquiry, Networking, Previous Relationship |
| Last Contact | Date | |
| Next Follow-up | Date | |
| Contract Signed | Checkbox | |
| Fee Agreement | Single select | $5,000 Flat Fee, Negotiated Rate, Retainer + Fee, TBD |
| Client Health Score | Number | 1-10 rating |
| Notes | Long text | |
| Job Orders | Link to another record | Link to JOB_ORDERS table |
| Communications | Link to another record | Link to COMMUNICATIONS table |
| Date Added | Created time | |

#### 💼 TABLE 3: JOB_ORDERS
**Create new table called "JOB_ORDERS":**

| Field Name | Field Type | Options/Description |
|------------|------------|---------------------|
| Position Title | Single line text | Primary field |
| Client | Link to another record | Link to CLIENTS table |
| Department | Single select | Executive/C-Suite, Project Management, Operations, Estimating, Business Development, Safety, Quality, Finance, HR, Field Operations |
| Employment Type | Single select | Full-time, Contract, Contract-to-hire, Part-time |
| Location | Single line text | |
| Remote OK | Checkbox | |
| Salary Min | Currency | |
| Salary Max | Currency | |
| Bonus Structure | Single line text | |
| Benefits | Long text | |
| Required Experience | Long text | |
| Required Skills | Multiple select | Same as CANDIDATES Skills |
| Preferred Skills | Long text | |
| Start Date | Date | |
| Urgency | Single select | ASAP (1-2 weeks), Urgent (2-4 weeks), Standard (4-6 weeks), Flexible (6+ weeks) |
| Job Description | Long text | |
| Candidates Submitted | Number | |
| Interviews | Number | |
| Offers | Number | |
| Status | Single select | Open, On Hold, Filled, Cancelled, Lost |
| Fee Amount | Currency | |
| Target Fill Date | Date | |
| Priority | Single select | Low, Medium, High, Critical |
| Notes | Long text | |
| Pipeline Deals | Link to another record | Link to PIPELINE table |
| Date Created | Created time | |

#### 📈 TABLE 4: PIPELINE  
**Create new table called "PIPELINE":**

| Field Name | Field Type | Options/Description |
|------------|------------|---------------------|
| Deal Name | Formula | `{Job Order} & ' - ' & {Candidate}` |
| Job Order | Link to another record | Link to JOB_ORDERS table |
| Candidate | Link to another record | Link to CANDIDATES table |
| Stage | Single select | New Lead, Qualified, Submitted, Phone Screen, Interview Scheduled, Interview Complete, Reference Check, Offer Pending, Offer Made, Offer Accepted, Placed, Lost |
| Submitted Date | Date | |
| Interview Date | Date | |
| Client Feedback | Long text | |
| Next Steps | Single line text | |
| Close Probability | Single select | 10%, 25%, 50%, 75%, 90%, 100%, 0% - Lost |
| Fee Amount | Currency | |
| Expected Close Date | Date | |
| Weighted Value | Formula | See formula in structure file |
| Days in Stage | Formula | `DATETIME_DIFF(TODAY(), {Last Updated}, 'days')` |
| Status | Single select | Active, Placed, Lost, On Hold |
| Lost Reason | Single select | Salary Mismatch, Location, Not Interested, Counter Offer, Skills Gap, Cultural Fit, Reference Issue, Other |
| Notes | Long text | |
| Communications | Link to another record | Link to COMMUNICATIONS table |
| Last Updated | Last modified time | |

#### 💬 TABLE 5: COMMUNICATIONS
**Create new table called "COMMUNICATIONS":**

| Field Name | Field Type | Options/Description |
|------------|------------|---------------------|
| Subject | Single line text | Primary field |
| Type | Single select | Email, Phone Call, Text/SMS, LinkedIn Message, In-Person Meeting, Video Call, Voicemail, Letter |
| Direction | Single select | Outbound, Inbound |
| Contact Type | Single select | Candidate, Client, Reference, Other |
| Candidate | Link to another record | Link to CANDIDATES table |
| Client | Link to another record | Link to CLIENTS table |
| Pipeline Deal | Link to another record | Link to PIPELINE table |
| Content | Long text | |
| Outcome | Single select | Successful, No Response, Left Voicemail, Scheduled Follow-up, Not Interested, Interested, Need More Info |
| Follow-up Required | Checkbox | |
| Follow-up Date | Date | |
| Priority | Single select | Low, Medium, High, Urgent |
| Created By | Single line text | |
| Date Created | Created time | |

### Step 3: Create Views

#### CANDIDATES Views:
1. **All Candidates** (Grid view)
2. **Active Candidates** (Grid, filter: Status = 'Active')
3. **Top Performers** (Grid, filter: Quality Score >= 8)
4. **Available Now** (Grid, filter: Availability = 'Immediate')
5. **By Location** (Grid, grouped by Location)
6. **Need Follow-up** (Grid, filter: Next Follow-up <= TODAY())
7. **Candidate Cards** (Gallery view, cover field: Resume)

#### CLIENTS Views:
1. **All Clients** (Grid view)
2. **Active Clients** (Grid, filter: Relationship Status = 'Active Client')  
3. **Prospects** (Grid, filter: Relationship Status IN ('Warm Lead', 'Active Prospect'))
4. **Need Follow-up** (Grid, filter: Next Follow-up <= TODAY())
5. **By State** (Grid, grouped by State)
6. **Client Health** (Grid, sorted by Client Health Score DESC)

#### JOB_ORDERS Views:
1. **All Jobs** (Grid view)
2. **Open Jobs** (Grid, filter: Status = 'Open')
3. **Urgent Jobs** (Grid, filter: Urgency IN ('ASAP (1-2 weeks)', 'Urgent (2-4 weeks)'))
4. **By Client** (Grid, grouped by Client)
5. **Calendar View** (Calendar view, date field: Target Fill Date)

#### PIPELINE Views:
1. **All Deals** (Grid view)
2. **Active Pipeline** (Grid, filter: Status = 'Active')
3. **Kanban Board** (Kanban view, grouped by Stage) ⭐ **MAIN VIEW**
4. **High Probability** (Grid, filter: Close Probability IN ('75%', '90%', '100%'))
5. **This Month Closes** (Grid, filter: Expected Close Date THIS_MONTH())
6. **Overdue Deals** (Grid, filter: Expected Close Date < TODAY())

#### COMMUNICATIONS Views:
1. **All Communications** (Grid view)
2. **Need Follow-up** (Grid, filter: Follow-up Required = TRUE)
3. **This Week** (Grid, filter: Date Created THIS_WEEK())
4. **By Type** (Grid, grouped by Type)
5. **Calendar View** (Calendar view, date field: Follow-up Date)

### Step 4: Set Up Automations (Pro Plan Required)

1. **New Candidate Welcome Email**
   - Trigger: When record created in CANDIDATES
   - Action: Send email notification

2. **Follow-up Reminders**
   - Trigger: Daily at 9 AM
   - Condition: Follow-up Date = TODAY()
   - Action: Send notification

3. **Pipeline Stage Updates**  
   - Trigger: When Pipeline Stage changes
   - Action: Update Job Order statistics

4. **Quality Score Calculator**
   - Trigger: When Candidate record updated
   - Action: Auto-calculate quality score

### Step 5: Import Sample Data

Copy sample data from `airtable_sample_data.json` to test your setup:

**CANDIDATES Sample:**
- John Smith (Project Manager, Dallas)
- Sarah Johnson (Superintendent, Austin)

**CLIENTS Sample:**
- BuildCorp Inc (Active Client, Houston)

### Step 6: Customize & Test

1. **Adjust field widths** in grid views
2. **Set up conditional formatting** for priorities
3. **Create dashboard with charts** (Pro feature)
4. **Test linked records** between tables
5. **Verify formulas** are calculating correctly

## 🎯 DAILY WORKFLOW

### Morning Routine (5 minutes):
1. **Check COMMUNICATIONS → Need Follow-up view**
2. **Review PIPELINE → Kanban Board** for stage updates
3. **Quick scan of CANDIDATES → Need Follow-up**

### Client Calls:
1. **Add new records** to JOB_ORDERS table
2. **Link to CLIENT** record automatically  
3. **Create PIPELINE deals** for submitted candidates
4. **Log call notes** in COMMUNICATIONS table

### Candidate Outreach:
1. **Use CANDIDATES → Available Now** view
2. **Log all touchpoints** in COMMUNICATIONS  
3. **Update Next Follow-up dates**
4. **Move promising candidates** to Active status

## 💰 COST BREAKDOWN

- **Free Plan**: 1,200 records per base (good for testing)
- **Pro Plan**: $20/month/user (unlimited records + automations)
- **ROI**: One $5K placement = 25 months of Pro plan!

## 🚀 NEXT INTEGRATIONS

Once your CRM is running:

1. **Web scraping** → Auto-populate CANDIDATES
2. **Email integration** → Auto-log COMMUNICATIONS
3. **Resume parsing** → Extract skills automatically  
4. **Zapier connections** → Connect to other tools
5. **API access** → Custom automations

## 🎉 YOU'RE READY!

Your Airtable CRM is now a professional recruiting powerhouse that can:
- ✅ Track 1000+ construction professionals
- ✅ Manage client relationships and $5K contracts  
- ✅ Monitor active searches and placements
- ✅ Forecast revenue with weighted pipeline
- ✅ Automate follow-ups and reminders
- ✅ Scale your flat-fee recruiting business

**Time to start filling that pipeline!** 🏗️💰