import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

campus_data = pd.read_csv('Placement_Data_Full_Class.csv')
x1 = campus_data.iloc[:,[2,4]].values
x2 = campus_data.iloc[:,[4,7]].values
x3 = campus_data.iloc[:,[2,4,7]].values
y = campus_data.iloc[:,12].values

from sklearn.model_selection import train_test_split
x1_train, x1_test, y_train, y_test = train_test_split(x1, y, test_size = 0.2,random_state = 0)
x2_train, x2_test, y_train, y_test = train_test_split(x2, y, test_size = 0.2,random_state = 0)
x3_train, x3_test, y_train, y_test = train_test_split(x3, y, test_size = 0.2,random_state = 0)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
lr = LinearRegression()

lr.fit(x1_train,y_train)

y_pred1 = lr.predict(x1_test)

#x1- Data includes both ssc_per and hsc_per as features and mba_p as the output variable. In the print the left one is the actual value and the right side is predicted value
#the regression eqn is : mba_p = 0.14(ssc_per)+0.13(hsc_per)+ 44.046

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred1.flatten()})
#print((np.concatenate((y_test.reshape(43,1),  y_pred1.reshape(43,1)),1)))
r2_score(y_test, y_pred1)
print(lr.intercept_)
print(lr.coef_)

#x2- Data includes hsc_per and degree_p as the two features and the same mba_p as output variable
#the regression eqn is : mba_p = 0.13(hsc_per)+0.23(degree_p) + 38.563


from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
lr2 = LinearRegression()
lr2.fit(x2_train,y_train)
y_pred2 = lr2.predict(x2_test)
#print(np.concatenate((y_test.reshape(43,1),  y_pred2.reshape(43,1)),1))
r2_score(y_test, y_pred2)
print(lr2.intercept_)
print(lr2.coef_)

#x3-Data, we use all three: degree_per, hsc_per, ssc_per as the determining features and mba_p as the output needed
#The regression eqn is : mba_p = 0.08(ssc_per)+0.11(hsc_per)+0.18(degree_p) + 37.719

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
lr3 = LinearRegression()
lr3.fit(x3_train,y_train)
y_pred3 = lr3.predict(x3_test)
#print(np.concatenate((y_test.reshape(43,1),  y_pred3.reshape(43,1)),1))
r2_score(y_test, y_pred3)
print(lr3.intercept_)
print(lr3.coef_)
