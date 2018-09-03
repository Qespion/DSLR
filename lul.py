#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import scipy.optimize as op
from sklearn.metrics import accuracy_score
import seaborn as sb
from sklearn.metrics import confusion_matrix #Confusion matrix
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
import scipy.io as sio

def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))

#Regularized cost function
def regCostFunction(theta, X, y, _lambda = 0.1):
    m = len(y)
    h = sigmoid(X.dot(theta))
    reg = (_lambda/(2 * m)) * np.sum(theta**2)
    return (1 / m) * (-y.T.dot(np.log(h)) - (1 - y).T.dot(np.log(1 - h))) + reg

#Regularized gradient function
def regGradient(theta, X, y, _lambda = 0.1):
    m, n = X.shape
    theta = theta.reshape((n, 1))
    y = y.reshape((m, 1))
    h = sigmoid(X.dot(theta))
    reg = _lambda * theta /m
    return ((1 / m) * X.T.dot(h - y)) + reg

#Optimal theta
def logisticRegression(X, y, theta):
    result = op.minimize(fun = regCostFunction, x0 = theta, args = (X, y),
                         method = 'TNC', jac = regGradient)
    return result.x
Houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
data = pd.read_csv('resources/dataset_train.csv', header=0)
columns=['Arithmancy','Astronomy','Herbology','Defense Against the Dark Arts','Divination','Muggle Studies',
                                'Ancient Runes','History of Magic','Transfiguration','Potions','Care of Magical Creatures','Charms','Flying']
df = pd.DataFrame(data)
df = df.dropna(axis=0, how='any')

x = df.loc[:][columns].values
y = df.loc[:]['Hogwarts House'].values

m = x.shape[0] #number of examples
n = x.shape[1] #number of features
k = 4 #from 1 to 4

X = np.ones((m, n + 1))
X[:, 1:] = x
all_theta = np.zeros((k, n + 1))

#One vs all
i = 0
for house in Houses:
    #set the labels in 0 and 1
    tmp_y = np.array(y == house, dtype = int)
    optTheta = logisticRegression(X, tmp_y, np.zeros((n + 1,1)))
    all_theta[i] = optTheta
    i += 1
#Predictions
P = sigmoid(X.dot(all_theta.T)) #probability for each house
p = [Houses[np.argmax(P[i, :])] for i in range(X.shape[0])]

print("Test Accuracy ", accuracy_score(y, p) * 100 , '%')