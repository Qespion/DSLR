#!/usr/bin/python

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import argparse

# array must be of the same size


def sanitize_arr(x1,x2):
    len_x1 = len(x1)
    nb = 0
    while nb < len_x1:
        while x1[nb] == '' or x2[nb] == '':
            del(x1[nb])
            del(x2[nb])
            len_x1 -= 1
        nb += 1
    return (x1, x2)

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
                else:
                    np.array(x1[j][0].append(''))
                j += 1
        if d['Hogwarts House'] == 'Ravenclaw':
            for i in headers[6:]:
                if d[i] != '':
                    np.array(x1[j][1].append(float(d[i])))
                else:
                    np.array(x1[j][1].append(''))
                j += 1
        if d['Hogwarts House'] == 'Slytherin':
            for i in headers[6:]:
                if d[i] != '':
                    np.array(x1[j][2].append(float(d[i])))
                else:
                    np.array(x1[j][2].append(''))
                j += 1
        if d['Hogwarts House'] == 'Hufflepuff':
            for i in headers[6:]:
                if d[i] != '':
                    np.array(x1[j][3].append(float(d[i])))
                else:
                    np.array(x1[j][3].append(''))
                j += 1
    cols = 13
    nb = N * N
    gs = gridspec.GridSpec(nb // cols + 1, cols)
    fig = plt.figure()
    ax = []
    i = 6
    for n in range(nb):
        row = (n // cols)
        col = n % cols
        ax.append(fig.add_subplot(gs[row, col]))
        fig.subplots_adjust(hspace=4)
        fig.legend(labels=houses)
        if col == row:
            l1, l2 = [], []
        else:
            for k in range(len(x1[0])):
                l1, l2 = sanitize_arr(x1[row][k][:], x1[col][k][:])
        ax[-1].scatter(l1, l2, c=colors, label=colors, s=5)
        if (col == 0):
            ax[-1].set_ylabel(headers[row + 6])
        if (row == 12):
            ax[-1].set_xlabel(headers[col + 6])
        ax[-1].set_yticklabels([])
        ax[-1].set_xticklabels([])

    fig.tight_layout()
    plt.show()