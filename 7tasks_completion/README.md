**Features:**

1. Automated Data Retrieval: Retrieves daily task list summaries from the 7Shifts API for a defined date range.
2. Data Aggregation: Aggregates the data into one dataset, offering a consolidated view of all necessary information.
3. Incomplete Task List Identification: Filters the dataset to highlight incomplete task lists, thus allowing managers to focus their attention where needed.
4. Data Export: Exports the filtered data to a CSV file, facilitating easy analysis and sharing.
5. Data Analysis and Visualization: Analyzes the data to identify which task lists are not completed the most frequently and visualizes this data through a bar chart.

**How It Works:**

1. Setting the Date Range: Define the start and end dates for data retrieval at the beginning of the script.
2. Data Retrieval: The script interacts with the 7Shifts platform via API calls, fetching the daily task list summaries within the chosen date range.
3. Data Processing: The data is processed to extract relevant details about each task list, including the completion status and percentage.
4. Filtering Incomplete Task Lists: The script filters the data to spotlight incomplete task lists where the completion percentage is less than 100%.
5. Removing Duplicate Dates: I found the way the data to be stored in 7shifts quite strange. For each task list on any given day, the "task_lists" field stores data for **all** task lists for that day, not just the data relevant to that task list. For that reason, the script removes rows with duplicate dates to prevent data redundancy, retaining only unique dates in the dataset.
6. Creating a Detailed Incomplete Task List: For each unique date, the script extracts details of incomplete task lists and collates this data into a new dataset.
7. Data Analysis and Visualization: The script analyzes the data to identify the task lists that are incomplete most frequently and visualizes this information through a bar chart, providing a graphical representation of the frequency of incomplete task lists.
8. Data Export: The new dataset, containing specifics of incomplete task lists, is exported to a CSV file for further scrutiny.

**Usage:**

1. Set up the necessary Python environment and install the required packages (requests, pandas, matplotlib, and seaborn).
2. Adjust the start_date and end_date variables at the beginning of the script to specify the date range for the data retrieval.
3. Run the script. It will automatically retrieve the data, identify the incomplete task lists, analyze the frequency of incompletions, and save the data and bar chart to files.
4. Open the CSV file and the bar chart image to analyze the incomplete task lists and identify areas requiring attention.

**Conclusion**

This script serves as a powerful tool for restaurant managers utilizing the 7Shifts platform to manage daily tasks. By automating the identification of incomplete task lists and visually representing the frequency of these incompletions, it saves time and facilitates a more focused and efficient approach to restaurant management.

For example: Upon running this script for the month of August at our King location, I can clearly see that the King FOH Opening Procedure is by far the most regularly incomplete task list. I can now quickly check the schedule to see who was opening on those days, and address the issue promptly.
