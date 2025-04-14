# Find the average value of the orders.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

average_value = df['Total_Amount'].mean()
print(f"Average value of the orders: {average_value:.3f}")


"""Output:
Average value of the orders: 1367.687
"""