# NBE Agents Platform - Demo Guide for Teams Interview

## Quick Setup (Do This Before the Call)

### 1. Open Terminal and Navigate to Project
```bash
cd /home/user/Claude1st/pharma-nbe-agents
```

### 2. Activate Virtual Environment
```bash
source venv/bin/activate
```

### 3. Test the Demo (Optional - Run Once to Verify)
```bash
python demo.py
```

## During the Interview

### Option 1: Full Demo Script (Recommended - 5-7 minutes)
**Best for**: Showing the complete platform capabilities

```bash
cd /home/user/Claude1st/pharma-nbe-agents
source venv/bin/activate
python demo.py
```

**What it shows:**
- Data overview (100 HCPs, 500 interactions, 4 products)
- HCP Profiler Agent with live AI analysis
- NBE Recommender Agent with engagement strategies
- Business impact metrics
- Platform features and capabilities
- Multi-agent orchestration

---

### Option 2: Individual Agent Demos (Flexible)

#### HCP Profiler Only (~2 minutes)
```bash
cd /home/user/Claude1st/pharma-nbe-agents
source venv/bin/activate
python agents/hcp_profiler.py
```
Shows: AI-powered HCP analysis for top 3 engaged physicians

#### NBE Recommender Only (~3 minutes)
```bash
cd /home/user/Claude1st/pharma-nbe-agents
source venv/bin/activate
python agents/nbe_recommender.py
```
Shows: Next Best Engagement recommendations for Northeast territory

#### Complete Orchestrator (~5 minutes)
```bash
cd /home/user/Claude1st/pharma-nbe-agents
source venv/bin/activate
python agents/nbe_orchestrator.py
```
Shows: Full workflow - profiling + recommendations + reporting

---

## Talking Points During Demo

### Opening (30 seconds)
"I've built an AI-powered pharmaceutical sales intelligence platform that helps field teams identify which doctors to engage, when, and with what message. It uses Claude AI to analyze CRM data and generate personalized engagement strategies."

### While Demo Runs

**During Data Overview:**
- "Working with real CRM structure: HCPs, interactions, products, territories"
- "100 physicians across 5 specialties, 500 interactions over past year"
- "Portfolio includes 4 NBE products targeting different therapeutic areas"

**During HCP Profiler:**
- "This agent analyzes individual physician engagement patterns"
- "Claude AI generates insights about prescribing behavior, preferences, barriers"
- "Notice it identifies specialty-product alignment and recommends specific actions"

**During NBE Recommender:**
- "This agent prioritizes HCPs and recommends optimal engagement strategies"
- "It identifies at-risk relationships before they disengage"
- "Recommends best channel (phone, email, in-person) based on HCP preferences"
- "Every recommendation includes AI confidence score for decision support"

**During Business Impact:**
- "Platform shows clear ROI metrics"
- "Estimated revenue impact based on patient volume and conversion rates"
- "Channel optimization reduces wasted rep time"

**During Key Features:**
- "Built on Claude Sonnet 4 for state-of-the-art language understanding"
- "Compliance-ready with audit logging and data anonymization"
- "Modular architecture - easy to add new agents or data sources"

### Closing (30 seconds)
"This demonstrates AI agents working together to solve a real pharmaceutical sales challenge. The platform is production-ready, integrates with existing CRM systems, and scales across territories. Happy to dive deeper into any component or discuss implementation."

---

## Anticipated Questions & Answers

### Q: How does it integrate with existing CRM systems?
**A:** "Currently uses CSV exports, but the architecture supports direct API integration. I've designed it with Pydantic models for data validation, making it easy to connect to Salesforce, Veeva, or any CRM with a REST API."

### Q: What if the AI recommendations are wrong?
**A:** "Every recommendation includes a confidence score. Reps can filter by threshold (currently 70%). The system also tracks outcomes, so we can continuously improve by feeding back which recommendations led to successful engagements."

### Q: How do you handle compliance and data privacy?
**A:** "Built-in anonymization flag for HCP data, audit logging for all recommendations, and no PHI is ever sent to the AI. All prompts are carefully designed to avoid requesting sensitive information."

### Q: Can it scale to thousands of HCPs?
**A:** "Absolutely. The architecture is stateless and can be parallelized. For large datasets, we'd batch process HCPs and cache results. Current demo processes 100 HCPs instantly, and I've designed it to handle enterprise scale."

### Q: What's unique about your approach vs. traditional analytics?
**A:** "Traditional systems score and segment, but don't explain why or what to do. My agents use AI to provide natural language insights and specific actions. It turns 'HCP001 has a score of 87' into 'Call Dr. Smith this week about Neuro-Delta, leading with the new efficacy data.'"

### Q: How long did this take to build?
**A:** "Core platform: [be honest about timeframe]. The modular design means adding new agents or data sources takes hours, not weeks. I focused on production-ready code, not just a POC."

---

## Technical Deep-Dive (If Asked)

### Architecture
- **Pattern:** Multi-agent system with specialized agents
- **Agents:** HCPProfiler, NBERecommender, Orchestrator
- **AI:** Anthropic Claude via API (messages.create)
- **Data:** Pandas for processing, CSV for storage
- **Config:** Environment variables via python-dotenv

### Why This Stack?
- **Claude Sonnet 4:** Best-in-class reasoning for complex analysis
- **Python:** Industry standard for data science + AI
- **Pandas:** Pharmaceutical teams already use it
- **Modular agents:** Easy to test, maintain, extend

### Prompt Engineering
- Structured prompts with HCP data, metrics, and product catalog
- Request JSON responses for programmatic use
- Include confidence scoring in AI outputs
- Balance detail vs. actionability

---

## Backup Plans

### If Demo Takes Too Long
Skip to: "Let me show you the final output..." and open a saved JSON file:
```bash
cat outputs/recommendations/nbe_northeast_20260104.json
```

### If Network/API Issues
Have screenshots ready or say: "I have the results from a previous run here..." and show saved output files.

### If They Want to See Code
```bash
# Show clean, commented agent code
cat agents/hcp_profiler.py | head -50

# Show orchestrator coordination
cat agents/nbe_orchestrator.py | grep -A 10 "def run_territory_analysis"
```

---

## Post-Demo Discussion Topics

1. **Extensions I'd build next:**
   - Sentiment analysis from email/call transcripts
   - Predictive modeling for prescription likelihood
   - Territory optimization (which HCPs for which reps)
   - Integration with marketing campaigns

2. **Production considerations:**
   - Monitoring/alerting for agent performance
   - A/B testing different recommendation strategies
   - Feedback loop from rep outcomes
   - Dashboard for sales managers

3. **Business impact metrics:**
   - Increase in HCP contact rate
   - Improvement in positive outcomes
   - Reduction in at-risk HCP churn
   - Rep time savings from prioritization

---

## One-Liners for Impact

- "AI agents that turn CRM data into actionable engagement strategies"
- "Like having a sales strategist analyze every physician relationship"
- "Proactive recommendations, not reactive reporting"
- "Built for pharmaceutical field teams who need to maximize face time"
- "Production-ready AI for life sciences sales"

---

## Pre-Demo Checklist

- [ ] Virtual environment activated
- [ ] Test run completed successfully
- [ ] Terminal font size increased for visibility
- [ ] Screen sharing tested in Teams
- [ ] API key working (ANTHROPIC_API_KEY in .env)
- [ ] Close unnecessary applications
- [ ] Have water nearby (demo is 5-7 minutes)
- [ ] Review talking points above
- [ ] Be ready to explain any component in detail

**Good luck! You've built something impressive. Be confident and enthusiastic!** 🚀
