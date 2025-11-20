# create_data.py
import pandas as pd
import os

# Create data directory
if not os.path.exists('data'):
    os.makedirs('data')

# 1. Universities Data
unis = {
    'University_Name': ['Amity University Online', 'Manipal University Jaipur', 'LPU Online', 'Jain University', 'Chandigarh University'],
    'NAAC_Grade': ['A+', 'A+', 'A++', 'A++', 'A+'],
    'Placement_Rate': [92, 94, 88, 91, 89],
    'Average_Package': ['5.5 LPA', '6.2 LPA', '4.8 LPA', '5.9 LPA', '5.0 LPA'],
    'Total_Fee_INR': [345000, 175000, 160000, 210000, 180000],
    'Primary_Energy_Fit': ['Creator', 'Analyst', 'Catalyst', 'Influencer', 'Creator']
}
pd.DataFrame(unis).to_csv('data/university_program_details.csv', index=False)

# 2. Energy Types
energy = {
    'Type': ['Creator', 'Influencer', 'Catalyst', 'Analyst'],
    'Alias': ['Dynamo', 'Blaze', 'Tempo', 'Steel'],
    'Color': ['#9B59B6', '#E67E22', '#27AE60', '#3498DB'],
    'Description': ['The Innovator', 'The Connector', 'The Grounded', 'The Architect']
}
pd.DataFrame(energy).to_csv('data/energy_types.csv', index=False)

print("✅ Data files created successfully in /data folder!")
