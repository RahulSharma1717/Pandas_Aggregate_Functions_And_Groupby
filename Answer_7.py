# Find the city and country with highest frequencies.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

max_counts = df[['City', 'Country']].mode()
print("City and Country with highest frequencies:\n")
for i, row in max_counts.iterrows():
    print(f"City: {row['City']}\nCountry: {row['Country']}")


"""Output:
City and Country with highest frequencies:

City: Chicago
Country: USA
"""