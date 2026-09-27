#Pandas dataframe
import pandas as pd
df= pd.DataFrame([1,2,3])
print(df)


#Pandas Series

numbers = pd.Series([10, 20, 30, 40, 50])

print(numbers)

#dataframe
data = {"Name": ["James", "Sara", "Louise"],"Age": [20, 22, 25],"Marks": [85, 92, 78]}

df = pd.DataFrame(data)

print(df)

#squaring a column

import numpy as np

df = pd.DataFrame({"Marks": [42, 66, 84]})

df["Square"] = np.square(df["Marks"])
print(df)

#dataset read csv file 
df_dia=pd.read_csv("diabetes.csv")
df_dia

#infor of the file
df_dia.info()

#shape: no of columns to rows
df_dia.shape

#Descriptive statistics include those that summarize the central tendency
df_dia.describe

#shows n number of columns
df_dia.head(n=30)

#shows all the columns names
df_dia.columns

df_dia["age_group"]= np.where(df_dia["Age"] < 25,"Young","Adult")# added age_grup column 
df_dia
