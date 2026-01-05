"""
NBE Orchestrator - Coordinates all pharma agents for comprehensive insights
Runs HCP profiling and NBE recommendations in an integrated workflow
"""
import os
import sys
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Import other agents
from hcp_profiler import HCPProfiler
from nbe_recommender import NBERecommender

class NBEOrchestrator:
    """Orchestrates all pharma NBE agents for comprehensive analysis"""

    def __init__(self):
        print("\n" + "="*70)
        print("NBE ORCHESTRATOR - Pharmaceutical Sales Intelligence Platform")
        print("="*70)
        print("\nInitializing agents...")

        # Initialize agents
        self.profiler = HCPProfiler()
        self.recommender = NBERecommender()

        # Load data for overview
        self.hcp_df = pd.read_csv(os.getenv('HCP_DATA_PATH'))
        self.interactions_df = pd.read_csv(os.getenv('INTERACTION_DATA_PATH'))
        self.products_df = pd.read_csv(os.getenv('PRODUCT_DATA_PATH'))
        self.territories_df = pd.read_csv(os.getenv('TERRITORY_DATA_PATH'))

        print("\n✅ All agents initialized successfully")
        self.display_data_summary()

    def display_data_summary(self):
        """Display summary of available data"""
        print("\n" + "─"*70)
        print("DATA SUMMARY")
        print("─"*70)
        print(f"HCPs: {len(self.hcp_df)}")
        print(f"Interactions: {len(self.interactions_df)}")
        print(f"Products: {len(self.products_df)}")
        print(f"Territories: {len(self.territories_df)}")
        print(f"\nSpecialties: {', '.join(self.hcp_df['specialty'].unique())}")
        print(f"Territories: {', '.join(self.hcp_df['territory'].unique())}")

    def run_territory_analysis(self, territory, top_n=5):
        """Complete territory analysis with profiling and recommendations"""
        print("\n" + "="*70)
        print(f"COMPLETE TERRITORY ANALYSIS: {territory}")
        print("="*70)

        # Get territory HCPs
        territory_hcps = self.hcp_df[self.hcp_df['territory'] == territory]
        print(f"\nTerritory Overview:")
        print(f"  Total HCPs: {len(territory_hcps)}")
        print(f"  Tier A: {len(territory_hcps[territory_hcps['tier'] == 'A'])}")
        print(f"  Tier B: {len(territory_hcps[territory_hcps['tier'] == 'B'])}")
        print(f"  Tier C: {len(territory_hcps[territory_hcps['tier'] == 'C'])}")

        # Specialty breakdown
        print(f"\n  Specialty Distribution:")
        for specialty, count in territory_hcps['specialty'].value_counts().items():
            print(f"    {specialty}: {count}")

        # Step 1: Profile top HCPs
        print("\n" + "─"*70)
        print("STEP 1: HCP PROFILING & ANALYSIS")
        print("─"*70)

        # Get interaction counts for territory
        territory_hcp_ids = territory_hcps['hcp_id'].tolist()
        territory_interactions = self.interactions_df[
            self.interactions_df['hcp_id'].isin(territory_hcp_ids)
        ]
        interaction_counts = territory_interactions['hcp_id'].value_counts()
        top_engaged_hcps = interaction_counts.head(min(3, top_n)).index.tolist()

        print(f"\nAnalyzing top {len(top_engaged_hcps)} most engaged HCPs...\n")

        for i, hcp_id in enumerate(top_engaged_hcps, 1):
            print(f"{'─'*70}")
            print(f"HCP {i}/{len(top_engaged_hcps)}: {hcp_id}")
            print(f"{'─'*70}")
            analysis = self.profiler.analyze_hcp_with_ai(hcp_id)
            print(analysis)
            print()

        # Step 2: Generate NBE Recommendations
        print("\n" + "─"*70)
        print("STEP 2: NEXT BEST ENGAGEMENT RECOMMENDATIONS")
        print("─"*70)

        recommendations = self.recommender.generate_territory_recommendations(
            territory,
            top_n=top_n
        )

        # Step 3: Generate Summary Report
        self.generate_territory_report(territory, recommendations)

        return recommendations

    def generate_territory_report(self, territory, recommendations):
        """Generate comprehensive territory report"""
        print("\n" + "="*70)
        print(f"TERRITORY REPORT SUMMARY: {territory}")
        print("="*70)

        if not recommendations:
            print("\nNo recommendations generated.")
            return

        # Aggregate insights
        high_priority = [r for r in recommendations if r.get('priority') == 'high']
        immediate_urgency = [r for r in recommendations if r.get('urgency') == 'immediate']

        print(f"\nTotal Recommendations: {len(recommendations)}")
        print(f"High Priority: {len(high_priority)}")
        print(f"Immediate Urgency: {len(immediate_urgency)}")

        # Channel breakdown
        channels = {}
        for rec in recommendations:
            channel = rec.get('recommended_channel', 'Unknown')
            channels[channel] = channels.get(channel, 0) + 1

        print(f"\nRecommended Channels:")
        for channel, count in sorted(channels.items(), key=lambda x: x[1], reverse=True):
            print(f"  {channel}: {count}")

        # Product focus breakdown
        products = {}
        for rec in recommendations:
            product = rec.get('product_focus', 'Unknown')
            products[product] = products.get(product, 0) + 1

        print(f"\nProduct Focus:")
        for product, count in sorted(products.items(), key=lambda x: x[1], reverse=True):
            print(f"  {product}: {count}")

        # Average confidence
        avg_confidence = sum(r.get('confidence', 0) for r in recommendations) / len(recommendations)
        print(f"\nAverage Confidence: {avg_confidence:.2%}")

        # Action items
        print(f"\n" + "─"*70)
        print("KEY ACTION ITEMS")
        print("─"*70)

        for i, rec in enumerate(immediate_urgency[:3], 1):
            print(f"\n{i}. {rec['hcp_name']} ({rec['specialty']})")
            print(f"   Action: {rec['recommended_action']}")
            print(f"   Channel: {rec['recommended_channel']}")
            print(f"   Priority Score: {rec['priority_score']}")

    def run_full_analysis(self, territories=None, top_n_per_territory=5):
        """Run analysis across multiple territories"""
        if territories is None:
            territories = self.hcp_df['territory'].unique().tolist()

        print("\n" + "="*70)
        print("FULL MULTI-TERRITORY ANALYSIS")
        print("="*70)
        print(f"Analyzing {len(territories)} territories: {', '.join(territories)}")

        all_recommendations = []

        for territory in territories:
            recs = self.run_territory_analysis(territory, top_n=top_n_per_territory)
            all_recommendations.extend(recs)

            print("\n" + "="*70)
            print()

        # Save consolidated recommendations
        self.save_consolidated_report(all_recommendations, territories)

        return all_recommendations

    def save_consolidated_report(self, recommendations, territories):
        """Save consolidated recommendations across territories"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        output_dir = os.path.join(project_root, 'outputs', 'recommendations')
        os.makedirs(output_dir, exist_ok=True)

        filename = f"consolidated_recommendations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        output_path = os.path.join(output_dir, filename)

        report = {
            'generated_at': datetime.now().isoformat(),
            'territories_analyzed': territories,
            'total_recommendations': len(recommendations),
            'recommendations': recommendations
        }

        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"\n💾 Consolidated report saved to: {output_path}")

    def interactive_menu(self):
        """Interactive menu for orchestrator"""
        while True:
            print("\n" + "="*70)
            print("NBE ORCHESTRATOR - MENU")
            print("="*70)
            print("\n1. Analyze single territory")
            print("2. Analyze all territories")
            print("3. Profile specific HCP")
            print("4. Generate NBE recommendations for territory")
            print("5. Exit")

            choice = input("\nSelect option (1-5): ").strip()

            if choice == '1':
                print("\nAvailable territories:", ', '.join(self.hcp_df['territory'].unique()))
                territory = input("Enter territory name: ").strip()
                if territory in self.hcp_df['territory'].unique():
                    self.run_territory_analysis(territory, top_n=5)
                else:
                    print("❌ Invalid territory")

            elif choice == '2':
                self.run_full_analysis(top_n_per_territory=3)

            elif choice == '3':
                hcp_id = input("Enter HCP ID (e.g., HCP001): ").strip()
                if hcp_id in self.hcp_df['hcp_id'].values:
                    analysis = self.profiler.analyze_hcp_with_ai(hcp_id)
                    print("\n" + "─"*70)
                    print(analysis)
                else:
                    print("❌ Invalid HCP ID")

            elif choice == '4':
                print("\nAvailable territories:", ', '.join(self.hcp_df['territory'].unique()))
                territory = input("Enter territory name: ").strip()
                if territory in self.hcp_df['territory'].unique():
                    recs = self.recommender.generate_territory_recommendations(territory, top_n=5)
                    print(f"\n✅ Generated {len(recs)} recommendations")
                else:
                    print("❌ Invalid territory")

            elif choice == '5':
                print("\n👋 Exiting NBE Orchestrator. Goodbye!")
                break

            else:
                print("❌ Invalid option. Please select 1-5.")

def main():
    """Main execution"""
    orchestrator = NBEOrchestrator()

    # Default: Run analysis for one territory
    print("\n" + "="*70)
    print("RUNNING SAMPLE ANALYSIS - Northeast Territory")
    print("="*70)

    orchestrator.run_territory_analysis('Northeast', top_n=3)

    print("\n" + "="*70)
    print("ORCHESTRATOR SAMPLE RUN COMPLETE")
    print("="*70)
    print("\nFor interactive mode, uncomment orchestrator.interactive_menu() in main()")

    # Uncomment for interactive mode:
    # orchestrator.interactive_menu()

if __name__ == "__main__":
    main()
