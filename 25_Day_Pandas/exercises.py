# -*- coding: utf-8 -*-
"""
Read the hacker_news_pandas.csv file from data directory
Get the first five rows
Get the last five rows
Get the title column as pandas series
Count the number of rows and columns
Filter the titles which contain python
Filter the titles which contain JavaScript
Explore the data and make sense of it
"""
import pandas as pd
from pathlib import Path

file = Path('data\hacker_news_pandas.csv')

data = pd.read_csv(file, encoding='utf-8',sep=',')
#Get the first five rows
print(data.head(5))

#Get the last five rows
print(data.tail(5))

#Get the title column as pandas series

print(pd.Series(data.columns,index=range(len(data.columns))))

#Count the number of rows and columns
print(data.shape)

#Filter the titles which contain python
df_title= data[data['title'].str.contains('python')]
print(df_title)

#Filter the titles which contain JavaScript
df_title= data[data['title'].str.contains('JavaScript')]
print(df_title)