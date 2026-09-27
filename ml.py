import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

df = pd.read_csv("insurance_data.csv")
df.head()


plt.scatter(df.age,df.bought_insurance,marker='*', color='Red')

from sklearn.model_selection import train_test_split


X_train, X_test, Y_train, Y_test= train_test_split(df[['age']],df[['bought_insurance']],train_size=0.8,random_state=10)

#random_state controls how the rows are randomly divided into training and testing data

#df['bought_insurance'] → Series --> Pandas returns a Series.
#df[['bought_insurance']] --> Pandas returns a DataFrame, not a Series


X_test

X_train


from sklearn.linear_model import LogisticRegression
model= LogisticRegression()

model.fit(X_train, Y_train)

y_predicted = model.predict(X_test)


model.predict_proba(X_test)
