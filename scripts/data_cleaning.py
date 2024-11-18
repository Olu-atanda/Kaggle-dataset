import pandas as pd
import numpy as np

# Step 1: Load the dataset
file_path = 'data/raw/supermarket_sales.csv'
df = pd.read_csv(file_path)

# Step 2: Display basic info and first few rows
print("Initial Data:")
print(df.head())
print("\nData Info:")
print(df.info())

# Step 3: Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Optionally, you can fill or drop missing values based on your analysis:
# For example, you can fill missing numerical columns with the median
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())
df['Unit price'] = df['Unit price'].fillna(df['Unit price'].median())
df['Total'] = df['Total'].fillna(df['Total'].median())
# Drop rows with missing categorical columns (if needed)
df.dropna(subset=['Product line', 'Payment'], inplace=True)

# Step 4: Check for duplicates
duplicates = df.duplicated()
if duplicates.any():
    print("\nRemoving duplicate rows...")
    df = df[~duplicates]
else:
    print("\nNo duplicates found.")

# Step 5: Convert columns to appropriate data types
df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date column is in datetime format
df['Quantity'] = df['Quantity'].astype(int)  # Ensure Quantity is an integer
df['Unit price'] = df['Unit price'].astype(float)  # Ensure Unit price is a float
df['Total'] = df['Total'].astype(float)  # Ensure Total is a float

# Step 6: Rename columns (if needed)
df.rename(columns={
    'Invoice ID': 'invoice_id',
    'Product line': 'product_line',
    'Unit price': 'unit_price',
    'Quantity': 'quantity',
    'Total': 'total_amount',
    'Date': 'date',
    'Time': 'time',
    'Payment': 'payment_method',
    'cogs': 'cost_of_goods_sold',
    'gross margin percentage': 'gross_margin_percentage',
    'gross income': 'gross_income',
    'Rating': 'customer_rating'
}, inplace=True)

# Step 7: Handle outliers (example for quantity and unit price)
# Removing rows where 'Quantity' or 'Unit price' are outliers (e.g., negative values or unreasonable numbers)
df = df[(df['quantity'] > 0) & (df['unit_price'] > 0)]

# Step 8: Check for any inconsistencies (like non-standard values in categorical columns)
# For instance, if payment methods have any unexpected values:
print("\nUnique values in 'payment_method':")
print(df['payment_method'].unique())

# If you find any inconsistencies, you can standardize or correct them
df['payment_method'] = df['payment_method'].replace({'Cash': 'Cash', 'Credit card': 'Credit Card', 'Ewallet': 'E-Wallet'})

# Step 9: Save the cleaned data
cleaned_file_path = 'data/processed/supermarket_sales_cleaned.csv'
df.to_csv(cleaned_file_path, index=False)

print(f"\nData cleaning completed. Cleaned data saved to: {cleaned_file_path}")
