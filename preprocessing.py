import pandas as pd

data = pd.read_csv('voting-survey_response.csv')
data = data.fillna(-1).replace('Some college', 'College')
data['Age_grp'] = pd.cut(data['age'], bins=[18, 35, 60, 100],
                         labels=['Young', 'Middle', 'Old'])

# Mapping for Q1
mapping_q1 = {'Q1': {1: 'Yes', 2: 'No'}}

# Mapping for Q2_1 to Q2_10
mapping_q2 = {i: {1: 'Very important', 2: 'Somewhat important', 3: 'Not so important',
                  4: 'Not at all important'} for i in [f'Q2_{j}' for j in range(1, 11)]}

# Mapping for Q3_1 to Q3_6
mapping_q3 = {i: {1: 'Strongly agree', 2: 'Somewhat agree', 3: 'Somewhat disagree',
                  4: 'Strongly disagree'} for i in [f'Q3_{j}' for j in range(1, 7)]}

# Mapping for Q4_1 to Q4_6
mapping_q4 = {i: {1: 'A significant impact', 2: 'Somewhat of an impact',
                  3: 'Just a slight impact', 4: 'No impact at all'} for i in [f'Q4_{j}' for j in range(1, 7)]}

# Mapping for Q6
mapping_q6 = {'Q6': {1: 'A lot', 2: 'Some', 3: 'Only a few', 4: 'None'}}

# Mapping for Q8_1 to Q8_9
mapping_q8 = {i: {1: 'A lot', 2: 'Some', 3: 'Not much', 4: 'Not at all'}
              for i in [f'Q8_{j}' for j in range(1, 10)]}

# Mapping for Q9_1 to Q9_4
mapping_q9 = {i: {1: 'Very good way', 2: 'Fairly good way', 3: 'Fairly bad way',
                  4: 'Very bad way'} for i in [f'Q9_{j}' for j in range(1, 5)]}

# Mapping for Q10_1 to Q10_4
mapping_q10 = {i: {1: 'Yes', 2: 'No'}
               for i in [f'Q10_{j}' for j in range(1, 5)]}

# Mapping for Q11_1 to Q11_6
mapping_q11 = {i: {1: 'Yes', 2: 'No'}
               for i in [f'Q11_{j}' for j in range(1, 7)]}

# Mapping for Q14
mapping_q14 = {'Q14': {1: 'Very easy', 2: 'Somewhat easy',
                       3: 'Somewhat difficult', 4: 'Very difficult'}}

# Mapping for Q15_1 to Q15_4
mapping_q15 = {i: {1: 'Very confident', 2: 'Somewhat confident', 3: 'Not very confident',
                   4: 'Not at all confident'} for i in [f'Q15_{j}' for j in range(1, 5)]}

# Mapping for Q16_1 to Q16_10
mapping_q16 = {i: {1: 'Yes', 2: 'No'}
               for i in [f'Q16_{j}' for j in range(1, 11)]}

# Mapping for Q18
mapping_q18 = {'Q18': {1: 'Yes', 2: 'No'}}

# Mapping for Q19
mapping_q19 = {'Q19': {1: 'Yes', 2: 'No', 3: 'Unsure/Undecided'}}

# Mapping for Q21
mapping_q21 = {'Q21': {1: 'Yes', 2: 'No', 3: -1}}  # no value for 3

# Mapping for Q23
mapping_q23 = {'Q23': {1: 'Very closely', 2: 'Somewhat closely',
                       3: 'Not very closely', 4: 'Not closely at all'}}

# Mapping for Q24
mapping_q24 = {'Q24': {1: 'Always', 2: 'Sometimes', 3: 'Rarely', 4: 'Never'}}

# Mapping for Q25_1 to Q25_6
mapping_q25 = {i: {1: 'Yes', 2: 'No'}
               for i in [f'Q25_{j}' for j in range(1, 7)]}

# Mapping for Q26_1 to Q26_8
mapping_q26 = {i: {1: 'Agree', 2: 'Disagree'}
               for i in [f'Q26_{j}' for j in range(1, 9)]}

# Mapping for Q29_1 to Q29_10
mapping_q29 = {i: {1: 'Agree', 2: 'Disagree'}
               for i in [f'Q29_{j}' for j in range(1, 11)]}

# Apply mappings
data = data.replace(mapping_q1).replace(mapping_q2).replace(mapping_q3)
data = data.replace(mapping_q4).replace(mapping_q6).replace(mapping_q8)
data = data.replace(mapping_q9).replace(mapping_q10).replace(mapping_q11)
data = data.replace(mapping_q14).replace(mapping_q15).replace(mapping_q16)
data = data.replace(mapping_q18).replace(mapping_q19).replace(mapping_q21)
data = data.replace(mapping_q23).replace(mapping_q24).replace(mapping_q25)
data = data.replace(mapping_q26).replace(mapping_q29)

data.to_csv('no_encoding_data.csv', index=False)

[print((i, data[i].nunique(), data[i].unique())) for i in data.columns]
