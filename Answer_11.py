# Create a new dataset which contains the total sale value of each brand.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

new_df = df.groupby('Product_Brand').agg(
    Total_Sales=('Total_Amount', 'sum')
)

print(new_df.round(2))


"""Output:
                   Total_Sales
Product_Brand                 
Adidas             24234757.37
Apple              23964805.29
Bed Bath & Beyond  24275368.20
BlueStar            2992518.55
Coca-Cola          24468668.08
HarperCollins      24331389.40
Home Depot         24157264.12
IKEA               23907496.39
Mitsubhisi          9008943.52
Nestle             24077347.84
Nike               24354963.07
Penguin Books      24170916.45
Pepsi              40420134.10
Random House       24224421.29
Samsung            24692121.44
Sony               24469110.44
Whirepool           9884276.34
Zara               24343747.02
"""