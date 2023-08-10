# -*- coding: utf-8 -*-
"""Task.1(Titanic Classification).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CKEa_fi7KGGY4UdG3hFTEg_orndoGxC3
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from google.colab import files
files.upload()

data = pd.read_csv('tested.csv')

data.head()

data.shape

data.info

data.isnull().sum()

data = data.drop(columns='Cabin',axis=1)

data['Age'].fillna(data['Age'].mean(),inplace=True)

print(data['Fare'].mode()[0])

data.isnull().sum()

data.describe()

data['Survived'].value_counts()

data['Sex'].value_counts()

sns.set()

sns.countplot(x='Survived',data=data,)

sns.countplot(x='Sex',data=data,)

sns.countplot(x='Pclass',data=data,)

sns.countplot(x='Embarked',data=data,)

data.replace({'Sex':{'male':1,'female':0},'Embarked':{'s':0,'c':1,'Q':2}},inplace=True)

features=data.drop(columns=['PassengerId','Name','Survived','Ticket'],axis=1)
print(features)

target=data['Survived']
print(target)

f_train,f_test,t_train,t_test=train_test_split(features,target,test_size=0.2,random_state=3)

print(features.shape,f_train.shape,f_test.shape)

model=LogisticRegression()

model.fit(f_train,t_train)