#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

def get_var(tab, nb):
	notes = []
	tab.pop()
	# print(tab)
	for lines in tab:
		array = lines.split(',')
		if array[nb] != '':
			# print(array[nb])
			notes.append(np.float128(array[nb]))
	# print(notes)
	return notes

# array must be of the same size

with open(sys.argv[1], 'r') as my_file:
	title = my_file.readline()
	title = title.split(',')
	file = my_file.read()
	tab = file.split('\n')
	x = get_var(tab, 8)
	y = get_var(tab, 9)

	print(len(x))
	print(len(y))
	exit(54)
# Plot
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
