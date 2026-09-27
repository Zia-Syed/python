import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

df = pd.read_csv("insurance_data.csv")
df.head()


plt.scatter(df.age,df.bought_insurance,marker='*', color='Red')

from sklearn.model_selection import train_test_split
