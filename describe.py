#!/usr/bin/python

import os
import sys
import math

def get_max(lst):
    lst.sort()
    return (lst[-1])

def get_min(lst):
    lst.sort()
    return (lst[0])

def lower_quartile(lst):
    lst.sort()
    lq = int(round((len(lst) + 1 ) / 4.0 ) - 1)
    return(lst[lq])

def upper_quartile(lst):
    lst.sort()
    uq = int((len(lst) - 1) * 0.75)
    return(lst[uq])

def median(lst):
    n = len(lst)
    lst.sort()
    if n % 2 == 1:
        return lst[n//2]
    else:
        return sum(lst[n//2-1:n//2+1])/2.0

def count(data):
    total = 0
    for _ in data:
        total += 1
    return (total)


def mean(data):
    new_data = []
    for nb in data:
        if nb != '':
            new_data.append(float(nb))
    return (sum(new_data) / float(len(new_data)))

def std(data):
    new_data = []
    for nb in data:
        if nb != '':
            new_data.append(float(nb))
    moy = mean(new_data)
    scd_nb = 0
    for x in new_data:
        scd_nb += (x - moy) ** 2
    return ((scd_nb/len(new_data))**0.5)

def percentil(data, percent):
    new_data = []
    for nb in data:
        if nb != '':
            new_data.append(float(nb))
    if percent == 0.50:
        return (median(new_data))
    elif percent == 0.25:
        return (lower_quartile(new_data))
    elif percent == 0.75:
        return (upper_quartile(new_data))
    elif percent == 0:
        return (get_min(new_data))
    else:
        return (get_max(new_data))
    return 0

def print_data(sel_features, features, data):
    sys.stdout.write("%8s" % ("Count"))
    for ft in sel_features:
        col = features.index(ft)
        sys.stdout.write("%35f" % (count(data[col])))
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write("%8s" % ("Mean"))

    for ft in sel_features:
        col = features.index(ft)
        sys.stdout.write("%35f" % (mean(data[col])))
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write("%8s" % ("Std"))

    for ft in sel_features:
        col = features.index(ft)
        sys.stdout.write("%35f" % (std(data[col])))
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write("%8s" % ("Min"))

    for ft in sel_features:
        col = features.index(ft)
        sys.stdout.write("%35f" % (percentil(data[col], 0)))
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write("%8s" % ("25%"))

    for ft in sel_features:
        col = features.index(ft)
        sys.stdout.write("%35f" % (percentil(data[col], 0.25)))
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write("%8s" % ("50%"))

    for ft in sel_features:
        col = features.index(ft)
        sys.stdout.write("%35f" % (percentil(data[col], 0.5)))
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write("%8s" % ("75%"))

    for ft in sel_features:
        col = features.index(ft)
        sys.stdout.write("%35f" % (percentil(data[col], 0.75)))
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write("%8s" % ("Max"))

    for ft in sel_features:
        col = features.index(ft)
        sys.stdout.write("%35f" % (percentil(data[col], 1)))
    sys.stdout.write("\n")
    sys.stdout.flush()
#end of print_data


def print_describe(fileName):
    data_file = open(fileName, "r")
    data_raw = data_file.read()
    data_file.close()
    lines = data_raw.split('\n');
    data_col = []
    for line in lines:
        if line != "":
            data_col.append(line.split(','))
    features = data_col[0]
    sample_data = data_col[1]
    # print(data_col)
    data = []
    i = 0
    while i < len(features):
        tmp = []
        j = 1
        while j < len(data_col):
            tmp.append(data_col[j][i])
            j += 1
        data.append(tmp)
        i += 1
    i = 1
    while i < len(features):
        tmp_features = []
        sys.stdout.write("%8s" % (""))
        while len(tmp_features) < 4 and i < len(features):
            try:
                float(sample_data[i])
                sys.stdout.write("%35s" % (features[i]))
                tmp_features.append(features[i]);
            except ValueError:
                pass
            i += 1
        sys.stdout.write('\n')
        print_data(tmp_features, features, data)
        sys.stdout.write('\n\n')
    sys.stdout.flush()
#end of print_describe

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print_describe(sys.argv[1])
    elif len(sys.argv) > 2:
        print("Too many arguments")
    else:
        print("You need to give a file as argument")
