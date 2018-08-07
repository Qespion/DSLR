#!/usr/bin/python

import sys
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from numpy import array

mu, sigma = 100, 15
x = np.random.randn(100000)
print(type(x))

def get_notes(tab):
	notes = []
	for lines in tab:
		if (lines != ''):
			array = lines.split(',')
			notes.append(array[6])
	return notes

with open(sys.argv[1], 'r') as my_file:
	my_file.readline()
	file = my_file.read()
	tab = file.split('\n')
	x = array(get_notes(tab))
	print(x)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
# y = mlab.normpdf( bins, mu, sigma)
# l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Grade')
plt.ylabel('Numbers of students')
plt.title("Feature 0")
plt.axis([0, 42, 0, 40000])
plt.grid(False)

plt.show()