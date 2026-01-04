"""
HCP Profiler Agent - Analyzes Healthcare Professional engagement and creates profiles
"""
import os
import pandas as pd
from anthropic import Anthropic
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

class HCPProfiler:
    """Agent that analyzes HCP data and generates insights"""

    def __init__(self):
        self.api_key = os.getenv('ANTHROPIC_API_KEY')
        self.client = Anthropic(api_key=self.api_key)
        self.model = os.getenv('NBE_MODEL', 'claude-sonnet-4-20250514')

        # Load data
        self.hcp_df = pd.read_csv(os.getenv('HCP_DATA_PATH'))
        self.interactions_df = pd.read_csv(os.getenv('INTERACTION_DATA_PATH'))
        self.products_df = pd.read_csv(os.getenv('PRODUCT_DATA_PATH'))

        print(f"✅ HCP Profiler initialized")
        print(f"   - Loaded {len(self.hcp_df)} HCP profiles")
        print(f"   - Loaded {len(self.interactions_df)} interactions")
        print(f"   - Loaded {len(self.products_df)} products")

    def get_hcp_engagement_metrics(self, hcp_id):
        """Calculate engagement metrics for a specific HCP"""
        hcp_interactions = self.interactions_df[
            self.interactions_df['hcp_id'] == hcp_id
        ]

        if len(hcp_interactions) == 0:
            return None

        metrics = {
            'total_interactions': len(hcp_interactions),
            'avg_sentiment': hcp_interactions['sentiment_score'].mean(),
            'last_interaction': hcp_interactions['date'].max(),
            'preferred_products': hcp_interactions['product_id'].value_counts().to_dict(),
            'interaction_types': hcp_interactions['interaction_type'].value_counts().to_dict(),
            'positive_outcomes': len(hcp_interactions[
                hcp_interactions['outcome'] == 'Positive'
            ]),
            'samples_received': hcp_interactions['samples_provided'].sum()
        }

        return metrics

    def analyze_hcp_with_ai(self, hcp_id):
        """Use Claude to analyze HCP profile and generate insights"""
        # Get HCP data
        hcp = self.hcp_df[self.hcp_df['hcp_id'] == hcp_id].iloc[0]
        metrics = self.get_hcp_engagement_metrics(hcp_id)

        if metrics is None:
            return f"No interaction data available for {hcp_id}"

        # Prepare context for Claude
        prompt = f"""You are a pharmaceutical sales analytics expert. Analyze this Healthcare Professional's profile and engagement data:

HCP Profile:
- ID: {hcp['hcp_id']}
- Name: {hcp['name']}
- Specialty: {hcp['specialty']}
- Practice Type: {hcp['practice_type']}
- Territory: {hcp['territory']}
- Patient Volume: {hcp['patient_volume']} patients
- Years in Practice: {hcp['years_in_practice']}
- Academic Affiliation: {hcp['academic_affiliation']}
- Tier: {hcp['tier']}

Engagement Metrics:
- Total Interactions: {metrics['total_interactions']}
- Average Sentiment Score: {metrics['avg_sentiment']:.2f} (0-1 scale)
- Last Interaction: {metrics['last_interaction']}
- Positive Outcomes: {metrics['positive_outcomes']} out of {metrics['total_interactions']}
- Samples Received: {metrics['samples_received']}
- Preferred Products: {metrics['preferred_products']}
- Interaction Types: {metrics['interaction_types']}

Available Products:
{self.products_df.to_string()}

Please provide:
1. A brief profile summary
2. Engagement assessment (high/medium/low and why)
3. Top 3 actionable recommendations for the sales team
4. Which products to focus on and why

Keep your response concise and actionable."""

        # Call Claude API
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        return message.content[0].text

    def profile_top_hcps(self, n=5):
        """Profile the top N HCPs by interaction count"""
        # Get interaction counts per HCP
        interaction_counts = self.interactions_df['hcp_id'].value_counts()
        top_hcps = interaction_counts.head(n).index.tolist()

        print(f"\n{'='*70}")
        print(f"TOP {n} HCPs BY ENGAGEMENT")
        print(f"{'='*70}\n")

        for i, hcp_id in enumerate(top_hcps, 1):
            print(f"\n{'─'*70}")
            print(f"PROFILE {i}: {hcp_id}")
            print(f"{'─'*70}")

            analysis = self.analyze_hcp_with_ai(hcp_id)
            print(analysis)
            print()

        return top_hcps

    def generate_territory_summary(self, territory):
        """Generate summary for a specific territory"""
        territory_hcps = self.hcp_df[self.hcp_df['territory'] == territory]

        print(f"\n{'='*70}")
        print(f"TERRITORY SUMMARY: {territory}")
        print(f"{'='*70}")
        print(f"Total HCPs: {len(territory_hcps)}")
        print(f"Specialty Breakdown:")
        print(territory_hcps['specialty'].value_counts())
        print(f"\nTier Distribution:")
        print(territory_hcps['tier'].value_counts())

        return territory_hcps

def main():
    """Main execution"""
    print("\n" + "="*70)
    print("HCP PROFILER AGENT - Pharmaceutical Sales Intelligence")
    print("="*70)

    # Initialize profiler
    profiler = HCPProfiler()

    # Profile top 3 HCPs
    print("\nAnalyzing top engaged HCPs...")
    profiler.profile_top_hcps(n=3)

    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)

if __name__ == "__main__":
    main()
