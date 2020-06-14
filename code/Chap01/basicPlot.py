import pandas as pd 
import matplotlib.pyplot as plot

def main():
    df = pd.read_csv('../../data/gapminder.tsv',sep='\t')
    global_yearly_life_exp = df.groupby('year')['lifeExp'].mean()
    global_yearly_life_exp.plot()
    plot.show()

if __name__ == "__main__":
    main()