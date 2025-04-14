# Find the total revenue generated from all transactions.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

total_revenue = df['Total_Amount'].sum()
print("Total revenue generated from all transactions:", round(total_revenue, 3))


"""Output:
Total revenue generated from all transactions: 401978248.894
"""