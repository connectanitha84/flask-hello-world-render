# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:48:48 2022

@author: anuaq
"""
import numpy as np
import pandas as pd
import pickle
df=pd.read_csv('encoded_adult.csv')

X = df.values[:, 0:12]
Y = df.values[:, 12]

from sklearn.model_selection import train_test_split
#Split the Data into Training and Testing sets with test size as 30%
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)


from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators = 100,random_state=0,criterion='entropy') 
clf.fit(X_train, y_train)

y_pred_rf = clf.predict(X_test)
pickle.dump(clf,open('model.pickle','wb'))