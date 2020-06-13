import pandas as pd 

# by Default the read_csv() function will take the comma seperated values
# But if I want to add tsv file , then use [set='\t']

# What is a DATAFRAME?
#DataFrame 
#is a 2-dimensional labeled data structure with columns of potentially different types.

df = pd.read_csv('../../data/gapminder.tsv',sep='\t')
print(df) # This will print first and last 5 rows
