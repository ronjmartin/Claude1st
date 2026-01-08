#!/usr/bin/env python3
"""
Executive Deck Generator for NBE Agents Platform
Creates a professional 10-slide presentation for interview demonstrations
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_executive_deck():
    """Create a professional 10-slide executive presentation"""

    # Create presentation
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Define colors
    BLUE = RGBColor(0, 102, 204)
    DARK_BLUE = RGBColor(0, 51, 102)
    GRAY = RGBColor(89, 89, 89)
    LIGHT_GRAY = RGBColor(217, 217, 217)
    GREEN = RGBColor(34, 139, 34)

    # SLIDE 1: Title Slide
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout

    # Add title
    title_box = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(8), Inches(1))
    title_frame = title_box.text_frame
    title_frame.text = "Pharmaceutical NBE Agents Platform"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(44)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE
    title_para.alignment = PP_ALIGN.CENTER

    # Add subtitle
    subtitle_box = slide.shapes.add_textbox(Inches(1), Inches(3.7), Inches(8), Inches(0.8))
    subtitle_frame = subtitle_box.text_frame
    subtitle_frame.text = "AI-Powered Sales Intelligence for Pharmaceutical Field Teams"
    subtitle_para = subtitle_frame.paragraphs[0]
    subtitle_para.font.size = Pt(24)
    subtitle_para.font.color.rgb = BLUE
    subtitle_para.alignment = PP_ALIGN.CENTER

    # Add tagline
    tagline_box = slide.shapes.add_textbox(Inches(1), Inches(5), Inches(8), Inches(0.6))
    tagline_frame = tagline_box.text_frame
    tagline_frame.text = "Turn CRM Data Into Actionable Engagement Strategies"
    tagline_para = tagline_frame.paragraphs[0]
    tagline_para.font.size = Pt(18)
    tagline_para.font.italic = True
    tagline_para.font.color.rgb = GRAY
    tagline_para.alignment = PP_ALIGN.CENTER

    # SLIDE 2: The Challenge
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "The Challenge"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(40)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE

    # Add challenges
    content_box = slide.shapes.add_textbox(Inches(1), Inches(1.8), Inches(8), Inches(5))
    text_frame = content_box.text_frame
    text_frame.word_wrap = True

    challenges = [
        "Pharmaceutical reps manage 100+ HCP relationships with limited face time",
        "Traditional CRM systems provide data, not actionable insights",
        "Difficult to identify at-risk relationships before they disengage",
        "No personalized guidance on when, how, and what to discuss",
        "Sales teams need prioritization, not just scores",
        "Compliance requirements limit marketing flexibility"
    ]

    for i, challenge in enumerate(challenges):
        p = text_frame.add_paragraph() if i > 0 else text_frame.paragraphs[0]
        p.text = "• " + challenge
        p.font.size = Pt(22)
        p.font.color.rgb = GRAY
        p.space_after = Pt(20)
        p.level = 0

    # SLIDE 3: The Solution
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "The Solution: AI Agents That Understand Your Territory"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(36)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE

    # Add solution description
    content_box = slide.shapes.add_textbox(Inches(1), Inches(1.8), Inches(8), Inches(5.2))
    text_frame = content_box.text_frame
    text_frame.word_wrap = True

    p = text_frame.paragraphs[0]
    p.text = "Like having a sales strategist analyze every physician relationship"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = BLUE
    p.space_after = Pt(30)

    solutions = [
        "HCP Profiler Agent: Analyzes individual physician engagement patterns and preferences",
        "NBE Recommender Agent: Generates Next Best Engagement strategies with channel optimization",
        "Orchestrator Agent: Coordinates multi-agent workflows for complete territory intelligence",
        "Built on Claude Sonnet 4 for advanced medical and business reasoning",
        "Transforms 'HCP001 has a score of 87' into 'Call Dr. Smith this week about Neuro-Delta, leading with new efficacy data'"
    ]

    for solution in solutions:
        p = text_frame.add_paragraph()
        p.text = "✓ " + solution
        p.font.size = Pt(18)
        p.font.color.rgb = GRAY
        p.space_after = Pt(18)
        p.level = 0

    # SLIDE 4: How It Works - Architecture
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "How It Works: Multi-Agent Architecture"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(36)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE

    # Create three agent boxes
    # HCP Profiler
    agent1_box = slide.shapes.add_textbox(Inches(0.8), Inches(2), Inches(2.5), Inches(3.5))
    agent1_frame = agent1_box.text_frame
    agent1_frame.word_wrap = True
    p = agent1_frame.paragraphs[0]
    p.text = "HCP Profiler"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = BLUE
    p = agent1_frame.add_paragraph()
    p.text = "\n• Analyzes engagement patterns\n• Calculates sentiment scores\n• Identifies preferences\n• Generates insights\n• Product-specialty matching"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY

    # NBE Recommender
    agent2_box = slide.shapes.add_textbox(Inches(3.7), Inches(2), Inches(2.5), Inches(3.5))
    agent2_frame = agent2_box.text_frame
    agent2_frame.word_wrap = True
    p = agent2_frame.paragraphs[0]
    p.text = "NBE Recommender"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = BLUE
    p = agent2_frame.add_paragraph()
    p.text = "\n• Priority scoring\n• At-risk detection\n• Channel optimization\n• Message personalization\n• Confidence scoring"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY

    # Orchestrator
    agent3_box = slide.shapes.add_textbox(Inches(6.6), Inches(2), Inches(2.5), Inches(3.5))
    agent3_frame = agent3_box.text_frame
    agent3_frame.word_wrap = True
    p = agent3_frame.paragraphs[0]
    p.text = "Orchestrator"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = BLUE
    p = agent3_frame.add_paragraph()
    p.text = "\n• Coordinates agents\n• Territory analysis\n• Batch processing\n• Report generation\n• CRM integration"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY

    # Data flow
    flow_box = slide.shapes.add_textbox(Inches(1), Inches(6), Inches(8), Inches(1))
    flow_frame = flow_box.text_frame
    p = flow_frame.paragraphs[0]
    p.text = "CRM Data → AI Analysis → Actionable Recommendations → Field Execution"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p.alignment = PP_ALIGN.CENTER

    # SLIDE 5: Key Features
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Key Features & Capabilities"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(40)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE

    # Left column
    left_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(4), Inches(5))
    left_frame = left_box.text_frame
    left_frame.word_wrap = True

    left_features = [
        ("HCP Micro-Segmentation", "Individual physician profiling beyond traditional tier systems"),
        ("At-Risk Detection", "Proactive identification of disengaging relationships (>90 days)"),
        ("Channel Optimization", "AI recommends optimal contact method per HCP"),
        ("Product-Specialty Alignment", "Automatic matching based on indication and expertise")
    ]

    for i, (title, desc) in enumerate(left_features):
        p = left_frame.paragraphs[0] if i == 0 else left_frame.add_paragraph()
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = BLUE
        p.space_after = Pt(5)

        p = left_frame.add_paragraph()
        p.text = desc
        p.font.size = Pt(13)
        p.font.color.rgb = GRAY
        p.space_after = Pt(20)

    # Right column
    right_box = slide.shapes.add_textbox(Inches(5.2), Inches(1.8), Inches(4), Inches(5))
    right_frame = right_box.text_frame
    right_frame.word_wrap = True

    right_features = [
        ("Confidence Scoring", "Every recommendation includes 0.0-1.0 AI confidence level"),
        ("Compliance Ready", "Audit logging, data anonymization, no PHI to AI"),
        ("Multi-Agent Orchestration", "Coordinated workflow across specialized agents"),
        ("CRM Integration", "JSON output for Salesforce, Veeva, or any CRM system")
    ]

    for i, (title, desc) in enumerate(right_features):
        p = right_frame.paragraphs[0] if i == 0 else right_frame.add_paragraph()
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = BLUE
        p.space_after = Pt(5)

        p = right_frame.add_paragraph()
        p.text = desc
        p.font.size = Pt(13)
        p.font.color.rgb = GRAY
        p.space_after = Pt(20)

    # SLIDE 6: AI Agent Outputs - Real Data
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Live Agent Output: NBE Recommendations"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(36)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE

    # Example 1
    example1_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(8.4), Inches(2))
    example1_frame = example1_box.text_frame
    example1_frame.word_wrap = True

    p = example1_frame.paragraphs[0]
    p.text = "Dr. H. Smith 85 - Tier A Oncologist | Priority: HIGH | Confidence: 92%"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLUE

    p = example1_frame.add_paragraph()
    p.text = "Action: Schedule urgent in-person visit to re-engage and assess current treatment protocols"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY
    p.space_after = Pt(8)

    p = example1_frame.add_paragraph()
    p.text = "Message: 'Latest clinical data shows NBE003 achieving superior progression-free survival in metastatic melanoma patients'"
    p.font.size = Pt(13)
    p.font.color.rgb = GRAY
    p.space_after = Pt(8)

    p = example1_frame.add_paragraph()
    p.text = "Rationale: High-value HCP out of contact for 443 days with low positive outcome rate (14%) despite good sentiment. Immediate re-engagement critical."
    p.font.size = Pt(12)
    p.font.italic = True
    p.font.color.rgb = GRAY

    # Example 2
    example2_box = slide.shapes.add_textbox(Inches(0.8), Inches(3.9), Inches(8.4), Inches(2))
    example2_frame = example2_box.text_frame
    example2_frame.word_wrap = True

    p = example2_frame.paragraphs[0]
    p.text = "Dr. G. Smith 6 - Tier A Neurologist | Priority: HIGH | Confidence: 85%"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLUE

    p = example2_frame.add_paragraph()
    p.text = "Action: Schedule urgent re-engagement call to rebuild relationship and assess current MS treatment approach"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY
    p.space_after = Pt(8)

    p = example2_frame.add_paragraph()
    p.text = "Message: 'Latest Neuro-Delta clinical data shows superior efficacy in relapsing MS patients - let's discuss impact on your protocols'"
    p.font.size = Pt(13)
    p.font.color.rgb = GRAY
    p.space_after = Pt(8)

    p = example2_frame.add_paragraph()
    p.text = "Rationale: 15+ months out of contact with at-risk status and low outcomes (14%). High priority score (167.39) and large patient volume (423) make re-engagement critical."
    p.font.size = Pt(12)
    p.font.italic = True
    p.font.color.rgb = GRAY

    # Footer note
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.2), Inches(8.4), Inches(0.6))
    footer_frame = footer_box.text_frame
    p = footer_frame.paragraphs[0]
    p.text = "Sample output from Northeast Territory analysis - Generated by NBE Recommender Agent with Claude Sonnet 4"
    p.font.size = Pt(11)
    p.font.italic = True
    p.font.color.rgb = LIGHT_GRAY
    p.alignment = PP_ALIGN.CENTER

    # SLIDE 7: Business Impact & ROI
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Business Impact & ROI"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(40)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE

    # Metrics grid - Top row
    metric1_box = slide.shapes.add_textbox(Inches(1), Inches(2), Inches(3.5), Inches(1.2))
    metric1_frame = metric1_box.text_frame
    p = metric1_frame.paragraphs[0]
    p.text = "3-5"
    p.font.size = Pt(48)
    p.font.bold = True
    p.font.color.rgb = BLUE
    p.alignment = PP_ALIGN.CENTER
    p = metric1_frame.add_paragraph()
    p.text = "High-Priority Recommendations\nPer Territory Analysis"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY
    p.alignment = PP_ALIGN.CENTER

    metric2_box = slide.shapes.add_textbox(Inches(5.5), Inches(2), Inches(3.5), Inches(1.2))
    metric2_frame = metric2_box.text_frame
    p = metric2_frame.paragraphs[0]
    p.text = "86%"
    p.font.size = Pt(48)
    p.font.bold = True
    p.font.color.rgb = BLUE
    p.alignment = PP_ALIGN.CENTER
    p = metric2_frame.add_paragraph()
    p.text = "Average AI Confidence Score\nOn All Recommendations"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY
    p.alignment = PP_ALIGN.CENTER

    # Bottom row
    metric3_box = slide.shapes.add_textbox(Inches(1), Inches(3.8), Inches(3.5), Inches(1.2))
    metric3_frame = metric3_box.text_frame
    p = metric3_frame.paragraphs[0]
    p.text = "$787K"
    p.font.size = Pt(48)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p.alignment = PP_ALIGN.CENTER
    p = metric3_frame.add_paragraph()
    p.text = "Potential Revenue Impact\nFrom Northeast Territory"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY
    p.alignment = PP_ALIGN.CENTER

    metric4_box = slide.shapes.add_textbox(Inches(5.5), Inches(3.8), Inches(3.5), Inches(1.2))
    metric4_frame = metric4_box.text_frame
    p = metric4_frame.paragraphs[0]
    p.text = "100%"
    p.font.size = Pt(48)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p.alignment = PP_ALIGN.CENTER
    p = metric4_frame.add_paragraph()
    p.text = "Recommendations Require\nImmediate Action"
    p.font.size = Pt(14)
    p.font.color.rgb = GRAY
    p.alignment = PP_ALIGN.CENTER

    # Value drivers
    value_box = slide.shapes.add_textbox(Inches(1), Inches(5.5), Inches(8), Inches(1.5))
    value_frame = value_box.text_frame
    value_frame.word_wrap = True

    p = value_frame.paragraphs[0]
    p.text = "Value Drivers:"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE
    p.space_after = Pt(12)

    values = [
        "Prevent at-risk HCP disengagement before revenue loss",
        "Optimize rep time by prioritizing highest-value interactions",
        "Increase positive outcome rates through personalized messaging",
        "Multi-channel strategy reduces wasted outreach attempts"
    ]

    for value in values:
        p = value_frame.add_paragraph()
        p.text = "• " + value
        p.font.size = Pt(14)
        p.font.color.rgb = GRAY
        p.space_after = Pt(8)

    # SLIDE 8: Technology Stack
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Technology Stack & Architecture"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(40)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE

    # Main tech stack
    stack_box = slide.shapes.add_textbox(Inches(1.5), Inches(1.8), Inches(7), Inches(4))
    stack_frame = stack_box.text_frame
    stack_frame.word_wrap = True

    tech_items = [
        ("Claude Sonnet 4", "State-of-the-art AI reasoning engine for medical and business intelligence"),
        ("Python 3.11", "Production-grade data processing and agent orchestration"),
        ("Pandas", "CRM data analysis and metric calculation"),
        ("Pydantic", "Data validation and schema enforcement for reliability"),
        ("Multi-Agent Pattern", "Specialized agents with coordinated workflows"),
        ("JSON API", "Standard integration format for CRM systems (Salesforce, Veeva)"),
        ("Environment Config", "Secure credential management and deployment flexibility")
    ]

    for i, (tech, desc) in enumerate(tech_items):
        p = stack_frame.paragraphs[0] if i == 0 else stack_frame.add_paragraph()
        p.text = tech
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = BLUE
        p.space_after = Pt(5)

        p = stack_frame.add_paragraph()
        p.text = desc
        p.font.size = Pt(14)
        p.font.color.rgb = GRAY
        p.space_after = Pt(18)

    # Architecture highlight
    arch_box = slide.shapes.add_textbox(Inches(1), Inches(6.2), Inches(8), Inches(0.8))
    arch_frame = arch_box.text_frame
    p = arch_frame.paragraphs[0]
    p.text = "Production-Ready: Modular, Testable, Scalable, Compliance-Focused"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p.alignment = PP_ALIGN.CENTER

    # SLIDE 9: Analogies & Value Proposition
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "The Value Proposition"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(40)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE

    # Main analogy
    analogy_box = slide.shapes.add_textbox(Inches(1), Inches(1.8), Inches(8), Inches(1.5))
    analogy_frame = analogy_box.text_frame
    analogy_frame.word_wrap = True

    p = analogy_frame.paragraphs[0]
    p.text = '"Like having a sales strategist analyze every physician relationship"'
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.italic = True
    p.font.color.rgb = BLUE
    p.alignment = PP_ALIGN.CENTER

    # Comparison table
    before_box = slide.shapes.add_textbox(Inches(0.8), Inches(3.8), Inches(4), Inches(3))
    before_frame = before_box.text_frame
    before_frame.word_wrap = True

    p = before_frame.paragraphs[0]
    p.text = "Traditional CRM Analytics"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = GRAY
    p.space_after = Pt(15)

    before_items = [
        "HCP001 has a score of 87",
        "Tier A physician",
        "Last contact: 443 days ago",
        "Positive outcome rate: 14%",
        "Next action: ?"
    ]

    for item in before_items:
        p = before_frame.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(14)
        p.font.color.rgb = GRAY
        p.space_after = Pt(10)

    after_box = slide.shapes.add_textbox(Inches(5.2), Inches(3.8), Inches(4), Inches(3))
    after_frame = after_box.text_frame
    after_frame.word_wrap = True

    p = after_frame.paragraphs[0]
    p.text = "NBE Agents Platform"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p.space_after = Pt(15)

    after_items = [
        '"Call Dr. Smith this week"',
        '"Use in-person visit"',
        '"Discuss Onco-Gamma"',
        '"Lead with new efficacy data"',
        '"92% confidence"'
    ]

    for item in after_items:
        p = after_frame.add_paragraph()
        p.text = "✓ " + item
        p.font.size = Pt(14)
        p.font.color.rgb = GRAY
        p.space_after = Pt(10)

    # Bottom tagline
    tagline_box = slide.shapes.add_textbox(Inches(1), Inches(6.5), Inches(8), Inches(0.6))
    tagline_frame = tagline_box.text_frame
    p = tagline_frame.paragraphs[0]
    p.text = "Proactive Recommendations, Not Reactive Reporting"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.italic = True
    p.font.color.rgb = BLUE
    p.alignment = PP_ALIGN.CENTER

    # SLIDE 10: Next Steps & Roadmap
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    title_frame.text = "Next Steps & Roadmap"
    title_para = title_frame.paragraphs[0]
    title_para.font.size = Pt(40)
    title_para.font.bold = True
    title_para.font.color.rgb = DARK_BLUE

    # Current capabilities
    current_box = slide.shapes.add_textbox(Inches(1), Inches(1.8), Inches(8), Inches(2))
    current_frame = current_box.text_frame
    current_frame.word_wrap = True

    p = current_frame.paragraphs[0]
    p.text = "Ready Today:"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = GREEN
    p.space_after = Pt(12)

    current_items = [
        "Production-ready codebase with 3 AI agents",
        "Processes 100 HCPs with real CRM data structure",
        "JSON output for CRM integration (Salesforce, Veeva)",
        "Compliance features: audit logging, data anonymization",
        "Scalable architecture for enterprise deployment"
    ]

    for item in current_items:
        p = current_frame.add_paragraph()
        p.text = "✓ " + item
        p.font.size = Pt(16)
        p.font.color.rgb = GRAY
        p.space_after = Pt(10)

    # Future enhancements
    future_box = slide.shapes.add_textbox(Inches(1), Inches(4.2), Inches(8), Inches(2.3))
    future_frame = future_box.text_frame
    future_frame.word_wrap = True

    p = future_frame.paragraphs[0]
    p.text = "Future Enhancements:"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = BLUE
    p.space_after = Pt(12)

    future_items = [
        "Sentiment analysis from email/call transcripts for deeper HCP insights",
        "Predictive modeling for prescription likelihood and revenue forecasting",
        "Territory optimization algorithms for rep assignment",
        "Dashboard for sales managers with real-time territory health",
        "Direct integration with Salesforce/Veeva APIs (currently CSV-based)",
        "Feedback loop from field outcomes to improve AI recommendations"
    ]

    for item in future_items:
        p = future_frame.add_paragraph()
        p.text = "→ " + item
        p.font.size = Pt(14)
        p.font.color.rgb = GRAY
        p.space_after = Pt(8)

    # Closing
    closing_box = slide.shapes.add_textbox(Inches(1), Inches(6.8), Inches(8), Inches(0.6))
    closing_frame = closing_box.text_frame
    p = closing_frame.paragraphs[0]
    p.text = "Built for pharmaceutical field teams who need to maximize face time with HCPs"
    p.font.size = Pt(16)
    p.font.italic = True
    p.font.color.rgb = BLUE
    p.alignment = PP_ALIGN.CENTER

    # Save presentation
    output_path = "/home/user/Claude1st/pharma-nbe-agents/NBE_Executive_Deck.pptx"
    prs.save(output_path)
    print(f"✓ Executive deck created successfully: {output_path}")
    print(f"✓ 10 slides generated with professional formatting")
    print(f"✓ Ready for download and interview presentation")

    return output_path

if __name__ == "__main__":
    create_executive_deck()
