import pandas as pd

excel_data_df = pd.read_excel('Gender_Set.xlsx')
df = pd.DataFrame(excel_data_df, columns=['Gender'])

counts = df.value_counts()


def function1():
    print(excel_data_df)
    print(counts)

def function2():
    print('+++++++++++')

def function3():
    print(counts)

if __name__ == '__main__':
    function1() 


