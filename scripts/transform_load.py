import pandas as pd
import sqlite3

# File paths
data_path = "./data/processed/supermarket_sales_cleaned.csv"
ddl_folder = "./sql/ddl/"
db_path = "supermarket_sales.db"

# Load the dataset
df = pd.read_csv(data_path)

# Normalize column names
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

# Create dimension tables and fact table
# Customer Dimension
customer_dim = df[['gender']].drop_duplicates().reset_index(drop=True)
customer_dim['customer_id'] = customer_dim.index + 1  # Assign unique IDs

# Product Dimension
product_dim = df[['product_line']].drop_duplicates().reset_index(drop=True)
product_dim['product_id'] = product_dim.index + 1  # Assign unique IDs

# Sales Fact Table
fact_table = df.merge(customer_dim, on='gender', how='left') \
               .merge(product_dim, on='product_line', how='left')

# Rename columns for clarity
fact_table.rename(columns={'total': 'total_price', 'payment': 'payment_method'}, inplace=True)

# Debugging: Ensure `total_price` exists
if 'total_price' not in fact_table.columns:
    print("Debug: 'total_price' column is missing.")
    print("Available columns:", fact_table.columns)

# Convert 'date' to proper format
fact_table['date'] = pd.to_datetime(fact_table['date'], format='%Y-%m-%d')

# Select only required columns
fact_table = fact_table[['invoice_id', 'customer_id', 'product_id', 'date', 'branch',
                         'city', 'quantity', 'unit_price', 'total_amount', 'payment_method']]

# Debugging: Verify the final fact table structure
print("Fact Table Columns:", fact_table.columns)

# Connect to SQLite
conn = sqlite3.connect(db_path)

# Execute DDL files to create tables
ddl_files = ['customer.sql', 'product.sql', 'sales.sql']
for ddl_file in ddl_files:
    with open(ddl_folder + ddl_file, 'r') as file:
        ddl_script = file.read()
        conn.execute(ddl_script)

# Load data into the tables
customer_dim.to_sql('Customer', conn, if_exists='append', index=False)
product_dim.to_sql('Product', conn, if_exists='append', index=False)
fact_table.to_sql('Sales', conn, if_exists='append', index=False)

# Close connection
conn.close()

print("Data loaded into SQLite database successfully.")
