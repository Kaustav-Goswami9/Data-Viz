import pandas as pd

data = pd.read_csv('no_encoding_data.csv')

# Selecting the relevant columns (Q12_2 to Q12_10)
q2_columns = ['Q2_2', 'Q2_3', 'Q2_4', 'Q2_5',
              'Q2_6', 'Q2_7', 'Q2_8', 'Q2_9', 'Q2_10']

# Creating a pivot table to count the occurrences of each option in each question
pivot_table = data.groupby('Q18')['voter_category'].value_counts()

print(pivot_table)
