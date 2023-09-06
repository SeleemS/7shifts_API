import requests
import pandas as pd
import matplotlib.pyplot as plt
from pandas import json_normalize

# Step 1: Get data from API
url = "https://api.7shifts.com/v2/company/163696/locations/261786/tip_pool_detailed_report?start_date=2023-08-01&end_date=2023-08-31"
headers = {
    "accept": "application/json",
    "authorization": "{bearer_token}"
}
response = requests.get(url, headers=headers)
data = response.json()

# Step 2: Transform nested JSON structure into a flat structure
report_rows = data['data']['report_rows']
flattened_data = []

for row in report_rows:
    for tip_pool in row['tip_pools']:
        for assigned_tip in tip_pool['assigned_tips']:
            flattened_data.append(assigned_tip)

# Step 3: Create a DataFrame (TESTING)
df = pd.DataFrame(flattened_data)

# Step 4: Save the DataFrame to a CSV file
df.to_csv('tip_out_data.csv', index=False)
print("Data saved to 'tip_out_data.csv'")

# Step 5: Filter the DataFrame to include only rows where the role is 'Cash/Expedite'
cash_expedite_df = df[df['role_name'] == 'Cashier']

# Step 6: Group by first and last name and sum values
grouped_df = cash_expedite_df.groupby(['first_name', 'last_name'])[['hours_worked', 'tip_out']].sum().reset_index()

# Step 7: Keep only required columns and calculate 'tips_per_hour'
grouped_df['tips_per_hour'] = grouped_df['tip_out'] / grouped_df['hours_worked']

# Step 8: Sort by 'tips_per_hour' in descending order
grouped_df = grouped_df.sort_values('tips_per_hour', ascending=False)

# Step 9: Save the grouped and sorted data to a new CSV file
grouped_df.to_csv('sorted_data.csv', index=False)
print("Grouped and sorted data saved to 'grouped_sorted_cash_expedite_data.csv'")

# Step 10: Create a bar chart to compare each cashier's tip out per hour
grouped_df['full_name'] = grouped_df['first_name'] + " " + grouped_df['last_name']
plt.bar(grouped_df['full_name'], grouped_df['tips_per_hour'])
plt.xlabel('Cashier')
plt.ylabel('Tips per Hour')
plt.title('Tips per Hour by Cashier')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('tipout_barchart.png')
plt.show()

