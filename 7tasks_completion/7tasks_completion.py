import requests
import pandas as pd
from datetime import datetime, timedelta
from ast import literal_eval
import matplotlib.pyplot as plt
import seaborn as sns

# Define the start and end dates
start_date = datetime(2023, 8, 1)
end_date = datetime(2023, 8, 31)

# Initialize an empty list to store the data
all_data = []

# Define the base URL and headers
url = "https://api.7shifts.com/v2/company/163696/task_list_daily_summary"
headers = {
    "accept": "application/json",
    "authorization": "{bearer_token}"
}

# Loop through each date in the range
current_date = start_date
while current_date <= end_date:
    # Get the data for the current date
    params = {
        "location_id": 126664,
        "date": current_date.strftime('%Y-%m-%d')
    }
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
    
        # Extract the 'data' field from the response
        daily_data = data.get('data', {})
    
        # Extract the 'task_lists' field
        task_lists = daily_data.get('task_lists', [])
    
        # Loop through each task list and create a row with combined data
        for task_list in task_lists:
            row_data = daily_data.copy()
            row_data.update(task_list)
            all_data.append(row_data)
    else:
        print(f"Failed to retrieve data for {current_date.strftime('%Y-%m-%d')}. Status code: {response.status_code}")

    
    # Move to the next date
    current_date += timedelta(days=1)

# Convert the combined data to a pandas DataFrame
df = pd.DataFrame(all_data)

# Save the DataFrame to a CSV file
df.to_csv('task_list_daily_summary.csv', index=False)

print("Data saved to task_list_daily_summary.csv")

# Filter the dataframe to keep only rows where total_completed_percentage is less than 100
incomplete_tasks_df = df[df['total_completed_percentage'] < 100]

# Remove rows with duplicate dates
incomplete_tasks_df = incomplete_tasks_df.drop_duplicates(subset=['date'])

# Initialize an empty list to store the new data
new_data = []

# Iterate through each row in the incomplete_tasks_df
for _, row in incomplete_tasks_df.iterrows():
    date = row['date']
    
    # The 'task_lists' column already contains a list of dictionaries
    task_lists = row['task_lists']
    
    # Iterate through each task list
    for task_list in task_lists:
        # Check if the task list is incomplete
        if task_list['completion_percentage'] < 100:
            # Create a new row with the required format
            new_row = {
                'Date': date,
                'Title': task_list['title'],
                'completion_status': task_list['completion_status'],
                'completion_percentage': task_list['completion_percentage']
            }
            # Add the new row to the new data list
            new_data.append(new_row)

# Create a new dataframe from the new data
new_df = pd.DataFrame(new_data)

# Save the new dataframe to a new CSV file
new_df.to_csv('incomplete_task_lists_detailed.csv', index=False)

print("Detailed incomplete task lists saved to incomplete_task_lists_detailed.csv")



# Data Analysis
task_list_frequency = new_df['Title'].value_counts().reset_index()
task_list_frequency.columns = ['Title', 'Frequency']

# Data Visualization
# Bar Chart to visualize the frequency of incomplete task lists
plt.figure(figsize=(10, 6))
sns.barplot(x='Frequency', y='Title', data=task_list_frequency)
plt.title('Frequency of Incomplete Task Lists')
plt.xlabel('Frequency')
plt.ylabel('Task List Title')
plt.tight_layout()
plt.savefig('task_list_frequency.png')
plt.show()

print("Data analysis and visualization completed. Charts saved as 'task_list_frequency.png' and 'task_list_trend.png'.")