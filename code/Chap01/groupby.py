import pandas as pd 

def main():
    df = pd.read_csv('../../data/gapminder.tsv',sep='\t')

    group_by_year = df.groupby('year')
    group_by_year_lifeExp = group_by_year['lifeExp']

    mean_lifeExp = group_by_year_lifeExp.mean()

    print(mean_lifeExp)


    # In One Line
    print(df.groupby('year')['gdpPercap'].mean())


    #multi_column groupby

    multi_var_groupby = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean()
    print(multi_var_groupby)


    #groupby frequency count()
    #IMPORTANT
    print(df.groupby('continent')['country'].nunique())

if __name__ == "__main__":
    main()