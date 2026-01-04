"""
Generate sample CRM data for pharmaceutical NBE agents demonstration
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

print("Generating sample pharmaceutical CRM data...")

# 1. Generate HCP (Healthcare Professional) Profiles
print("\n1. Generating HCP profiles...")
specialties = ['Oncology', 'Cardiology', 'Neurology', 'Immunology', 'Rheumatology']
practice_types = ['Hospital', 'Private Practice', 'Academic Medical Center', 'Clinic']
territories = ['Northeast', 'Southeast', 'Midwest', 'Southwest', 'West']

hcp_data = []
for i in range(1, 101):  # 100 HCPs
    hcp_data.append({
        'hcp_id': f'HCP{i:03d}',
        'name': f'Dr. {chr(65 + (i % 26))}. Smith {i}',
        'specialty': random.choice(specialties),
        'practice_type': random.choice(practice_types),
        'territory': random.choice(territories),
        'patient_volume': random.randint(50, 500),
        'years_in_practice': random.randint(1, 35),
        'academic_affiliation': random.choice([True, False]),
        'preferred_contact_method': random.choice(['Email', 'Phone', 'In-Person']),
        'tier': random.choice(['A', 'B', 'C'])  # A=high value, C=low value
    })

hcp_df = pd.DataFrame(hcp_data)
hcp_df.to_csv('hcp_profiles.csv', index=False)
print(f"   Created {len(hcp_df)} HCP profiles")

# 2. Generate Products
print("\n2. Generating product data...")
products_data = [
    {
        'product_id': 'NBE001',
        'product_name': 'Immunex-Alpha',
        'indication': 'Rheumatoid Arthritis',
        'launch_date': '2023-06-01',
        'price_per_treatment': 5000,
        'target_specialties': 'Rheumatology,Immunology'
    },
    {
        'product_id': 'NBE002',
        'product_name': 'Cardio-Beta',
        'indication': 'Heart Failure',
        'launch_date': '2023-09-15',
        'price_per_treatment': 3500,
        'target_specialties': 'Cardiology'
    },
    {
        'product_id': 'NBE003',
        'product_name': 'Onco-Gamma',
        'indication': 'Metastatic Melanoma',
        'launch_date': '2024-01-10',
        'price_per_treatment': 8000,
        'target_specialties': 'Oncology'
    },
    {
        'product_id': 'NBE004',
        'product_name': 'Neuro-Delta',
        'indication': 'Multiple Sclerosis',
        'launch_date': '2023-03-20',
        'price_per_treatment': 6500,
        'target_specialties': 'Neurology'
    }
]

products_df = pd.DataFrame(products_data)
products_df.to_csv('products.csv', index=False)
print(f"   Created {len(products_df)} products")

# 3. Generate Territories
print("\n3. Generating territory data...")
territory_data = []
for territory in territories:
    territory_data.append({
        'territory_id': f'T{territories.index(territory) + 1:02d}',
        'territory_name': territory,
        'region': 'US',
        'hcp_count': len(hcp_df[hcp_df['territory'] == territory]),
        'rep_count': random.randint(3, 8),
        'quarterly_target': random.randint(500000, 2000000)
    })

territory_df = pd.DataFrame(territory_data)
territory_df.to_csv('territories.csv', index=False)
print(f"   Created {len(territory_df)} territories")

# 4. Generate Interactions
print("\n4. Generating interaction history...")
interaction_types = ['Office Visit', 'Phone Call', 'Email', 'Virtual Meeting', 'Conference']
interaction_outcomes = ['Positive', 'Neutral', 'Needs Follow-up', 'Sample Requested']

interactions_data = []
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 1, 1)

# Generate 500 interactions
for i in range(1, 501):
    hcp = random.choice(hcp_df['hcp_id'].values)
    product = random.choice(products_df['product_id'].values)

    # Random date in the past year
    days_diff = (end_date - start_date).days
    random_date = start_date + timedelta(days=random.randint(0, days_diff))

    interactions_data.append({
        'interaction_id': f'INT{i:04d}',
        'hcp_id': hcp,
        'product_id': product,
        'date': random_date.strftime('%Y-%m-%d'),
        'interaction_type': random.choice(interaction_types),
        'duration_minutes': random.randint(5, 60),
        'outcome': random.choice(interaction_outcomes),
        'samples_provided': random.choice([0, 0, 0, 5, 10, 15]),
        'rep_id': f'REP{random.randint(1, 25):03d}',
        'sentiment_score': round(random.uniform(0.3, 1.0), 2),
        'topics_discussed': random.choice([
            'Efficacy,Safety',
            'Dosing,Administration',
            'Patient Selection',
            'Clinical Trial Results',
            'Reimbursement'
        ])
    })

interactions_df = pd.DataFrame(interactions_data)
interactions_df.to_csv('interactions.csv', index=False)
print(f"   Created {len(interactions_df)} interactions")

# Summary
print("\n" + "="*60)
print("SAMPLE DATA GENERATION COMPLETE!")
print("="*60)
print(f"\nFiles created:")
print(f"  - hcp_profiles.csv ({len(hcp_df)} records)")
print(f"  - products.csv ({len(products_df)} records)")
print(f"  - territories.csv ({len(territory_df)} records)")
print(f"  - interactions.csv ({len(interactions_df)} records)")
print("\nData Summary:")
print(f"  - Specialties: {', '.join(specialties)}")
print(f"  - Territories: {', '.join(territories)}")
print(f"  - Products: {len(products_df)} NBE products")
print(f"  - Date Range: {start_date.date()} to {end_date.date()}")
print("\nReady for pharma-nbe-agents processing!")
