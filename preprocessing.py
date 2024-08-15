import pandas as pd

data = pd.read_csv('voting-survey_response.csv')
data = data.fillna(-1).replace('Some college', 'College')
data['Age_grp'] = pd.cut(data['age'], bins=[18, 35, 60, 100],
                         labels=['Young', 'Middle', 'Old'])

cat_col = data.select_dtypes(include='object').columns

data.to_csv('modified_data.csv', index=False)

data = pd.read_csv('modified_data.csv')

[print((i, data[i].nunique(), data[i].unique())) for i in data.columns]
