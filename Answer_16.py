# Find out the total number of transactions for each payment method for every country.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

new_df = df.groupby(['Payment_Method', 'Country']).agg(
    Total_Transactions=('Transaction_ID', 'count')
)

print(new_df)


"""Output:
                          Total_Transactions
Payment_Method Country                      
Cash           Australia               10733
               Canada                  10742
               Germany                 12439
               UK                      14934
               USA                     23079
Credit Card    Australia               13879
               Canada                  13972
               Germany                 15690
               UK                      18026
               USA                     26214
Debit Card     Australia               11283
               Canada                  11134
               Germany                 13137
               UK                      15848
               USA                     23342
PayPal         Australia                8275
               Canada                   8262
               Germany                 10167
               UK                      12590
               USA                     20165
"""