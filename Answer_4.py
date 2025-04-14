# Find the lowest sale value.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

lowest_sale = df['Total_Amount'].min()
print(f"Lowest sale value among the orders: {lowest_sale}")


"""Output:
Lowest sale value among the orders: 10.00374959
"""