import pandas as pd
import matplotlib.pyplot as plt

# Load the DataFrame
df = pd.read_csv("C:/Users/DOREEN WANYAMA/Downloads/sales_data_sample.csv", encoding='ISO-8859-1')


# Print detailed information about the DataFrame
print("\nDetailed Information about the DataFrame:")
df.info()

# Find null values and print them with respective columns
null_counts = df.isnull().sum()
null_columns = null_counts[null_counts > 0].index.tolist()

print(null_counts)
print(null_columns)

# Print the PRODUCTLINE column to check its contents

print(df["PRODUCTLINE"].head())

# Group by PRODUCTLINE and sum the SALES column
product_sales = df.groupby('PRODUCTLINE')['SALES'].sum()

# Sort the result to get the top 5 products with the most sales
top_5_products = product_sales.sort_values(ascending=False).head(5)

# Print the top 5 products with the most sales
print("\nTop 5 products with the most sales:")
print(top_5_products)

# Top 5 territories with the most orders
orders_by_territory = df.groupby('TERRITORY')['ORDERNUMBER'].count()
top_5_orders_by_territory = orders_by_territory.sort_values(ascending=False).head(5)
print("\nTop 5 territories with the most orders:")
print(top_5_orders_by_territory)

# Top 5 territories with the most sales
sales_by_territory = df.groupby('TERRITORY')['SALES'].sum()
top_5_sales_by_territory = sales_by_territory.sort_values(ascending=False).head(5)
print("\nTop 5 territories with the most sales:")
print(top_5_sales_by_territory)

# Top 5 cities with the most orders
orders_by_city = df.groupby('CITY')['ORDERNUMBER'].count()
top_5_orders_by_city = orders_by_city.sort_values(ascending=False).head(5)
print("\nTop 5 cities with the most orders:")
print(top_5_orders_by_city)

# Top 5 cities with the most sales
sales_by_city = df.groupby('CITY')['SALES'].sum()
top_5_sales_by_city = sales_by_city.sort_values(ascending=False).head(5)
print("\nTop 5 cities with the most sales:")
print(top_5_sales_by_city)

# Cities with less sales
sales_by_city = df.groupby('CITY')['SALES'].sum()
top_5_sales_by_city = sales_by_city.sort_values(ascending=True).head(5)
print("\nTop 5 cities with the most sales:")
print(top_5_sales_by_city)

# Group by MONTH_ID and sum the SALES column
sales_by_month = df.groupby('MONTH_ID')['SALES'].sum()
print(sales_by_month)

# Find the month with the most sales
most_sales_month = sales_by_month.idxmax()
most_sales_value = sales_by_month.max()

# Find the month with the least sales
least_sales_month = sales_by_month.idxmin()
least_sales_value = sales_by_month.min()

print(f"Month with the most sales: {most_sales_month} (Sales: {most_sales_value})")
print(f"Month with the least sales: {least_sales_month} (Sales: {least_sales_value})")

# finding the top customers 
# Group by CUSTOMERNAME and PHONE, then sum the SALES
customer_sales = df.groupby(['CUSTOMERNAME', 'PHONE'])['SALES'].sum().reset_index()

# Sort the customers by the total sales in descending order
customer_sales_sorted = customer_sales.sort_values(by='SALES', ascending=False)

# Select the top 5 customers
top_5_customers = customer_sales_sorted.head(5)

# Print the top 5 customers with most sales
print("\nTop 5 Customers with Most Sales:")
print(top_5_customers)


# Create subplots for both visualizations
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Plot total sales by city
sales_by_city.head(10).plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_title('Total Sales by City (Top 10)')
ax1.set_xlabel('City')
ax1.set_ylabel('Total Sales')
ax1.set_xticklabels(sales_by_city.head(10).index, rotation=45)

# Plot total sales by month
sales_by_month.plot(kind='line', ax=ax2, marker='o', color='green')
ax2.set_title('Total Sales by Month')
ax2.set_xlabel('Month')
ax2.set_ylabel('Total Sales')
ax2.set_xticks(range(1, 13))
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.tight_layout()
plt.show()

