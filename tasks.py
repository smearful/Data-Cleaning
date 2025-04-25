import pandas as pd
#from datetime import datetime
#import seaborn as sns
#import matplotlib.pyplot as plt

df = pd.read_csv('employee_data.csv')
newdf = df[['emp_id', 'salary', 'department']]

part21 = df[(df['department'] == 'IT')]
part22 = df[(df['age'] > 30)]
part23 = df[(df['salary'] > 60000) & (df['remote'] == True)]
part24 = df[(df['gender'] == 'F') & (df['department'] == 'HR')]
part25 = df[(df['joining_date'] < '2020-01-01')]
            
#print(df)
#print(df.describe())

#print(newdf)
#print(newdf.describe())

#print(part21)
#print(part22)
#print(part23)
#print(part24)
#print(part25)

grouped = df.groupby('department').agg({'salary': ['mean', 'max', 'min']})

print(grouped)

