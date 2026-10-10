import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pharmacy_sales.csv')
print(df.head())

# Chart 1 - Top Medicines
top = df.groupby('MEDICINE')['QUANTITY'].sum().sort_values(ascending=False)
plt.figure()
top.plot(kind='bar', color='skyblue')
plt.title('Top Selling Medicines by Quantity')
plt.savefig('top_medicines.png')
plt.show()

# Chart 2 - Monthly Growth
monthly = df.groupby('MONTH')['SALE_AMOUNT'].sum()
order = ['Jan','Feb','Mar','Apr','May','Jun','Jul']
monthly = monthly.reindex(order)
plt.figure()
monthly.plot(marker='o', color='green')
plt.title('Monthly Sales Growth')
plt.savefig('monthly_growth.png')
plt.show()

# Chart 3 - Branded vs Generic
type_sale = df.groupby('TYPE')['SALE_AMOUNT'].sum()
plt.figure()
type_sale.plot.pie(autopct='%1.1f%%')
plt.title('Branded vs Generic Revenue')
plt.savefig('branded_vs_generic.png')
plt.show()

# Chart 4 - Revenue by Medicine
rev = df.groupby('MEDICINE')['SALE_AMOUNT'].sum().sort_values(ascending=False)
plt.figure()
rev.plot(kind='bar', color='orange')
plt.title('Revenue by Medicine')
plt.savefig('revenue_medicine.png')
plt.show()
