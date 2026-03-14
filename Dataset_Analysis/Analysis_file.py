----# To check if a dataset has a categorical data , we can check the data type of column ---

import pandas as pd

def main():
    data = pd.read_csv('File Name .csv')
    categorical_cols=[]

    for col in data.columns:
        if data[col].dtype == 'object':
            categorical_cols.append(col)

    print("categorical column:",categorical_cols)

    for col in categorical_cols:

        unique_values= list(set(data[col]))
        mapping = {}

        for i,value in enumerate(unique_values):
            mapping[value] = i

        data[col] = [mapping[v] for in data[col]]

    print("\mEncoded Dataset:")
    print(data.head())
    print(data.shape)
    print(data.isnull().sum())

if __name__ == "__main__":
    main()
