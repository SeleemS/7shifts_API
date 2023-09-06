**Cashier Performance Analysis Script**

**Overview**

This script is a useful tool for any restaurant manager, allowing them to efficiently analyze cashier performance through the lens of tips per hour, a proven indicator of customer satisfaction. By automating the data retrieval and analysis process, the script saves managers substantial time that can be better spent on the floor, enhancing the dining experience.

**Script Workflow**

1. Data Retrieval: The script initiates by fetching the necessary data from the 7shifts API, which contains detailed information about the tip outs and hours worked by cashiers.
2. Data Transformation: It then transforms the nested JSON structure retrieved from the API into a flat structure, making it easier to analyze.
3. Data Filtering: The script filters the data to only include rows where the role is 'Cash/Expedite', thus focusing on the cashiers' data.
4. Data Aggregation: It groups the data by first and last name, summing the hours worked and tips received to get a comprehensive view of each cashier's performance over the specified period.
5. Calculations: A new column, 'tips_per_hour', is calculated to understand the average tips received by each cashier per hour of work.
6. Data Visualization: Finally, the script visualizes this data in a bar chart, offering a graphical representation of each cashier's performance, and saves this chart as a PNG file for easy sharing and reference.
Benefits

**Time Efficiency**
Traditionally, collecting and analyzing this data manually would be a time-consuming task, prone to human error. This script automates the process, delivering accurate results in a fraction of the time, thus freeing up managers to focus on more strategic tasks.

**Customer Satisfaction Insights**
Tips per hour is a significant indicator in the restaurant industry, often correlating with the level of customer service provided. Cashiers with higher tips per hour are likely offering superior service, leaving customers more satisfied. This script helps identify the high performers who might be setting the standard in customer service. At the same time, by identifying cashiers who might be underperforming, managers can focus on providing necessary training and guidance, helping them improve and maintain a high standard of service. It can also be used to set performance benchmarks, encouraging a healthy competitive environment.

**Conclusion**

By utilizing this script, restaurant managers can enhance their decision-making process, foster a culture of continuous improvement, and ultimately, elevate the customer experience. It serves as a valuable tool in the ongoing effort to meet and exceed customer expectations in the highly competitive restaurant industry.

For example, at our Square One location, I can clearly see that Mr. Faidi is doing very well and should perhaps be rewarded, while Ms. Suhanshi could perhaps need extra training and support to ensure she is offering the same level of customer satisfaction
