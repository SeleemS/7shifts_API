**Prep Cost Analysis Script**

**Overview**

This script is a great resource for cost managers and chefs, aiding them in a detailed analysis of kitchen prep costs broken down by individual items on a weekly basis. By providing a week-by-week comparison, it enables a clear understanding of the fluctuating costs, allowing for more informed decision-making regarding menu pricing, inventory management, and other operational aspects. Moreover, the automation of data retrieval and analysis streamlines the managerial workflow, thus saving valuable time that can be invested in enhancing the dining experience.

_Note:_ For a tool such as this one to work efficiently, prep shifts must be scheduled **per item** instead of general "Prep" shifts. Prep cooks must punch in before beginning that specific item, and punch out after being completely done. Utilizing 7shifts and 7punches in this way allows cost manager a more in depth insight on where time is **actually** being spent. This also allows for a more accurate labour cost per unit, which is especially useful for franchises which are selling their prepped items at a markup.

**Script Workflow:**

1. Data Retrieval: Initially, the script automatically fetches data from the 7shifts API, which contains comprehensive information about the roles, hours worked, and pay for each kitchen item.
2. Data Transformation: The retrieved data, which is in a nested JSON format, is transformed into a more manageable structure, facilitating easier analysis.
3. Data Aggregation: It then aggregates the data based on roles and calculates the total hours worked and the total pay for each role in the specified week.
4. Data Comparison: The script compares the data week by week, allowing for a detailed analysis of variations in prep costs for each item.
5. Data Visualization: Subsequently, the script visualizes the data through bar charts, presenting a clear graphical representation of the total hours and total pay for each role, week by week, and saving these charts as PNG files for easy reference and sharing.

**Benefits:**

_Cost Efficiency and Budget Management_  
Analyzing kitchen prep costs item by item allows for a more granulated view of the budget, facilitating better management and cost-efficiency. Managers can identify areas where costs might be escalating and take timely corrective actions.

_Operational Insights_  
By comparing data on a week-by-week basis, the script provides valuable insights into the operational dynamics of the kitchen. Managers can identify patterns and trends, helping to optimize inventory management, workforce allocation, and menu pricing.

_Resource Allocation_  
Identifying the time and resources spent on each kitchen item allows for better resource allocation, ensuring that the kitchen operates at optimum efficiency without compromising on quality.
