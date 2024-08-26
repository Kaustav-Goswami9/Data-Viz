import pandas as pd

data = pd.read_csv('no_encoding_data.csv')

# Selecting the relevant columns (Q15_1 to Q15_4)
q15_columns = ['Q15_1', 'Q15_2', 'Q15_3', 'Q15_4']

# Creating a pivot table to count the occurrences of each option in each question
pivot_table = data[q15_columns].apply(pd.Series.value_counts).fillna(0)

print(pivot_table)
