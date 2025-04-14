# Find the total number of transactions for each shipping method.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

new_df = df.groupby('Shipping_Method').agg(
    Total_Transactions=('Transaction_ID', 'count')
)

print(new_df)


"""Output:
                 Total_Transactions
Shipping_Method                    
Express                       99600
Same-Day                     101541
Standard                      92770
"""