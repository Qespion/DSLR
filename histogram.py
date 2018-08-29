#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import argparse

"""
    This file create histogram according to a train csv file.
"""

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
    houses = ['Ravenclaw', 'Hufflepuff', 'Slytherin', 'Gryffindor']
    x1 = []
    i = 6
    for h in headers[6:]:
        np.array(x1.append([[], [], [], []]))
    for d in reader:
        j = 0
        if d['Hogwarts House'] == 'Ravenclaw':
            for i in headers[6:]:
                if d[i] != '':
                    np.array(x1[j][0].append(float(d[i])))
                j += 1
        if d['Hogwarts House'] == 'Hufflepuff':
            for i in headers[6:]:
                if d[i] != '':
                    np.array(x1[j][1].append(float(d[i])))
                j += 1
        if d['Hogwarts House'] == 'Slytherin':
            for i in headers[6:]:
                if d[i] != '':
                    np.array(x1[j][2].append(float(d[i])))
                j += 1
        if d['Hogwarts House'] == 'Gryffindor':
            for i in headers[6:]:
                if d[i] != '':
                    np.array(x1[j][3].append(float(d[i])))
                j += 1
    cols = 3
    gs = gridspec.GridSpec(N // cols + 1, cols)
    fig = plt.figure()
    ax = []
    i = 6
    for n in range(N):
        row = (n // cols)
        col = n % cols
        ax.append(fig.add_subplot(gs[row, col]))
        fig.subplots_adjust(hspace=0.5)
        fig.legend(labels=houses)
        ax[-1].set_title(headers[i], fontsize=15)
        i += 1
        ax[-1].hist(x1[n], histtype='barstacked', label=houses, stacked=True)
        ax[-1].set_xlabel('Grade')
        ax[-1].set_ylabel('Numbers of students')
    plt.show()
