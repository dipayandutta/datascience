import pandas as pd 

df = pd.read_csv('../../data/gapminder.tsv',sep='\t')

#print first 5 rows using head() method
print(df.head())

# print last 5 rows using tail() method
print(df.tail())
