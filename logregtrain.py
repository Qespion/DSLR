# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logregtrain.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: oespion <oespion@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/08/26 14:02:27 by oespion           #+#    #+#              #
#    Updated: 2018/08/29 09:37:44 by oespion          ###   ########.fr        #
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

"""
    This file has trouble to work according to a train csv file.
"""

def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def gradient_9_12(x1):
    learning_rate = 0.0001
    initial_b = 0
    initial_m = 0
    num_iteration = 1000
    r = 0
    points = [[],[]]
    for i in range(1600):
        points[0].append([])
    for i in range(4):
        for nb in x1[9][i]:
            points[i][r][0].append(nb)
            points[i][r][1].append(x1[12][i][r])
            r += 1
            # print(points)
            # exit()
    for r in range(4):
        [b, m] = gradient_descent_runner(points[r], initial_b, initial_m, learning_rate, num_iterations)
        f.write([b, m])

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
    N = len(headers) - 6
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
    print(x1)
    exit()
    gradient_9_12(x1[:])
    f = open("weight.txt","w+")
    f.write("T GROS\n")
    f.close()
