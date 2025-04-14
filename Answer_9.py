# Find the total sales city wise.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

new_df = df.groupby('City').agg(
    Total_Sales=('Total_Amount', 'sum')
)

print(new_df.round(3))


"""Output:
                Total_Sales
City                       
Adelaide        2972902.478
Albuquerque     1213216.631
Albury-Wodonga  3026289.915
Arlington       1169383.651
Atlanta         1229511.633
...                     ...
Wichita         1188115.235
Windsor         2954509.563
Winnipeg        3160659.048
Wollongong      3101859.919
Wuppertal       3043289.001

[130 rows x 1 columns]
"""