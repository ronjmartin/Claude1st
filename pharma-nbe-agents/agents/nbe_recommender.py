"""
NBE Recommender Agent - Next Best Engagement recommendations for HCPs
Suggests optimal engagement strategies, timing, and product focus
"""
import os
import pandas as pd
from anthropic import Anthropic
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json

# Load environment variables
load_dotenv()

class NBERecommender:
    """Agent that generates Next Best Engagement recommendations"""

    def __init__(self):
        self.api_key = os.getenv('ANTHROPIC_API_KEY')
        self.client = Anthropic(api_key=self.api_key)
        self.model = os.getenv('NBE_MODEL', 'claude-sonnet-4-20250514')
        self.max_recommendations = int(os.getenv('MAX_RECOMMENDATIONS_PER_HCP', 3))
        self.confidence_threshold = float(os.getenv('CONFIDENCE_THRESHOLD', 0.7))

        # Load data
        self.hcp_df = pd.read_csv(os.getenv('HCP_DATA_PATH'))
        self.interactions_df = pd.read_csv(os.getenv('INTERACTION_DATA_PATH'))
        self.products_df = pd.read_csv(os.getenv('PRODUCT_DATA_PATH'))
        self.territories_df = pd.read_csv(os.getenv('TERRITORY_DATA_PATH'))

        # Convert dates
        self.interactions_df['date'] = pd.to_datetime(self.interactions_df['date'])

        print(f"✅ NBE Recommender initialized")
        print(f"   - Model: {self.model}")
        print(f"   - Max recommendations per HCP: {self.max_recommendations}")
        print(f"   - Confidence threshold: {self.confidence_threshold}")

    def calculate_hcp_score(self, hcp_id):
        """Calculate priority score for an HCP"""
        hcp = self.hcp_df[self.hcp_df['hcp_id'] == hcp_id].iloc[0]
        hcp_interactions = self.interactions_df[
            self.interactions_df['hcp_id'] == hcp_id
        ]

        # Base score from tier
        tier_scores = {'A': 100, 'B': 60, 'C': 30}
        score = tier_scores.get(hcp['tier'], 50)

        # Add points for patient volume
        score += min(hcp['patient_volume'] / 10, 50)

        # Add points for recent engagement
        if len(hcp_interactions) > 0:
            last_interaction = hcp_interactions['date'].max()
            days_since = (datetime.now() - last_interaction).days
            recency_score = max(0, 30 - (days_since / 10))
            score += recency_score

            # Add points for positive sentiment
            avg_sentiment = hcp_interactions['sentiment_score'].mean()
            score += avg_sentiment * 20

        # Academic affiliation bonus
        if hcp['academic_affiliation']:
            score += 15

        return round(score, 2)

    def get_engagement_insights(self, hcp_id):
        """Get detailed engagement insights for an HCP"""
        hcp = self.hcp_df[self.hcp_df['hcp_id'] == hcp_id].iloc[0]
        hcp_interactions = self.interactions_df[
            self.interactions_df['hcp_id'] == hcp_id
        ]

        if len(hcp_interactions) == 0:
            return {
                'status': 'no_engagement',
                'priority': 'high' if hcp['tier'] == 'A' else 'medium',
                'recommended_action': 'initial_outreach'
            }

        # Calculate insights
        last_interaction = hcp_interactions['date'].max()
        days_since = (datetime.now() - last_interaction).days
        avg_sentiment = hcp_interactions['sentiment_score'].mean()
        positive_rate = len(hcp_interactions[
            hcp_interactions['outcome'] == 'Positive'
        ]) / len(hcp_interactions)

        # Determine engagement status
        if days_since > 90:
            status = 'at_risk'
        elif days_since > 30:
            status = 'cooling'
        else:
            status = 'active'

        return {
            'status': status,
            'days_since_last': days_since,
            'avg_sentiment': round(avg_sentiment, 2),
            'positive_rate': round(positive_rate, 2),
            'total_interactions': len(hcp_interactions),
            'preferred_channel': hcp_interactions['interaction_type'].mode()[0],
            'top_product': hcp_interactions['product_id'].mode()[0] if len(hcp_interactions) > 0 else None
        }

    def generate_nbe_recommendation(self, hcp_id):
        """Generate AI-powered NBE recommendation for an HCP"""
        hcp = self.hcp_df[self.hcp_df['hcp_id'] == hcp_id].iloc[0]
        insights = self.get_engagement_insights(hcp_id)
        score = self.calculate_hcp_score(hcp_id)

        # Get relevant products for specialty
        relevant_products = self.products_df[
            self.products_df['target_specialties'].str.contains(
                hcp['specialty'],
                case=False,
                na=False
            )
        ]

        prompt = f"""You are a pharmaceutical sales strategy AI. Generate the Next Best Engagement recommendation for this HCP.

HCP Profile:
- ID: {hcp['hcp_id']}
- Specialty: {hcp['specialty']}
- Practice: {hcp['practice_type']}
- Territory: {hcp['territory']}
- Tier: {hcp['tier']}
- Patient Volume: {hcp['patient_volume']}
- Preferred Contact: {hcp['preferred_contact_method']}

Engagement Insights:
- Status: {insights['status']}
- Days Since Last Contact: {insights.get('days_since_last', 'N/A')}
- Average Sentiment: {insights.get('avg_sentiment', 'N/A')}
- Positive Outcome Rate: {insights.get('positive_rate', 'N/A')}
- Preferred Channel: {insights.get('preferred_channel', 'Unknown')}
- Priority Score: {score}

Relevant Products:
{relevant_products[['product_id', 'product_name', 'indication']].to_string() if len(relevant_products) > 0 else 'None matching specialty'}

Generate a JSON response with these exact fields:
{{
  "priority": "high|medium|low",
  "urgency": "immediate|this_week|this_month",
  "recommended_action": "brief action description",
  "recommended_channel": "Email|Phone|In-Person|Virtual Meeting",
  "product_focus": "product_id or 'multiple'",
  "key_message": "concise value proposition",
  "rationale": "why this recommendation",
  "confidence": 0.0-1.0
}}

Be specific and actionable. Consider the HCP's preferences and engagement history."""

        # Call Claude API
        message = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        # Parse JSON response
        try:
            response_text = message.content[0].text
            # Extract JSON from response (handle markdown code blocks)
            if '```json' in response_text:
                json_str = response_text.split('```json')[1].split('```')[0].strip()
            elif '```' in response_text:
                json_str = response_text.split('```')[1].split('```')[0].strip()
            else:
                json_str = response_text.strip()

            recommendation = json.loads(json_str)
            recommendation['hcp_id'] = hcp_id
            recommendation['hcp_name'] = hcp['name']
            recommendation['specialty'] = hcp['specialty']
            recommendation['priority_score'] = score

            return recommendation
        except Exception as e:
            print(f"Error parsing recommendation for {hcp_id}: {e}")
            return None

    def generate_territory_recommendations(self, territory, top_n=5):
        """Generate NBE recommendations for top HCPs in a territory"""
        territory_hcps = self.hcp_df[self.hcp_df['territory'] == territory]

        print(f"\n{'='*70}")
        print(f"NBE RECOMMENDATIONS - {territory} Territory")
        print(f"{'='*70}")
        print(f"Total HCPs in territory: {len(territory_hcps)}")

        # Calculate scores and prioritize
        hcp_scores = []
        for hcp_id in territory_hcps['hcp_id']:
            score = self.calculate_hcp_score(hcp_id)
            hcp_scores.append((hcp_id, score))

        # Sort by score and get top N
        hcp_scores.sort(key=lambda x: x[1], reverse=True)
        top_hcps = [hcp_id for hcp_id, score in hcp_scores[:top_n]]

        recommendations = []
        for i, hcp_id in enumerate(top_hcps, 1):
            print(f"\n{'─'*70}")
            print(f"RECOMMENDATION {i}")
            print(f"{'─'*70}")

            rec = self.generate_nbe_recommendation(hcp_id)
            if rec and rec.get('confidence', 0) >= self.confidence_threshold:
                recommendations.append(rec)
                self.display_recommendation(rec)
            else:
                print(f"⚠️  Low confidence recommendation for {hcp_id} (skipped)")

        return recommendations

    def display_recommendation(self, rec):
        """Display a recommendation in a formatted way"""
        print(f"\n🎯 HCP: {rec['hcp_name']} ({rec['hcp_id']})")
        print(f"   Specialty: {rec['specialty']}")
        print(f"   Priority Score: {rec['priority_score']}")
        print(f"\n📊 Recommendation:")
        print(f"   Priority: {rec['priority'].upper()}")
        print(f"   Urgency: {rec['urgency'].replace('_', ' ').title()}")
        print(f"   Channel: {rec['recommended_channel']}")
        print(f"   Product Focus: {rec['product_focus']}")
        print(f"\n💡 Action: {rec['recommended_action']}")
        print(f"\n📝 Key Message: {rec['key_message']}")
        print(f"\n🔍 Rationale: {rec['rationale']}")
        print(f"\n✅ Confidence: {rec['confidence']}")

    def save_recommendations(self, recommendations, filename='nbe_recommendations.json'):
        """Save recommendations to file"""
        # Get the project root directory (parent of agents directory)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        output_dir = os.path.join(project_root, 'outputs', 'recommendations')

        # Create directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'w') as f:
            json.dump(recommendations, f, indent=2)
        print(f"\n💾 Recommendations saved to: {output_path}")

def main():
    """Main execution"""
    print("\n" + "="*70)
    print("NBE RECOMMENDER - Next Best Engagement Intelligence")
    print("="*70)

    # Initialize recommender
    recommender = NBERecommender()

    # Generate recommendations for a sample territory
    territory = 'Northeast'
    print(f"\nGenerating top 5 NBE recommendations for {territory}...")

    recommendations = recommender.generate_territory_recommendations(territory, top_n=5)

    # Save to file
    if recommendations:
        recommender.save_recommendations(
            recommendations,
            f'nbe_{territory.lower()}_{datetime.now().strftime("%Y%m%d")}.json'
        )

    print("\n" + "="*70)
    print(f"GENERATED {len(recommendations)} NBE RECOMMENDATIONS")
    print("="*70)

if __name__ == "__main__":
    main()
