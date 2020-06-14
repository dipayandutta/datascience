import pandas as pd 

def main():
    df = pd.read_csv('../../data/gapminder.tsv',sep='\t')
    #loc = row name
    #iloc = row number

    # get the first row
    print (df.loc[0])

    #get the first three rows 
    print(df.loc[:2])

    # get the last row
    number_of_rows = df.shape[0]
    last_row = number_of_rows - 1
    print(df.loc[last_row])

    #print the last row using iloc[-1]
    print(df.iloc[-1])


    #print programmer definded columns and rows first three
    #These is the example of subsetting columns
    print(df[['country','continent','year','lifeExp']].loc[:2].to_string(index=False))

    #print the country name at n th row
    print(df.loc[40,'country'])


    


if __name__ == "__main__":
    main()