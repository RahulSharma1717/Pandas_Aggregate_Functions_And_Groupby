# Count the number of transactions per country wise.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

new_df = df.groupby('Country').agg(
    Total_Transactions=('Total_Purchases', 'count')
)

print(new_df)


"""Output:
           Total_Transactions
Country                      
Australia               44170
Canada                  44110
Germany                 51433
UK                      61398
USA                     92800
"""