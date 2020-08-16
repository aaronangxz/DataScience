# -*- coding: utf-8 -*-
"""Data Analysis Session 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yhira975IPresHQdWMAZCHXLRC5Cebxw
"""

print("Hello")

from google.colab import files
uploaded=files.upload()

import pandas as pd
df = pd.read_csv('unit05-data.csv')
df

import pandas as pd
df = pd.read_csv('unit05-data.csv')

sg = df[(df['country'] == 'Singapore')]
sg['Estimated incidence (all forms) per 100 000 population'].sum()

import pandas as pd
df = pd.read_csv('unit05-data.csv')

#part 1
year = df[ (df['year'] == 2008)]
print(year['Estimated incidence (all forms) per 100 000 population'].sum())

#part 2
zimbabwe = df[(df['country'] == 'Zimbabwe')]
print(zimbabwe['Estimated incidence (all forms) per 100 000 population'].sum())

import pandas as pd
data = [
        {'name':'Alex','age':20,'salary':1050},
        {'name':'Bob','age':52,'salary':1400},
        {'name':'Cat','age':23,'salary':1690}
]

df = pd.DataFrame(data,columns = ['name','age','salary'])
df.loc[0]

import pandas as pd
data = [
        {'name':'Alex','age':20,'salary':1050},
        {'name':'Bob','age':52,'salary':1400},
        {'name':'Cat','age':23,'salary':1690}
]

df = pd.DataFrame(data,columns = ['name','age','salary'])
df['name']

import pandas as pd
student = ["Anna","Bob","Cass","Darius","Eugene","Felica","Gordon"]
classroom = ["A","A","B","A","B","B","B"]
age = [15,15,16,17,15,18,15]
score =  [80,82,95,70,67,98,85]
data = {"Student": student, "Class":classroom, "Age": age,"Score": score}
df = pd.DataFrame(data)
df

import pandas as pd
student = ["Anna","Bob","Cass","Darius","Eugene","Felica","Gordon"]
classroom = ["A","A","B","A","B","B","B"]
age = [15,15,16,17,15,18,15]
score =  [80,82,95,70,67,98,85]
data = {"Student": student, "Class":classroom, "Age": age,"Score": score}
df = pd.DataFrame(data)
class_score = df.groupby('Class').agg({'Score': ['mean', 'min', 'max']})
class_score

import pandas as pd
student = ["Anna","Bob","Cass","Darius","Eugene","Felica","Gordon"]
classroom = ["A","A","B","A","B","B","B"]
age = [15,15,16,17,15,18,15]
score =  [80,82,95,70,67,98,85]
data = {"Student": student, "Class":classroom, "Age": age,"Score": score}
df = pd.DataFrame(data)
class_score = df.groupby(['Class','Age']).agg({'Score': ['mean', 'min', 'max']})
class_score

import pandas as pd
df = pd.read_csv('unit05-data.csv')

year_2002 = df[(df['year'] == 2002)]
year_2002

import pandas as pd
df = pd.read_csv('unit05-data.csv')

year_not_2002 = df[ (df['year'] != 2002)]
year_not_2002

import pandas as pd
df = pd.read_csv('unit05-data.csv')

years = [2002,2008]
selection = df[df.year.isin(years)]

selection

import pandas as pd
df = pd.read_csv('unit05-data.csv')

years = [2002,2008]
selection = df[~df.year.isin(years)]

selection

import pandas as pd
df = pd.read_csv('unit05-data.csv')

years = [2002,2008]
country = ["Singapore"]
selection = df[df.year.isin(years) & df.country.isin(country)]

selection

import pandas as pd
df = pd.read_csv('unit05-data.csv')
selection = df[df.year.isin(range(2004,2009)) & ~df.country.isin(['Singapore'])]
selection

import pandas as pd
student1 = ["Anna","Bob","Cass","Darius","Eugene","Felica","Gordon"]
classroom1 = ["A","A","B","A","B","B","B"]
age1 = [15,15,16,17,15,18,15]
score1 =  [80,82,95,70,67,98,85]
data1 = {"Student": student1, "Class":classroom1, "Age": age1,"Score": score1}
df1 = pd.DataFrame(data1)

student2 = ["Charlie","James","Ethan"]
classroom2 = ["C","C","C"]
age2 = [16,17,18]
score2 = [95,77,80]
data2 = {"Student": student2, "Class":classroom2, "Age": age2,"Score": score2}
df2 = pd.DataFrame(data2)

df_row = pd.concat([df1, df2], ignore_index=True)
df_row

import pandas as pd
student1 = ["Anna","Bob","Cass","Darius","Eugene","Felica","Gordon"]
classroom1 = ["A","A","B","A","B","B","B"]
age1 = [15,15,16,17,15,18,15]
score1 =  [80,82,95,70,67,98,85]
data1 = {"Student": student1, "Class":classroom1, "Age": age1,"Score": score1}
df1 = pd.DataFrame(data1)

student2 = ["Charlie","James","Ethan"]
classroom2 = ["C","C","C"]
age2 = [16,17,18]
score2 = [95,77,80]
data2 = {"Student": student2, "Class":classroom2, "Age": age2,"Score": score2}
df2 = pd.DataFrame(data2)

df_row = pd.concat([df1, df2], ignore_index=True)
df_row

import pandas as pd
student1 = ["Anna","Bob","Cass","Darius","Eugene","Felica","Gordon"]
classroom1 = ["A","A","B","A","B","B","B"]
age1 = [15,15,16,17,15,18,15]
score1 =  [80,82,95,70,67,98,85]
data1 = {"Student": student1, "Class":classroom1, "Age": age1,"Score": score1}
df1 = pd.DataFrame(data1,columns = ['Student', 'Class', 'Age', 'Score'])

student2 = ["Charlie","James","Ethan"]
classroom2 = ["C","C","C"]
age2 = [16,17,18]
score2 = [95,77,80]
data2 = {"Student": student2, "Class":classroom2, "Age": age2,"Score": score2}
df2 = pd.DataFrame(data2, columns = ['Student', 'Class', 'Age', 'Score'])

df_row = pd.concat([df1, df2], ignore_index=True)

student3 = ["Anna","Bob","Cass","Darius","Eugene","Felica","Gordon","Charlie","James","Ethan"]
id3 = [1,2,3,4,5,6,7,8,9,10]
data3 = {"Student":student3, "id":id3}
df3 = pd.DataFrame(data3,columns = ['Student', 'id'])

df_merge_col = pd.merge(df_row, df3, on="Student")
df_merge_col

import pandas as pd
student1 = ["Anna","Bob","Cass","Darius","Eugene","Felica","Gordon"]
classroom1 = ["A","A","B","A","B","B","B"]
age1 = [15,15,16,17,15,18,15]
score1 =  [80,82,95,70,67,98,85]
data1 = {"Student": student1, "Class":classroom1, "Age": age1,"Score": score1}
df1 = pd.DataFrame(data1,columns = ['Student', 'Class', 'Age', 'Score'])

student2 = ["Charlie","James","Ethan"]
classroom2 = ["C","C","C"]
age2 = [16,17,18]
score2 = [95,77,80]
data2 = {"Student": student2, "Class":classroom2, "Age": age2,"Score": score2}
df2 = pd.DataFrame(data2, columns = ['Student', 'Class', 'Age', 'Score'])

df_row = pd.concat([df1, df2], ignore_index=True)
student3 = ["Anna","Bob","Cass","Darius","Eugene","Felica","Gordon","Charlie","James","Ethan"]
id3 = [1,2,3,4,5,6,7,8,9,10]

data3 = {"Student":student3, "id":id3}
df3 = pd.DataFrame(data3,columns = ['Student', 'id'])

df_merge_col = pd.merge(df_row, df3, on="Student")
df_merge_col

df_merge_col.pivot_table(index="Class", columns="Age", values="Score",fill_value = 0, aggfunc = ["min","max"])

df_merge_col.to_csv (r'df_merge_col.csv', index = False, header=True)

from google.colab import files
uploaded = files.upload()

import pandas as pd
df = pd.read_excel("MissingData.xls")
df

import pandas as pd
df = pd.read_excel("MissingData.xls")
df = df.dropna()
df

import pandas as pd
df = pd.read_excel("MissingData.xls")
df = df.dropna(axis = 1)
df

import pandas as pd
df = pd.read_excel("MissingData.xls",typ = "series")
m = df.Age.mean()
df["Age"] = df["Age"].fillna(m)
df

import pandas as pd
import plotly.express as px

x = [84, 65, 78, 75, 89, 59, 90, 88, 83, 72, 91, 90, 73, 54]
df = pd.DataFrame(x, columns = ['x'])
data = px.histogram(df, x = 'x')
data

import pandas as pd
import plotly.express as px

y1 = [84, 65, 78, 75, 89, 59, 90, 88, 83, 72, 91, 90, 73, 54]
df = pd.DataFrame(y1, columns = ['y1'])
data = px.box(df, y = 'y1')
data

data = px.box(df_merge_col, y = 'Age', x = 'Class')
data

import pandas as pd
import plotly.express as px

foodItemList = ['sushi', 'pizza', 'hamburger', 'fried chicken']
numberList = [2, 5, 4, 3]
df = pd.DataFrame({'Food Item': foodItemList, 'Number of Students': numberList})
data = px.bar(df, x = 'Food Item', y = 'Number of Students')
data

import pandas as pd
import plotly.express as px

foodItemList = ['sushi', 'pizza', 'hamburger', 'fried chicken']
numberList = [2, 5, 4, 3]
df = pd.DataFrame({'Food Item': foodItemList, 'Number of Students': numberList})
data = px.pie(df, names = 'Food Item', values = 'Number of Students')
data