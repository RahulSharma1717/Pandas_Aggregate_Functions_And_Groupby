# Find the average rating given by customers.

import pandas as pd

df = pd.read_csv('retail_data.csv')
#pd.set_option('display.max_columns', None)

average_rating = df['Ratings'].mean()
print(f"Average rating given by customers: {average_rating:.3f}")


"""Output:
Average rating given by customers: 3.162
"""