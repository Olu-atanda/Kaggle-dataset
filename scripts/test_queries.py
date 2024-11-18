import sqlite3

# Connect to the SQLite database
db_path = "supermarket_sales.db"
conn = sqlite3.connect(db_path)

# Function to query a table and print the results
def query_table(table_name):
    print(f"--- Records from {table_name} ---")
    query = f"SELECT * FROM {table_name} LIMIT 10;"  # Adjust LIMIT as needed
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    
    # Get column names
    columns = [desc[0] for desc in cursor.description]
    print(columns)  # Print column headers
    
    # Print rows
    for row in rows:
        print(row)
    print("\n")

# Query the tables
query_table("Customer")
query_table("Product")
query_table("Sales")

# Close the connection
conn.close()
