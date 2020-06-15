import pandas as pd 

def main():
    read_csv = pd.read_csv('../../data/scientists.csv')
    print(read_csv['Name'])
    print("Mean ==> ",read_csv['Age'].mean())
    print(read_csv[read_csv['Age']>read_csv['Age'].mean()])


    first_half = read_csv[:4]
    second_half= read_csv[4:]

    print(first_half)
    print(second_half)

    print(first_half['Age'].mean())

    print(first_half[['Name','Age']].loc[2])

    print(pd.to_datetime(second_half['Born'],format='%Y-%m-%d'))
if __name__ == "__main__":
    main()