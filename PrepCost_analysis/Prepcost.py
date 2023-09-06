import requests
import pandas as pd
import json
from pandas import json_normalize
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def calculate_date_ranges():
    today = datetime.now()
    last_sunday = today - timedelta(days=(today.weekday() + 1) % 7)
    last_monday = last_sunday - timedelta(days=6)
    date_ranges = [
        (last_monday - timedelta(days=7), last_sunday - timedelta(days=7)),
        (last_monday, last_sunday)
    ]
    return date_ranges

def fetch_and_process_data(start_date_str, end_date_str, date_range_str):
    url = f"https://api.7shifts.com/v2/reports/hours_and_wages?punches=true&company_id=163696&from={start_date_str}&to={end_date_str}&department_id=292954"
    headers = {
        "accept": "application/json",
        "authorization": "{bearer_token}"
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['users'])
        
        roles_data = []
        for roles in df['roles']:
            for role in roles:
                roles_data.append(role)
        
        df_roles = pd.DataFrame(roles_data)
        
        df_roles['total'] = df_roles['total'].astype(str).str.replace("'", '"').apply(json.loads)
        df_unpacked = json_normalize(df_roles['total'])

        df_roles = pd.concat([df_roles, df_unpacked], axis=1)
        df_roles.drop(columns=['total'], inplace=True)

        df_grouped = df_roles.groupby(['role_id', 'role_label', 'location_label']).sum().reset_index()

        df_grouped['total_hours'] = df_grouped['regular_hours'] + df_grouped['overtime_hours']
        df_grouped['total_pay'] = df_grouped['regular_pay'] + df_grouped['overtime_pay']
        df_filtered = df_grouped[['role_id', 'role_label', 'total_hours', 'total_pay']]

        df_filtered = df_filtered[df_filtered['role_id'] != 0]

        df_filtered['total_hours'] = df_filtered['total_hours'].round(2)
        df_filtered['total_pay'] = df_filtered['total_pay'].round(2)

        df_filtered.to_csv(f'{date_range_str}.csv', index=False)
        print(f"Data saved to {date_range_str}.csv")
        
        return df_filtered
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def plot_combined_chart(df_filtered1, df_filtered2, date_range_str1, date_range_str2):
    # Combining the data of both weeks into a single data frame for total pay
    df_combined_pay = df_filtered1.merge(df_filtered2, on='role_label', how='outer', suffixes=(f'_{date_range_str1}', f'_{date_range_str2}')).fillna(0)

    # Sorting the dataframe based on the sum of total_pay from both weeks in descending order
    df_combined_pay['total_pay_sum'] = df_combined_pay[f'total_pay_{date_range_str1}'] + df_combined_pay[f'total_pay_{date_range_str2}']
    df_combined_pay.sort_values('total_pay_sum', ascending=False, inplace=True)
    df_combined_pay.drop(columns=['total_pay_sum'], inplace=True)

    # For the total pay bar chart
    ax1 = df_combined_pay.plot(x='role_label', y=[f'total_pay_{date_range_str1}', f'total_pay_{date_range_str2}'], kind='bar', figsize=(12, 8))
    plt.title('Total Pay by Role for the Two Weeks', fontsize=16, color='white')
    plt.ylabel('Total Pay', fontsize=14, color='white')
    plt.xlabel('Role Label', fontsize=14, color='white')
    plt.xticks(rotation=45, ha="right", fontsize=12, color='white')
    plt.yticks(color='white')
    ax1.legend(fontsize=12, facecolor='grey')
    plt.grid(axis='y')

    # Adding the total_pay values on top of the bars
    for i, v in enumerate(df_combined_pay[f'total_pay_{date_range_str1}']):
        ax1.text(i - 0.15, v + 10, "$"+str(round(v, 2)), ha='center', va='bottom', fontsize=8, color='black')

    for i, v in enumerate(df_combined_pay[f'total_pay_{date_range_str2}']):
        ax1.text(i + 0.15, v + 10, "$"+str(round(v, 2)), ha='center', va='bottom', fontsize=8, color='black')

    plt.tight_layout()
    plt.savefig(f'combined_barchart_pay_{date_range_str1}_and_{date_range_str2}.png', facecolor='#1e1e1e')  # Assuming GitHub dark mode background color
    plt.close()

    # Combining the data of both weeks into a single data frame for total hours
    df_combined_hours = df_filtered1.merge(df_filtered2, on='role_label', how='outer', suffixes=(f'_{date_range_str1}', f'_{date_range_str2}')).fillna(0)

    # Sorting the dataframe based on the sum of total_hours from both weeks in descending order
    df_combined_hours['total_hours_sum'] = df_combined_hours[f'total_hours_{date_range_str1}'] + df_combined_hours[f'total_hours_{date_range_str2}']
    df_combined_hours.sort_values('total_hours_sum', ascending=False, inplace=True)
    df_combined_hours.drop(columns=['total_hours_sum'], inplace=True)

    ax2 = df_combined_hours.plot(x='role_label', y=[f'total_hours_{date_range_str1}', f'total_hours_{date_range_str2}'], kind='bar', color=['orange', 'yellow'], figsize=(12, 8))
    plt.title('Total Hours by Role for the Two Weeks', fontsize=16, color='white')
    plt.ylabel('Total Hours', fontsize=14, color='white')
    plt.xlabel('Role Label', fontsize=14, color='white')
    plt.xticks(rotation=45, ha="right", fontsize=12, color='white')
    plt.yticks(color='white')
    ax2.legend(fontsize=12, facecolor='grey')
    plt.grid(axis='y')

    # Adding the total_hours values on top of the bars
    for i, v in enumerate(df_combined_hours[f'total_hours_{date_range_str1}']):
        ax2.text(i - 0.15, v + 1, str(round(v, 2))+' hrs', ha='center', va='bottom', fontsize=8, color='black')

    for i, v in enumerate(df_combined_hours[f'total_hours_{date_range_str2}']):
        ax2.text(i + 0.15, v + 1, str(round(v, 2))+' hrs', ha='center', va='bottom', fontsize=8, color='black')

    plt.tight_layout()
    plt.savefig(f'combined_barchart_hours_{date_range_str1}_and_{date_range_str2}.png', facecolor='#1e1e1e')
    print(f"Combined bar chart for total hours saved as combined_barchart_hours_{date_range_str1}_and_{date_range_str2}.png")

date_ranges = calculate_date_ranges()

dataframes = []
date_range_strings = []

for start_date, end_date in date_ranges:
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')
    date_range_str = f"{start_date_str}_to_{end_date_str}"
    
    df = fetch_and_process_data(start_date_str, end_date_str, date_range_str)
    if df is not None:
        dataframes.append(df)
        date_range_strings.append(date_range_str)

if len(dataframes) == 2:
    plot_combined_chart(dataframes[0], dataframes[1], date_range_strings[0], date_range_strings[1])
else:
    print("Could not generate combined chart due to missing data.")
