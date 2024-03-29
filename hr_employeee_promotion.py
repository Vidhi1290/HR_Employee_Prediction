# -*- coding: utf-8 -*-
"""HR_EMPLOYEEE_PROMOTION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KQOAJ03qFw1TAJ-RHjh4sdw32PPDXSNP
"""

#importing important libraries:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

#Loading the necessary datasets:
train_df = pd.read_csv('/Users/vidhiwaghela/Desktop/NMIMS MSC IN AI:ML OPS NOTES/MODULE-7/HR EMPLOYEE PROMOTION/train.csv')
test_df = pd.read_csv('/Users/vidhiwaghela/Desktop/NMIMS MSC IN AI:ML OPS NOTES/MODULE-7/HR EMPLOYEE PROMOTION/test.csv')

"""### DATA EXPLORATION PART:

EXPLORING AND EXAMINING THE DATASETS:
"""

#Shape of training dataset:
train_df.shape

#Shape of testing dataset:
test_df.shape

#Comprehensive method to check null values in Training dataset:
train_df.columns
[i for i in train_df.columns if train_df[i].isnull().sum()>0]

#Comprehensive method to check null values in Testing dataset:
test_df.columns
[i for i in test_df.columns if test_df[i].isnull().sum()>0]

# Fill missing values in the education column with the mode value
train_df['education'].fillna(train_df['education'].mode()[0], inplace=True)
test_df['education'].fillna(test_df['education'].mode()[0], inplace=True)

# Fill missing values in the education column with the mode value
train_df['previous_year_rating'].fillna(train_df['previous_year_rating'].mode()[0], inplace=True)
test_df['previous_year_rating'].fillna(test_df['previous_year_rating'].mode()[0], inplace=True)

# Label encode categorical columns
le = LabelEncoder()
train_df['department'] = le.fit_transform(train_df['department'])
test_df['department'] = le.transform(test_df['department'])
train_df['region'] = le.fit_transform(train_df['region'])
test_df['region'] = le.transform(test_df['region'])
train_df['education'] = le.fit_transform(train_df['education'])
test_df['education'] = le.transform(test_df['education'])
train_df['gender'] = le.fit_transform(train_df['gender'])
test_df['gender'] = le.transform(test_df['gender'])
train_df['recruitment_channel'] = le.fit_transform(train_df['recruitment_channel'])
test_df['recruitment_channel'] = le.transform(test_df['recruitment_channel'])

# Drop irrelevant columns
train_df = train_df.drop(['employee_id'], axis=1)
test_df = test_df.drop(['employee_id'], axis=1)

"""### DATA EXPLORATION AND VISUALIZATION:

### EXPERIMENTINGGGGG WITHHH MODELSSS
"""

# Split dataset into X (features) and y (target)
X = train_df.drop(['is_promoted'], axis=1)
y = train_df['is_promoted']

# Split dataset into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the model
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)

# Predict on validation set
y_pred = rfc.predict(X_val)

# Print classification report and confusion matrix
print(classification_report(y_val, y_pred))
print(confusion_matrix(y_val, y_pred))

"""### VALIDATION AND PARAMETER TUNING:"""

# Tune hyperparameters with RandomizedSearchCV
#from sklearn.model_selection import RandomizedSearchCV

#param_distributions = {
    #'n_estimators': [100, 200, 300, 400, 500],
    #'max_depth': [5, 10, 15, 20, 25, 30],
    #'min_samples_split': [2, 5, 10, 15, 20],
    #'min_samples_leaf': [1, 2, 4, 8],
    #'max_features':['sqrt']
#}

#rfc_rs = RandomizedSearchCV(estimator=rfc, param_distributions=param_distributions, cv=5, n_iter=50, random_state=42)
#rfc_rs.fit(X_train, y_train)

# Print best parameters and score
#print(rfc_rs.best_params_)
#print(rfc_rs.best_score_)cl

# Predict on validation set with best parameters
#y_pred_rs = rfc_rs.predict(X_val)

# Print classification report and confusion matrix with best parameters
#print(classification_report(y_val, y_pred_rs))
#print(confusion_matrix(y_val, y_pred_rs))

import pickle

pickle.dump(rfc, open('model.pkl', 'wb'))
