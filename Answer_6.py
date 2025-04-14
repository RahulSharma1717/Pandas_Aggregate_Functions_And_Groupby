# Find the total number of  products sold.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

total_products = df['Total_Purchases'].sum()
print(f"Total number of products sold: {total_products}")


"""Output:
Total number of products sold: 1575323
"""

