# Find out the top sale from each country.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

new_df = df.groupby('Country').agg(
    Top_Sale=('Total_Amount', 'max')
)

print(new_df)


"""Output:
              Top_Sale
Country               
Australia  4997.714637
Canada     4999.171428
Germany    4998.603558
UK         4999.625796
USA        4999.340097
"""