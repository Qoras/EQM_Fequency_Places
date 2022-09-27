# Linear Regression On Earthquakes.
#with measured i/p 'Reacter Scale' & 'Frequency/decades'

import pandas as pd
df= pd.read_csv('https://raw.githubusercontent.com/Qoras/EQM_Fequency_Places/main/Earth_Quakes_Measure_Data.csv')
df

import matplotlib.pyplot as plt
plt.scatter(df['Reacter scale'],df['Frequency/decade'])

x=df.iloc[:,1:2].values #x var as 2d i/p
x

y=df.iloc[:,2].values #y var as 1d o/p
y

from sklearn.linear_model import LinearRegression   #Scikit lib for LR.
model=LinearRegression()

model.fit(x,y)     #var fitting
y

model.predict([[2000]]) # prediction with 2d i/p

#Cross verificatioin with, y = mx +c 
m=model.coef_  #slope & model's coeff.
m

C=model.intercept_ # C is constant or model coeficient
C

m*2000+C

plt.scatter(x,y)
plt.plot(x,y_pred,c='orangered')
