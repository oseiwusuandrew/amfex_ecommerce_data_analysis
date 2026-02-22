import pandas as pd
import matplotlib.pyplot as plt
import os

# Ecommerce Data Analysis Script
# This script loads raw ecommerce data and performs comprehensive analysis
# including data cleaning, descriptive stats, and visualization

# Load the data
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, '../data/Ecommerce_Data.xlsx')
df = pd.read_excel(file_path)

# Save cleaned version for future use
output_csv = os.path.join(script_dir, '../data/ecommerce_cleaned.csv')
df.to_csv(output_csv, index=False)

# Create output folder
output_folder = os.path.join(script_dir, '../outputs_charts')
os.makedirs(output_folder, exist_ok=True)


# 1. DATA UNDERSTANDING
print("1. Data Understanding\n")

# First, let's understand the structure and scope of the dataset
print("Total records:", len(df))
print("\nColumn Names and Data Types:")
print(df.dtypes)
print()

print("Unique product categories:", df['Category'].nunique())
print("Unique regions:", df['Region'].nunique())

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
print("\nDate Range:", df['OrderDate'].min(), "to", df['OrderDate'].max())


# 2. DATA CLEANING
print("\n2. Data Cleaning\n")

# Check for missing values and data quality issues
print("Missing values before cleaning:")
print(df.isnull().sum(), "\n")

# Fill missing values with sensible defaults
df['PaymentMethod'] = df['PaymentMethod'].fillna("Unknown")
df['DeliveryStatus'] = df['DeliveryStatus'].fillna("Unknown")

# Remove duplicates
print("Duplicates before:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Duplicates after:", df.duplicated().sum())

# Fix invalid Quantity values
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df.loc[df['Quantity'] <= 0, 'Quantity'] = 1
df['Quantity'] = df['Quantity'].astype(int)
print("Invalid quantities fixed.")

# 3. DESCRIPTIVE ANALYSIS
print("\n3. Descriptive Analysis\n")

df['TotalAmount ($)'] = pd.to_numeric(df['TotalAmount ($)'], errors='coerce')

print("Average Order Value:", df['TotalAmount ($)'].mean())
print("Minimum Order Value:", df['TotalAmount ($)'].min())
print("Maximum Order Value:", df['TotalAmount ($)'].max())

# Category with highest sales
cat_sales = df.groupby('Category')['TotalAmount ($)'].sum().sort_values(ascending=False)
print("\nCategory with Highest Sales:", cat_sales.idxmax())

# Most common payment method
print("Most Common Payment Method:", df['PaymentMethod'].mode()[0])

# Cancelled or Returned orders
cancel_count = df[df['DeliveryStatus'].str.lower().isin(['cancelled', 'returned'])].shape[0]
print("Cancelled/Returned Orders:", cancel_count)

# Top revenue region
region_sales = df.groupby('Region')['TotalAmount ($)'].sum().sort_values(ascending=False)
print("Region with Highest Revenue:", region_sales.idxmax())


# 4. CUSTOMER & PRODUCT INSIGHTS
print("\n4. Customer & Product Insights\n")

# Top 5 customers by spending
top_customers = df.groupby('CustomerName')['TotalAmount ($)'].sum().sort_values(ascending=False).head(5)
print("Top 5 Customers by Spending:")
print(top_customers, "\n")

# Category with highest average price
avg_price = df.groupby('Category')['TotalAmount ($)'].mean().sort_values(ascending=False)
print("Category with Highest Average Order Value:", avg_price.idxmax())

# Compare sales by region
print("\nTotal Sales by Region:")
print(region_sales, "\n")

# Delivered orders
delivered = df[df['DeliveryStatus'].str.contains("Delivered", case=False)]
print("Total Delivered Orders:", len(delivered))

# Average quantity
print("Average Quantity per Order:", df['Quantity'].mean())


# 5. VISUALIZATION TASKS
print("\n5. Creating Charts...\n")

# Total Sales per Category
cat_sales.plot(kind='bar', color='skyblue', title='Total Sales per Category')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "total_sales_per_category.png"))
plt.close()

# Payment Method Distribution
df['PaymentMethod'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Payment Method Distribution')
plt.ylabel('')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "payment_method_distribution.png"))
plt.close()

# Histogram of Total Amount
df['TotalAmount ($)'].plot(kind='hist', bins=25, title='Histogram of Total Order Value')
plt.xlabel("Total Amount ($)")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "hist_total_amount.png"))
plt.close()

# Monthly Sales Trend
df['Month'] = df['OrderDate'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['TotalAmount ($)'].sum()
monthly_sales.plot(marker='o', title='Monthly Sales Trend')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "monthly_sales_trend.png"))
plt.close()

# Delivery Status by Region
pivot = pd.crosstab(df['Region'], df['DeliveryStatus'])
pivot.plot(kind='bar', stacked=True, title='Delivery Status by Region')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "delivery_status_by_region.png"))
plt.close()

print("All charts saved in outputs_charts folder.")


# 6. BUSINESS INSIGHTS
print("\n6. Business Insights\n")

# Top 3 categories to invest in (based on sales & low returns)
returned = df['DeliveryStatus'].str.lower().str.contains("return")
total_sales = df.groupby('Category')['TotalAmount ($)'].sum()
returned_sales = df[returned].groupby('Category')['TotalAmount ($)'].sum().reindex(total_sales.index).fillna(0)
score = (total_sales - returned_sales).sort_values(ascending=False)
print("Top 3 Categories to Invest In:")
print(score.head(3), "\n")

# Payment method with highest avg order value
payment_avg = df.groupby('PaymentMethod')['TotalAmount ($)'].mean().sort_values(ascending=False)
print("Payment Method with Highest Avg Order Value:", payment_avg.idxmax())

# Region delivery success rate
delivered_rate = df[df['DeliveryStatus'].str.contains('deliv', case=False)]
region_success = delivered_rate.groupby('Region').size() / df.groupby('Region').size()
print("\nDelivery Success Rates by Region:")
print(region_success, "\n")

# Print top performing category for strategic focus
top_category = cat_sales.idxmax()
print(f"Recommendations based on analysis:")
print(f"- Top performing category: {top_category} (${cat_sales.max():,.2f})")
print(f"- Best payment method: {payment_avg.idxmax()} (avg ${payment_avg.max():,.2f})")
print(f"- Regions needing attention: {region_success[region_success < region_success.mean()].index.tolist()}\n")
