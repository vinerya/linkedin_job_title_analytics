import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
from dotenv import load_dotenv

class LinkedInAPIAnalyzer:
    def __init__(self):
        load_dotenv()
        self.access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')
        self.base_url = 'https://api.linkedin.com/v2'
        self.results = []
        self.countries = [
            "United States",
            "United Kingdom",
            "Germany",
            "France",
            "Netherlands",
            "Sweden",
            "Singapore",
            "Australia",
            "Canada",
            "India"
        ]
        
        # Map countries to ISO 3166-1 alpha-2 codes (required by LinkedIn API)
        self.country_codes = {
            "United States": "US",
            "United Kingdom": "GB",
            "Germany": "DE",
            "France": "FR",
            "Netherlands": "NL",
            "Sweden": "SE",
            "Singapore": "SG",
            "Australia": "AU",
            "Canada": "CA",
            "India": "IN"
        }

    def get_headers(self):
        """Get headers for API requests"""
        return {
            'Authorization': f'Bearer {self.access_token}',
            'X-Restli-Protocol-Version': '2.0.0',
            'Content-Type': 'application/json'
        }

    def search_jobs(self, country_code):
        """Search for "Target Job Title" positions using LinkedIn's Job Search API"""
        endpoint = f"{self.base_url}/jobSearch"
        
        params = {
            'keywords': 'Innovation Manager', # as example
            'locationCode': country_code,
            'count': 1  # We only need the count, not actual listings
        }
        
        try:
            response = requests.get(
                endpoint,
                headers=self.get_headers(),
                params=params
            )
            response.raise_for_status()
            data = response.json()
            
            # Extract total number of results
            total_count = data.get('paging', {}).get('total', 0)
            return total_count
            
        except requests.exceptions.RequestException as e:
            print(f"Error searching jobs for {country_code}: {str(e)}")
            return 0

    def collect_data(self):
        """Collect data for all countries"""
        for country in self.countries:
            country_code = self.country_codes[country]
            count = self.search_jobs(country_code)
            
            self.results.append({
                'country': country,
                'count': count,
                'timestamp': datetime.now()
            })

    def analyze_data(self):
        """Analyze and visualize the collected data"""
        df = pd.DataFrame(self.results)
        
        # Create visualization
        plt.figure(figsize=(12, 6))
        bars = plt.bar(df['country'], df['count'])
        plt.xticks(rotation=45, ha='right')
        plt.title('Innovation Manager Positions by Country')
        plt.xlabel('Country')
        plt.ylabel('Number of Positions')
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height):,}',
                    ha='center', va='bottom')
        
        plt.tight_layout()
        plt.savefig('results.png')
        
        # Save to CSV
        df.to_csv('results.csv', index=False)
        
        return df

    def run(self):
        """Main execution method"""
        self.collect_data()
        return self.analyze_data()

if __name__ == "__main__":
    analyzer = LinkedInAPIAnalyzer()
    results_df = analyzer.run()
    print("\nResults saved to results.csv and results.png")
    print("\nSummary of findings:")
    print(results_df.to_string(index=False))
