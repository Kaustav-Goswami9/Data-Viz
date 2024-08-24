import pandas as pd

# Load the data
data = pd.read_csv('no_encoding_data.csv')

# Create a pivot table with 'Q18' as the index and 'voter_category' as columns
pivot_table = data.pivot_table(index='Q21', columns='Q24',
                               aggfunc='size', fill_value=0)

# Print the pivoted table
print(pivot_table)
