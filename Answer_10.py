# Find out average sales for every product category.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

new_df = df.groupby('Product_Category').agg(
    Average_Sales=('Total_Amount', 'mean')
)

print(new_df.round(3))


"""Output:
                  Average_Sales
Product_Category               
Books                  1367.069
Clothing               1368.820
Electronics            1369.737
Grocery                1366.062
Home Decor             1366.481
"""