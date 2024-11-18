import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("supermarket_sales.db")

# Verify table contents (debug step)
for table in ["Sales", "Product"]:
    print(f"--- {table} Row Count ---")
    row_count = pd.read_sql_query(f"SELECT COUNT(*) AS count FROM {table};", conn)
    print(row_count)

# Define the revised query
query = """
WITH RevenueSummary AS (
    SELECT 
        f.branch,
        p.product_line,
        SUM(f.total_amount) AS total_revenue,
        SUM(SUM(f.total_amount)) OVER (PARTITION BY f.branch) AS branch_total_revenue
    FROM Sales f
    JOIN Product p ON f.product_id = p.product_id
    GROUP BY f.branch, p.product_line
),
RankedRevenue AS (
    SELECT
        branch,
        product_line,
        total_revenue,
        branch_total_revenue,
        ROUND((total_revenue * 100.0 / branch_total_revenue), 2) AS revenue_percentage,
        RANK() OVER (PARTITION BY branch ORDER BY total_revenue DESC) AS revenue_rank
    FROM RevenueSummary
)
SELECT
    branch,
    product_line,
    total_revenue,
    revenue_percentage,
    revenue_rank
FROM RankedRevenue
ORDER BY branch, revenue_rank;
"""

# Execute the query
try:
    df_result = pd.read_sql_query(query, conn)
    if df_result.empty:
        print("No results returned from the query.")
    else:
        print("Query executed successfully. Displaying results:")
        print(df_result)
except Exception as e:
    print("Error executing query:", e)

# Close the connection
conn.close()
