import pandas as pd 

def main():
    df = pd.read_csv('../../data/gapminder.tsv',sep='\t')

    # Print the Name of the Columns
    print (df.columns)

    #print the country column
    print (df['country'])


    #print the first 5 country names
    print(df['country'].head())

    #print without the index numbers
    print(df['country'].head().to_string(index=False))


    #Lookin at three column simultenously
    print(df[['country','continent','year','lifeExp']].head(n=10).to_string(index=False))
if __name__ == "__main__":
    main()