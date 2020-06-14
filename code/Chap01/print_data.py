import pandas as pd 

df = pd.read_csv('../../data/gapminder.tsv',sep='\t')

#print first 5 rows using head() method
# By Default it will print first 5 rows
print(df.head())

# print last 5 rows using tail() method
# By default it will print last 5 rows
print(df.tail())


#print head(n=10)

print(df.head(n=10))

# Get the number of rows and columns
print(df.shape)

#Get the column Names 
print(df.columns)

#Get the datatype of each column
# If it shows object then it is String(most common)
print(df.dtypes)

#Get more information about the data
print(df.info())