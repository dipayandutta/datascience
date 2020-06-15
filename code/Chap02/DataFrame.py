import pandas as pd 

def main():
    # DataFrame can be considerd as -- dictonary of a Series Objects
    scientists = pd.DataFrame({
        'Name':['Rosaline Franklin','William Gosset'],
        'Occupation':['Chemist','Statistician'],
        'Born':['1920-07-25','1876-06-13'],
        'Died':['1958-04-16','1937-10-16'],
        'Age': ['36','61']
    })

    print(scientists)


    scntst = pd.DataFrame(
        data = {
                'Occupation':['Chemist','Statistician'],
                'Born':['1920-07-25','1876-06-13'],
                'Died':['1958-04-16','1937-10-16'],
                'Age': [37,61],
       
    },
    index= ['Rosalin Franklin','William Gossets'],
    columns=['Occupation','Born','Died','Age'])

    print(scntst)

    first_row = scntst.loc['Rosalin Franklin']
    print(first_row)
    print(first_row.index)
    print(first_row.keys)


    ages = scntst['Age']
    print (ages)

    # Get The Basic Status
    print(ages.describe())

    # Get the mean value
    print(ages.mean())

    #print(ages > ages.mean()) Whose age is greater than mean age
    print(ages>ages.mean())

if __name__ == "__main__":
    main()