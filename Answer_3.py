# Find the highest sale value.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

highest_sale = df['Total_Amount'].max()
print(f"Highest sale value among the orders: {highest_sale}")


"""Output:
Highest sale value among the orders: 4999.625796
"""