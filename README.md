# LinkedIn Job Title Analytics

This project uses LinkedIn's API to analyze the distribution of your Target Job Title positions across different countries.

## Prerequisites

1. LinkedIn Developer Account
2. LinkedIn API Access Token
   - Go to [LinkedIn Developer Portal](https://developer.linkedin.com/)
   - Create an application
   - Request access to Marketing Developer Platform
   - Generate an access token with the following scopes:
     - r_emailaddress
     - r_liteprofile
     - r_ads_reporting

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file from the template:
```bash
cp .env.example .env
```

3. Add your LinkedIn API access token to the `.env` file:
```
LINKEDIN_ACCESS_TOKEN=your_access_token_here
```

4. Run the script:
```bash
python main.py
```

## Features
- Uses LinkedIn's official API for reliable data collection
- Searches across 10 major countries
- Generates visualization (results.png)
- Saves raw data (results.csv)

## Output
The script generates:
- results.csv: Raw data with country, position count, and timestamp
- results.png: Bar chart visualization of positions by country

## Note
This project uses LinkedIn's Marketing API which requires approval from LinkedIn. You'll need to:
1. Have a LinkedIn Page
2. Apply for Marketing Developer Platform access
3. Complete LinkedIn's review process

For more information, visit [LinkedIn's Marketing Developer Platform documentation](https://learn.microsoft.com/en-us/linkedin/marketing/)
