import pandas as pd
from math import ceil
import matplotlib.pyplot as plt

data = pd.read_csv('modified_data.csv')

cat_3 = ['Q4_1', 'Q4_2', 'Q4_3', 'Q4_4', 'Q4_5', 'Q4_6', 'Q6', 'Q12', 'Q13']
cat_4 = ['Q3_1', 'Q3_2', 'Q3_3', 'Q3_4', 'Q3_5', 'Q3_6',
         'Q7', 'Q9_1', 'Q9_2', 'Q9_3', 'Q9_4']
cat_5 = ['Q8_1', 'Q8_2', 'Q8_3', 'Q8_4', 'Q8_5', 'Q8_6', 'Q8_7', 'Q8_8', 'Q8_9',
         'Q10_1', 'Q10_2', 'Q10_3', 'Q10_4',
         'Q11_1', 'Q11_2', 'Q11_3', 'Q11_4', 'Q11_5', 'Q11_6',
         'Q16_1', 'Q16_2', 'Q16_3', 'Q16_4', 'Q16_5', 'Q16_6', 'Q16_7', 'Q16_8', 'Q16_9', 'Q16_10']

for i, cat in enumerate([cat_3, cat_4, cat_5]):
    plt.figure(figsize=(10, 10))
    for j, col in enumerate(cat):
        plt.subplot(ceil(len(cat)/3), 3, j+1)
        # plot pie chart
        data[col].value_counts().plot.pie(autopct='%1.1f%%')
        plt.title(col)
    plt.tight_layout()
    plt.savefig(f'cat_{i+3}.png')
