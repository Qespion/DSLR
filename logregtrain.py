# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logregtrain.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oespion <oespion@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/08/26 14:02:27 by oespion           #+#    #+#              #
#    Updated: 2018/09/03 17:17:16 by oespion          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import argparse

def sigmoid(z):
    return 1.0 / (np.exp(-z))

def sanitize(points):
    for r in range(4):
        len_arr = len(points[0][r])
        nb = 0
        while nb < len_arr:
            while points[0][r][nb] == '' or points[1][r][nb] == '':
                del(points[0][r][nb])
                del(points[1][r][nb])
                len_arr -= 1
            nb += 1
    return (points)

"""
cost & cost gradiant from one vs all page
"""

def cost(theta, X, y):
    predictions = sigmoid(X @ theta)
    predictions[predictions == 1] = 0.999 # log(1)=0 causes error in division
    error = -y * np.log(predictions) - (1 - y) * np.log(1 - predictions);
    return sum(error) / len(y);

def cost_gradient(theta, X, y):
    predictions = sigmoid(X @ theta);
    return X.transpose() @ (predictions - y) / len(y)

def data_9_12(x1):
    r = 0
    points = [[],[],[],[]],[[],[],[],[]]
    for nb in x1[9]:
        points[0][r] = nb
        r += 1
    r = 0;
    for nb in x1[12]:
        points[1][r] = nb
        r += 1
    sanitize(points)
    return points

def y_in_houses(y ,u):
    new_y = np.zeros(len(y))
    i = 0
    for line in y:
        if line == 'Gryffindor' and u == 0:
            new_y[i] = 1
        if line == 'Ravenclaw' and u == 1:
            new_y[i] = 1
        if line == 'Slytherin' and u == 2:
            new_y[i] = 1
        if line == 'Hufflepuff' and u == 3:
            new_y[i] = 1
        i += 1
    return (new_y)

def logistic_regression(x1, y):
    points = data_9_12(x1[:])
    for u in range(4):
        initial_theta = np.zeros(len(y))

def check_file_ext(filename):
    if not filename.endswith('.csv'):
        raise argparse.ArgumentTypeError('wrong filetype or path')
    return filename

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=check_file_ext, help="CSV file path")
args = parser.parse_args()

with open(args.filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    headers = reader.fieldnames
    houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
    colors = ['#7F0909', '#000A90', '#0D6217', '#EEE117']
    x1 = []
    i = 6
    for h in headers[6:]:
            np.array(x1.append([[], [], [], []]))
    for d in reader:
        j = 0
        if d['Hogwarts House'] == 'Gryffindor':
            for i in headers[6:]:
                if d[i] != '':
                    np.array(x1[j][0].append(float(d[i])))
                j += 1
        if d['Hogwarts House'] == 'Ravenclaw':
            for i in headers[6:]:
                if d[i] != '':
                    np.array(x1[j][1].append(float(d[i])))
                j += 1
        if d['Hogwarts House'] == 'Slytherin':
            for i in headers[6:]:
                if d[i] != '':
                    np.array(x1[j][2].append(float(d[i])))
                j += 1
        if d['Hogwarts House'] == 'Hufflepuff':
            for i in headers[6:]:
                if d[i] != '':
                    np.array(x1[j][3].append(float(d[i])))
                j += 1
    logistic_regression(x1[:])
    f = open("weight.csv","w+")
    f.write("T GROS\n")
    f.close()
