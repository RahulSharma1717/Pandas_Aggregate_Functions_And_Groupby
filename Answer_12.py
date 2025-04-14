# Find out the highest average transaction value as per payment method.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

new_df = df.groupby('Payment_Method').agg(
    Average_Transaction=('Total_Amount', 'mean')
)

new_df = new_df.reset_index()
print(new_df)
print("\nHighest average transaction value as per payment method\n", new_df.max())


"""Output:
  Payment_Method  Average_Transaction
0           Cash          1366.912163
1    Credit Card          1369.456358
2     Debit Card          1367.446651
3         PayPal          1366.314212

Highest average transaction value as per payment method
 Payment_Method              PayPal
Average_Transaction    1369.456358
dtype: object
"""


