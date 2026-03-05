# 🏗️ LEMMIK RECRUITING CRM SETUP GUIDE

## 🚀 QUICK SETUP (5 Minutes)

### Step 1: Create Your Google Sheet
1. Go to [Google Sheets](https://docs.google.com/spreadsheets/create)
2. Name it: **"Lemmik Recruiting CRM"**
3. Create 5 tabs: **CANDIDATES**, **CLIENTS**, **JOB_ORDERS**, **PIPELINE**, **COMMUNICATIONS**

### Step 2: Copy Headers
Use the headers from `crm_structure.json` for each sheet:

**CANDIDATES Headers (Row 1):**
```
ID | First Name | Last Name | Email | Phone | LinkedIn | Current Company | Current Title | Years Experience | Construction Focus | Skills | Location | Open to Relocate? | Current Salary | Target Salary | Availability | Resume Link | Source | Quality Score | Status | Last Contact | Notes | Date Added
```

**CLIENTS Headers (Row 1):**
```
Client ID | Company Name | Website | Industry Focus | Company Size | Primary Contact | Contact Title | Contact Email | Contact Phone | Secondary Contact | Secondary Email | Secondary Phone | Address | City | State | Relationship Status | Lead Source | Last Contact | Next Follow-up | Contract Signed? | Fee Agreement | Notes | Date Added
```

**JOB_ORDERS Headers (Row 1):**
```
Job ID | Client ID | Company Name | Position Title | Department | Employment Type | Location | Remote OK? | Salary Min | Salary Max | Bonus Structure | Benefits | Required Experience | Required Skills | Preferred Skills | Start Date | Urgency | Job Description | Candidates Submitted | Interviews | Offers | Status | Fee Amount | Date Created | Target Fill Date | Notes
```

**PIPELINE Headers (Row 1):**
```
Deal ID | Job ID | Company | Position | Stage | Candidate Name | Submitted Date | Interview Date | Feedback | Next Steps | Close Probability | Fee Amount | Expected Close Date | Status | Notes | Last Updated
```

**COMMUNICATIONS Headers (Row 1):**
```
Comm ID | Type | Contact Type | Contact ID | Contact Name | Company | Date/Time | Subject | Content/Notes | Follow-up Required? | Follow-up Date | Status | Created By
```

### Step 3: Format Your Sheets
For each sheet:
1. **Select Row 1** (headers)
2. **Format** → **Bold** + **Background Color** (Blue)
3. **View** → **Freeze** → **1 row**
4. **Adjust column widths** as needed

### Step 4: Add Sample Data
Copy sample data from `crm_sample_data.csv` to test your setup.

## 🎯 ADVANCED FEATURES

### Data Validation Dropdowns

**CANDIDATES Status Column (T):**
1. Select column T (Status)
2. **Data** → **Data validation**
3. **Criteria**: List of items
4. **Values**: `New, Active, Passive, Interviewing, Placed, Inactive`

**PIPELINE Stage Column (E):**
1. Select column E (Stage)
2. **Data** → **Data validation**
3. **Criteria**: List of items
4. **Values**: `New Lead, Qualified, Submitted, Interview Scheduled, Interview Complete, Reference Check, Offer Made, Offer Accepted, Placed, Lost`

### Useful Formulas

**Auto-populate Date Added (CANDIDATES W column):**
```excel
=IF(B2<>"",IF(W2="",TODAY(),W2),"")
```

**Calculate Days Since Last Contact (CANDIDATES):**
```excel
=IF(U2<>"",TODAY()-U2,"")
```

**Pipeline Value Calculation (PIPELINE L column):**
```excel
=IF(K2<>"",K2/100*L2,0)
```

**Count Active Candidates:**
```excel
=COUNTIF(CANDIDATES!T:T,"Active")
```

**This Month Revenue:**
```excel
=SUMIFS(PIPELINE!L:L,PIPELINE!N:N,"Placed",PIPELINE!P:P,">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1))
```

## 📊 DASHBOARD CREATION

Create a 6th sheet called **DASHBOARD** with these metrics:

| METRIC | FORMULA | TARGET |
|--------|---------|--------|
| Total Candidates | `=COUNTA(CANDIDATES!A:A)-1` | 1000 |
| Active Candidates | `=COUNTIF(CANDIDATES!T:T,"Active")` | 500 |
| Total Clients | `=COUNTA(CLIENTS!A:A)-1` | 50 |
| Active Job Orders | `=COUNTIF(JOB_ORDERS!V:V,"Open")` | 10 |
| Pipeline Value | `=SUMIF(PIPELINE!N:N,"Active",PIPELINE!L:L)` | $50,000 |
| This Month Placements | `=COUNTIFS(PIPELINE!N:N,"Placed",PIPELINE!P:P,">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1))` | 5 |
| Revenue This Month | `=SUMIFS(PIPELINE!L:L,PIPELINE!N:N,"Placed",PIPELINE!P:P,">="&DATE(YEAR(TODAY()),MONTH(TODAY()),1))` | $25,000 |

## 🔧 AUTOMATION IDEAS

### Email Integration
- Use Google Apps Script to automatically log emails
- Parse candidate emails and extract resume attachments
- Send automated follow-up sequences

### Candidate Scoring
Create a scoring formula in CANDIDATES S column:
```excel
=IF(I2<>"", 
  (MIN(I2,15)/15 * 40) +  // Experience (40%)
  (IF(L2="Yes",20,10)) +   // Relocation (20%)
  (IF(P2="Immediate",20,IF(P2="2 weeks",15,10))) + // Availability (20%)
  (IF(F2<>"",20,0))        // LinkedIn Profile (20%)
, "")
```

### Client Health Score
Create a relationship score in CLIENTS:
```excel
=IF(P2="Active Client",10,IF(P2="Warm Lead",7,IF(P2="Prospect",5,3))) +
 IF(T2="Yes",5,0) +        // Contract Signed
 IF(R2<TODAY()-30,0,3)     // Recent Contact
```

## 🚀 NEXT STEPS INTEGRATION

Once your CRM is ready, we can integrate:

1. **Web Scraping** → Automatically populate CANDIDATES
2. **Email Automation** → Log in COMMUNICATIONS  
3. **Resume Parsing** → Extract skills and experience
4. **Client Portal** → Submit candidates from PIPELINE
5. **Reporting** → Automated weekly/monthly reports

## 💡 PRO TIPS

1. **Use Conditional Formatting** to highlight:
   - Overdue follow-ups (red)
   - High-probability deals (green)
   - Urgent job orders (yellow)

2. **Create Views/Filters**:
   - Active candidates by location
   - Open jobs by urgency  
   - Pipeline by stage

3. **Share Strategically**:
   - Full access for you
   - View-only for clients (specific sheets)
   - Comment access for team members

4. **Backup Regularly**:
   - Export to Excel monthly
   - Use Google Sheet version history

Your CRM is now ready to scale your $5K flat-fee recruiting business! 🏗️💰