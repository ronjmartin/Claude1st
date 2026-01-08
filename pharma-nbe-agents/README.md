# Pharmaceutical NBE Agents Platform

AI-Powered Sales Intelligence for Pharmaceutical Field Teams

## Overview

The Pharma NBE Agents Platform is a multi-agent AI system that analyzes CRM data to generate actionable Next Best Engagement (NBE) strategies for pharmaceutical sales teams. Built with Claude Sonnet 4, it provides intelligent HCP profiling, engagement recommendations, and business impact analysis.

## Key Features

- 🤖 **AI-Powered Analytics** - Claude Sonnet 4 for advanced reasoning and insights
- 🎯 **HCP Micro-Segmentation** - Individual physician profiling with personalized strategies
- 📊 **NBE Recommendations** - Next Best Engagement strategies with channel optimization
- 🔍 **At-Risk Detection** - Proactive identification of disengaging relationships
- 📈 **Priority Scoring** - Data-driven HCP prioritization based on tier, volume, engagement
- 💬 **Channel Optimization** - AI recommends optimal contact method per HCP
- 💊 **Product-Specialty Alignment** - Automatic matching of products to physician specialties
- ✅ **Confidence Scoring** - Every recommendation includes AI confidence level
- 🔒 **Compliance Ready** - Audit logging and data anonymization
- 🎼 **Multi-Agent Orchestration** - Coordinated workflow across all agents

## Architecture

### Agents

1. **HCP Profiler Agent** (`agents/hcp_profiler.py`)
   - Analyzes healthcare professional engagement patterns
   - Calculates engagement metrics (interactions, sentiment, outcomes)
   - Generates AI-powered insights and recommendations
   - Supports territory and tier-based segmentation

2. **NBE Recommender Agent** (`agents/nbe_recommender.py`)
   - Generates Next Best Engagement strategies
   - Prioritizes HCPs using multi-factor scoring
   - Identifies at-risk relationships
   - Recommends optimal channels and product focus
   - Outputs JSON for CRM integration

3. **Orchestrator Agent** (`agents/nbe_orchestrator.py`)
   - Coordinates all agents in integrated workflow
   - Runs complete territory analysis
   - Generates consolidated reports
   - Supports interactive and batch modes

## Quick Start

### Prerequisites

- Python 3.11+
- Anthropic API key

### Installation

```bash
# Clone and navigate to project
cd pharma-nbe-agents

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### Run Demo

```bash
# Full platform demo (recommended for first time)
python demo.py

# Individual agents
python agents/hcp_profiler.py        # HCP profiling
python agents/nbe_recommender.py     # NBE recommendations
python agents/nbe_orchestrator.py    # Complete workflow
```

## Usage

### Sample Data

The project includes sample CRM data:
- 100 Healthcare Professionals across 5 specialties
- 500 interactions over 12 months
- 4 NBE products (Immunex-Alpha, Cardio-Beta, Onco-Gamma, Neuro-Delta)
- 5 US territories

Generate fresh sample data:
```bash
cd data/sample_crm
python generate_sample_data.py
```

### Integration with Real CRM

Update `.env` with your CRM data paths:
```bash
HCP_DATA_PATH=./data/your_crm/hcp_profiles.csv
INTERACTION_DATA_PATH=./data/your_crm/interactions.csv
TERRITORY_DATA_PATH=./data/your_crm/territories.csv
PRODUCT_DATA_PATH=./data/your_crm/products.csv
```

### Configuration

Edit `.env` to customize:
```bash
# AI Model
NBE_MODEL=claude-sonnet-4-20250514

# Recommendations
MAX_RECOMMENDATIONS_PER_HCP=3
CONFIDENCE_THRESHOLD=0.7

# Compliance
ENABLE_AUDIT_LOGGING=true
ANONYMIZE_HCP_DATA=true
```

## Data Schema

### HCP Profiles (hcp_profiles.csv)
```
hcp_id, name, specialty, practice_type, territory, patient_volume,
years_in_practice, academic_affiliation, preferred_contact_method, tier
```

### Interactions (interactions.csv)
```
interaction_id, hcp_id, product_id, date, interaction_type,
duration_minutes, outcome, samples_provided, rep_id, sentiment_score
```

### Products (products.csv)
```
product_id, product_name, indication, launch_date,
price_per_treatment, target_specialties
```

### Territories (territories.csv)
```
territory_id, territory_name, region, hcp_count,
rep_count, quarterly_target
```

## Output

### HCP Profile Example
```
Profile Summary: Tier A neurologist with 14 years experience...
Engagement Assessment: MEDIUM-HIGH
  - Good sentiment score (0.68/1.0)
  - 40% positive outcome rate
  - Recent engagement (Dec 2024)

Top 3 Recommendations:
1. Increase face-to-face engagement
2. Focus on educational content
3. Optimize sample strategy

Product Focus: NBE004 (Neuro-Delta) - perfect specialty match
```

### NBE Recommendation Example
```json
{
  "hcp_id": "HCP080",
  "priority": "high",
  "urgency": "immediate",
  "recommended_action": "Schedule virtual meeting...",
  "recommended_channel": "Virtual Meeting",
  "product_focus": "NBE003",
  "key_message": "Latest efficacy data shows...",
  "rationale": "Tier A oncologist at-risk...",
  "confidence": 0.85,
  "priority_score": 170.9
}
```

## Business Impact

Example results from Northeast territory analysis:
- **3 high-priority recommendations** generated
- **86% average AI confidence** score
- **$787,500 potential revenue** impact (estimated)
- **100% immediate action** recommendations
- **Multi-channel strategy** (in-person, virtual, phone)

## Technology Stack

- **Python 3.11** - Core language
- **Anthropic Claude Sonnet 4** - AI reasoning engine
- **Pandas** - Data processing
- **Pydantic** - Data validation
- **python-dotenv** - Configuration management

## Project Structure

```
pharma-nbe-agents/
├── agents/
│   ├── hcp_profiler.py          # HCP analysis agent
│   ├── nbe_recommender.py       # NBE strategy agent
│   └── nbe_orchestrator.py      # Multi-agent coordinator
├── data/
│   └── sample_crm/              # Sample CRM data
│       ├── generate_sample_data.py
│       ├── hcp_profiles.csv
│       ├── interactions.csv
│       ├── products.csv
│       └── territories.csv
├── outputs/
│   └── recommendations/          # Generated recommendations
├── config/                       # Configuration files
├── logs/                         # Application logs
├── demo.py                       # Live demo script
├── requirements.txt              # Python dependencies
├── .env                          # Environment configuration
├── README.md                     # This file
└── DEMO_GUIDE.md                 # Demo presentation guide
```

## Development

### Running Tests
```bash
pytest
```

### Adding New Agents

1. Create new agent file in `agents/`
2. Inherit from base patterns in existing agents
3. Import and coordinate in `nbe_orchestrator.py`

### Extending Data Sources

Update data loaders in agent `__init__` methods:
```python
self.hcp_df = pd.read_csv(os.getenv('HCP_DATA_PATH'))
# or
self.hcp_df = fetch_from_api(crm_endpoint)
```

## Compliance & Security

- ✅ No PHI (Protected Health Information) sent to AI
- ✅ HCP data anonymization option
- ✅ Audit logging for all recommendations
- ✅ Configurable confidence thresholds
- ✅ Local data processing (no external storage)

## Roadmap

Future enhancements:
- [ ] Sentiment analysis from email/call transcripts
- [ ] Predictive modeling for prescription likelihood
- [ ] Territory optimization algorithms
- [ ] Dashboard for sales managers
- [ ] Integration with major CRM APIs (Salesforce, Veeva)
- [ ] Feedback loop from field outcomes
- [ ] Multi-language support

## License

Proprietary - Demo/Interview Project

## Contact

For questions or demo requests, contact the development team.

---

**Built with ❤️ for pharmaceutical sales teams**
