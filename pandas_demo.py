# Pandas: It is a Python library used for data manipulation and analysis.
# It provides data structures and functions needed to manipulate structured data.
#Data will be displayed in tabular form with rows and columns.


from operator import index

import pandas as pd

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
# }

# df = pd.DataFrame(data)
# print(df)

# Series: It is a one-dimensional labeled array capable of holding any data type.
# It is a basic building block of pandas and can be thought of as a single column of data.

#Difference between list and series:
'''Duplicate values:
                    List can have
                    Series can also have 
                    
    Labels:
                    List does not have labels
                    Series has labels (index)
    '''
'''Synatx of series :
pd.Series(data, index, dtype, name, copy)'''

# #Program using series
# temp_series = pd.Series([10, 20, 30, 40])
# print(temp_series)
# #Celsius to Fahrenheit
# fahrenheit = (temp_series * 9/5) + 32
# print(fahrenheit)

# series1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(series1)

# print(series1.describe())

#describe() give instant statistical summary of data in series
''' Automatic Data Alignment:
                    Series automatically aligns data based on labels (index) when performing operations.
                    This means that when you perform operations on two Series, pandas will align the data based on the index labels, even if they are not in the same order.    '''

# w1 = pd.Series([0,20],index=['Monday','Tuesday'])
# w2 = pd.Series([0,20],index=['Tuesday','Monday'])

# print(w1 + w2)

#DataFrame: It is a two-dimensional labeled data structure with columns of potentially different types.
# Syntax of DataFrame:
'''pd.DataFrame(data, index, columns, dtype, copy)
We can create a dataframe from 1)dictionary,
                               2)List of lists,
                               3)Raw Files like csv,excel etc.
                               4)Numpy arrays'''

'''Dictionary example:'''
# data = {
#     'Name':['Sai','Shrutika','Namrata','Swara'],
#     'Marks':[90,85,95,91]
# }
# df=pd.DataFrame(data)
# print(df)

'''List of lists example:'''
# data = [
#     ["Cpp",85],
#     ["C",90],   
#     ["Python",95],
#     ["Java",91]
# ]

# data_marks=pd.DataFrame(data,columns=["Subject","Marks"])
# print(data_marks)

'''Raw files example:'''
# df = pd.read_csv('students.csv')
# print(df)

'''Numpy arrays example:'''
# import numpy as np
# data = np.array([[1, 2, 3], [4, 5, 6]])
# df = pd.DataFrame(data, columns=['A', 'B', 'C'])
# print(df)

'''Functions in pandas:'''
import numpy as np
data = {
    'Name':['Sai','Shrutika','Namrata','Swara'],
    'Marks':[90,np.nan,95,91]
}
df=pd.DataFrame(data,index=[1,2,3,4])
print("ORIGINAL DATAFRAME:")
print(df)

#INFORMATION ABOUT DATAFRAME
print("\n INFORMATION ABOUT DATAFRAME:")
print(df.info())

#Statistical summary of dataframe
print("\n STATISTICAL SUMMARY OF DATAFRAME:")   
print(df.describe())

#Check missing values in dataframe
print("\n CHECK MISSING VALUES IN DATAFRAME:")  
print(df.isnull())

#Fill missing values with average value
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
print(df)

#Filter students scoring above 90
print("\nMARKS > 90")
print(df[df["Marks"]>90])

#Sort by marks in descending order
print("\nSORT BY MARKS IN DESCENDING ORDER:")
print(df.sort_values(by="Marks",ascending=False))

#Select row using LOC
print("\nSELECT ROW USING LOC:")
print(df.loc[2])

#Add new column
df["Result"]=np.where(df["Marks"]>=90,"Pass","Fail")
print("\nADD NEW COLUMN:")
print(df)

#Group by marks and count
print("\nGROUP BY MARKS AND COUNT:")
print(df.groupby("Marks").count())  

#Remove column
new_df = df.drop("Result",axis=1)
print("\nREMOVE COLUMN:")
print(new_df)