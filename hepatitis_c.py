# -*- coding: utf-8 -*-
"""hepatitis_c.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ujAQa2wKtywVQREyZn1eSgjg7ka4pdqE
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib notebook
# %matplotlib inline

data = pd.read_csv('HepatitisCdata.csv')

data.head()

data.tail()

data.drop('Unnamed: 0', axis=1, inplace=True)

data.head()

data.replace(to_replace=['0=Blood Donor',
                         '0s=suspect Blood Donor',
                         '1=Hepatitis',
                         '2=Fibrosis',
                         '3=Cirrhosis'],
             value=['0','1','2','3','4'], inplace=True)

data.head()

data['Category'].unique()

data.replace(to_replace=['m','f'], value=['0','1'], inplace=True)

data.head()

data.isnull().sum()

data['ALP'].replace(np.NaN, data['ALP'].mode()[0], inplace=True)
data['PROT'].replace(np.NaN, data['PROT'].mode()[0], inplace=True)
data['CHOL'].replace(np.NaN, data['CHOL'].mode()[0], inplace=True)
data['ALT'].replace(np.NaN, data['ALT'].mode()[0], inplace=True)
data['ALB'].replace(np.NaN, data['ALB'].mode()[0], inplace=True)

data.isnull().sum()





num_cols = ['Age', 'Sex', 'ALB', 'ALP', 'ALT', 'AST', 'BIL', 'CHE', 'CHOL', 'CREA', 'GGT', 'PROT', 'Target']
fig, axes = plt.subplots(3, 4, figsize=(15, 15))
axes = axes.flatten()

for ax, col in zip(axes, num_cols):
    sns.histplot(data=data, x=col, ax=ax)

fig=plt.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(data.corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
plt.show()

sns.set(style="whitegrid")
correlation_matrix = data.corr()
fig, ax = plt.subplots(figsize=(12, 10))
plt.title("Correlation Matrix Heatmap", fontsize=16)
sns.heatmap(correlation_matrix, annot=True, annot_kws={"size": 12}, cmap='coolwarm', ax=ax)
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=12)
cbar.set_label('Correlation Strength', rotation=270, fontsize=14, labelpad=15)
plt.show()





x = data.drop(columns='Category', axis=1)
y = data['Category']

x.head()

y.head()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=2)

x.shape, x_train.shape, x_test.shape

y.shape, y_train.shape, y_test.shape

model = LogisticRegression()
model.fit(x_train, y_train)

x_train_prediction = model.predict(x_train)
accuracy_score(x_train_prediction, y_train)



x_test_prediction = model.predict(x_test)
accuracy_score(x_test_prediction, y_test)

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

x_train_prediction = knn.predict(x_train)
accuracy_score(x_train_prediction, y_train)

x_test_prediction = knn.predict(x_test)
accuracy_score(x_test_prediction, y_test)

import pickle
filename = 'hepatitis-c_model.sav'

pickle.dump(model, open(filename, 'wb'))

filename = 'hepatitis-c_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))