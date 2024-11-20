import sqlite3
import pandas as pd

# File path to the SQL query
query_file_path = "sql/report_query.sql"

# Connect to SQLite database
conn = sqlite3.connect("supermarket_sales.db")

# Verify table contents (debug step)
for table in ["Sales", "Product"]:
    print(f"--- {table} Row Count ---")
    row_count = pd.read_sql_query(f"SELECT COUNT(*) AS count FROM {table};", conn)
    print(row_count)

# Load the query from the file
try:
    with open(query_file_path, "r") as file:
        query = file.read()
except FileNotFoundError:
    print(f"Error: Query file not found at {query_file_path}")
    conn.close()
    exit()

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

