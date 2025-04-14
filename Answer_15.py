# Find out total number of transactions for each product category in every country.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

new_df = df.groupby(['Product_Category', 'Country']).agg(
    Total_Transactions=('Transaction_ID', 'count')
)

print(new_df)


"""Output:
                            Total_Transactions
Product_Category Country                      
Books            Australia                8165
                 Canada                   7965
                 Germany                  9581
                 UK                      11455
                 USA                     16033
Clothing         Australia                8055
                 Canada                   8175
                 Germany                  9549
                 UK                      11643
                 USA                     15860
Electronics      Australia               11038
                 Canada                  11334
                 Germany                 12575
                 UK                      14786
                 USA                     19632
Grocery          Australia                8743
                 Canada                   8676
                 Germany                 10162
                 UK                      12048
                 USA                     25497
Home Decor       Australia                8169
                 Canada                   7960
                 Germany                  9566
                 UK                      11466
                 USA                     15778
"""