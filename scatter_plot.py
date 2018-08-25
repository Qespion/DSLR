#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
import argparse

"""
	This file create a scatter plot according to a train csv file.
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
	houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
	colors = ['#7F0909', '#000A90', '#0D6217', '#EEE117']
	plt.scatter(x, y, s=area, c=colors, alpha=0.5)
	plt.title('Scatter plot')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.show()