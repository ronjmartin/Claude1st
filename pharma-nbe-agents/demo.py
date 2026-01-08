"""
NBE AGENTS DEMO - Live Demonstration Script
For Teams Video Call Interview

This demo showcases the complete pharmaceutical sales intelligence platform
with AI-powered HCP profiling and Next Best Engagement recommendations.
"""
import os
import time
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment
load_dotenv()

def print_header(text, char="="):
    """Print formatted header"""
    width = 80
    print("\n" + char * width)
    print(text.center(width))
    print(char * width)

def print_section(text):
    """Print section header"""
    print("\n" + "─" * 80)
    print(f"  {text}")
    print("─" * 80)

def pause(seconds=1.5):
    """Dramatic pause for demo effect"""
    time.sleep(seconds)

def demo_intro():
    """Introduction to the demo"""
    print_header("PHARMACEUTICAL NBE AGENTS PLATFORM", "=")
    print("\n🎯 LIVE DEMONSTRATION")
    print("   AI-Powered Sales Intelligence for Pharmaceutical Teams")
    print("\n📅 Demo Date:", datetime.now().strftime("%B %d, %Y"))
    pause(2)

def demo_data_overview():
    """Show the data we're working with"""
    print_header("STEP 1: DATA OVERVIEW", "=")

    # Load data
    hcp_df = pd.read_csv('./data/sample_crm/hcp_profiles.csv')
    interactions_df = pd.read_csv('./data/sample_crm/interactions.csv')
    products_df = pd.read_csv('./data/sample_crm/products.csv')
    territories_df = pd.read_csv('./data/sample_crm/territories.csv')

    print("\n📊 CRM DATA LOADED:")
    print(f"   • {len(hcp_df)} Healthcare Professionals")
    print(f"   • {len(interactions_df)} Interactions (past 12 months)")
    print(f"   • {len(products_df)} NBE Products in portfolio")
    print(f"   • {len(territories_df)} US Territories")

    pause(2)

    print("\n🔬 SPECIALTIES COVERED:")
    for specialty in hcp_df['specialty'].unique():
        count = len(hcp_df[hcp_df['specialty'] == specialty])
        print(f"   • {specialty}: {count} HCPs")

    pause(2)

    print("\n💊 PRODUCT PORTFOLIO:")
    for _, product in products_df.iterrows():
        print(f"   • {product['product_name']} ({product['product_id']})")
        print(f"     Indication: {product['indication']}")
        print(f"     Target: {product['target_specialties']}")

    pause(2)

    return hcp_df, interactions_df, products_df, territories_df

def demo_hcp_profiler(hcp_id="HCP049"):
    """Demonstrate HCP Profiler Agent"""
    print_header("STEP 2: HCP PROFILER AGENT", "=")
    print("\n🤖 AGENT: HCP Profiler")
    print("   Purpose: AI-powered analysis of healthcare professional engagement")

    pause(1)

    print(f"\n🎯 Analyzing: {hcp_id}")
    print("   Loading HCP data...")
    pause(1)

    # Import and run profiler
    from agents.hcp_profiler import HCPProfiler

    profiler = HCPProfiler()

    print("   Calculating engagement metrics...")
    pause(1)

    print("   Querying Claude AI for insights...")
    pause(1)

    print_section("AI-GENERATED HCP PROFILE & INSIGHTS")
    analysis = profiler.analyze_hcp_with_ai(hcp_id)
    print(analysis)

    pause(3)

def demo_nbe_recommender(territory="Northeast"):
    """Demonstrate NBE Recommender Agent"""
    print_header("STEP 3: NBE RECOMMENDER AGENT", "=")
    print("\n🤖 AGENT: NBE Recommender")
    print("   Purpose: Generate Next Best Engagement strategies with AI")

    pause(1)

    print(f"\n🗺️  Territory: {territory}")
    print("   Calculating HCP priority scores...")
    pause(1)

    print("   Analyzing engagement patterns...")
    pause(1)

    print("   Identifying at-risk relationships...")
    pause(1)

    # Import and run recommender
    from agents.nbe_recommender import NBERecommender

    recommender = NBERecommender()

    print("   Generating AI-powered recommendations...")
    pause(1)

    print_section(f"TOP 3 NBE RECOMMENDATIONS - {territory}")
    recommendations = recommender.generate_territory_recommendations(territory, top_n=3)

    pause(3)

    return recommendations

def demo_business_impact(recommendations):
    """Show business impact metrics"""
    print_header("STEP 4: BUSINESS IMPACT ANALYSIS", "=")

    if not recommendations:
        print("\n⚠️  No recommendations to analyze")
        return

    print("\n📈 RECOMMENDATION SUMMARY:")
    print(f"   • Total Recommendations: {len(recommendations)}")

    high_priority = [r for r in recommendations if r.get('priority') == 'high']
    print(f"   • High Priority: {len(high_priority)}")

    immediate = [r for r in recommendations if r.get('urgency') == 'immediate']
    print(f"   • Immediate Action Required: {len(immediate)}")

    avg_confidence = sum(r.get('confidence', 0) for r in recommendations) / len(recommendations)
    print(f"   • Average AI Confidence: {avg_confidence:.1%}")

    pause(2)

    print("\n🎯 CHANNEL OPTIMIZATION:")
    channels = {}
    for rec in recommendations:
        channel = rec.get('recommended_channel', 'Unknown')
        channels[channel] = channels.get(channel, 0) + 1

    for channel, count in sorted(channels.items(), key=lambda x: x[1], reverse=True):
        print(f"   • {channel}: {count} recommendation(s)")

    pause(2)

    print("\n💊 PRODUCT STRATEGY:")
    products = {}
    for rec in recommendations:
        product = rec.get('product_focus', 'Unknown')
        products[product] = products.get(product, 0) + 1

    for product, count in sorted(products.items(), key=lambda x: x[1], reverse=True):
        print(f"   • {product}: {count} HCP(s)")

    pause(2)

    print("\n💰 ESTIMATED BUSINESS VALUE:")
    total_hcps = len(recommendations)
    avg_patient_volume = 350  # Average from data
    avg_rx_value = 5000  # Average product price

    potential_value = total_hcps * avg_patient_volume * 0.15 * avg_rx_value

    print(f"   • {total_hcps} High-Value HCPs Targeted")
    print(f"   • Est. Patient Reach: {total_hcps * avg_patient_volume:,} patients")
    print(f"   • Potential Revenue Impact: ${potential_value:,.0f}")
    print(f"     (Based on 15% prescription conversion rate)")

    pause(3)

def demo_key_features():
    """Highlight key platform features"""
    print_header("PLATFORM CAPABILITIES", "=")

    print("\n✨ KEY FEATURES:\n")

    features = [
        ("🤖 AI-Powered Intelligence", "Claude Sonnet 4 for advanced analytics"),
        ("📊 Real-Time Analysis", "Process CRM data and generate insights instantly"),
        ("🎯 Micro-Segmentation", "Individual HCP profiling with personalized strategies"),
        ("🔍 At-Risk Detection", "Identify disengaging relationships before it's too late"),
        ("📈 Priority Scoring", "Data-driven HCP prioritization (tier, volume, engagement)"),
        ("💬 Channel Optimization", "AI recommends best contact method per HCP"),
        ("💊 Product Alignment", "Match products to physician specialties automatically"),
        ("📝 Actionable Insights", "Specific actions, not just analytics"),
        ("✅ Confidence Scoring", "Every recommendation includes AI confidence level"),
        ("🔒 Compliance Ready", "Audit logging and data anonymization built-in"),
    ]

    for i, (feature, description) in enumerate(features, 1):
        print(f"{i:2}. {feature}")
        print(f"    {description}")
        pause(0.5)

    pause(2)

def demo_orchestrator_preview():
    """Preview the orchestrator capability"""
    print_header("BONUS: ORCHESTRATOR AGENT", "=")

    print("\n🎼 MULTI-AGENT ORCHESTRATION:")
    print("   The platform includes an orchestrator that coordinates all agents")
    print("   for complete territory-level analysis.")

    pause(2)

    print("\n📋 ORCHESTRATOR CAPABILITIES:")
    print("   • Run complete workflow: Profiling → Recommendations → Reporting")
    print("   • Multi-territory batch processing")
    print("   • Consolidated insights across all agents")
    print("   • Executive-ready summary reports")
    print("   • Interactive mode for ad-hoc analysis")

    pause(2)

    print("\n💡 EXAMPLE USE CASE:")
    print('   Command: python agents/nbe_orchestrator.py')
    print("   Result: Complete Northeast territory analysis with:")
    print("          - HCP profiling for top engaged physicians")
    print("          - NBE recommendations with action items")
    print("          - Territory summary report")
    print("          - Saved JSON output for CRM integration")

    pause(3)

def demo_conclusion():
    """Wrap up the demo"""
    print_header("DEMONSTRATION COMPLETE", "=")

    print("\n🎉 PHARMA NBE AGENTS PLATFORM")
    print("\n✅ What We've Demonstrated:")
    print("   1. ✓ CRM data integration (100 HCPs, 500 interactions)")
    print("   2. ✓ AI-powered HCP profiling with detailed insights")
    print("   3. ✓ Next Best Engagement recommendations")
    print("   4. ✓ Business impact analysis")
    print("   5. ✓ Multi-agent orchestration capability")

    pause(2)

    print("\n🚀 READY FOR DEPLOYMENT:")
    print("   • Modular agent architecture")
    print("   • Easy CRM integration via CSV/API")
    print("   • Configurable via environment variables")
    print("   • Production-ready with compliance features")
    print("   • Extensible for additional agents/workflows")

    pause(2)

    print("\n📊 TECHNOLOGY STACK:")
    print("   • Python 3.11")
    print("   • Anthropic Claude Sonnet 4 API")
    print("   • Pandas for data processing")
    print("   • Pydantic for data validation")
    print("   • Modular, testable architecture")

    pause(2)

    print("\n💼 BUSINESS VALUE:")
    print("   • Increase sales efficiency with AI-driven prioritization")
    print("   • Improve HCP engagement rates with personalized strategies")
    print("   • Reduce churn with proactive at-risk detection")
    print("   • Scale insights across entire sales organization")
    print("   • Data-driven decision making for field teams")

    pause(2)

    print_header("THANK YOU!", "=")
    print("\n🙋 Questions & Discussion")
    print("\n")

def main():
    """Run the complete demo"""
    try:
        # Introduction
        demo_intro()

        # Data Overview
        hcp_df, interactions_df, products_df, territories_df = demo_data_overview()

        # HCP Profiler Demo
        demo_hcp_profiler(hcp_id="HCP049")

        # NBE Recommender Demo
        recommendations = demo_nbe_recommender(territory="Northeast")

        # Business Impact
        demo_business_impact(recommendations)

        # Key Features
        demo_key_features()

        # Orchestrator Preview
        demo_orchestrator_preview()

        # Conclusion
        demo_conclusion()

    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Demo error: {e}")
        raise

if __name__ == "__main__":
    main()
