#!/usr/bin/python

import sys
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from numpy import array

# Still need to create a grid of histogram

def get_notes_slytherin(tab):
	notes = []
	for lines in tab:
		array = lines.split(',')
		if array[18] != '' and array[1] == 'Slytherin':
			notes.append(float(array[18]))
	return notes

def get_notes_hufflepuff(tab):
	notes = []
	for lines in tab:
		array = lines.split(',')
		if array[18] != '' and array[1] == 'Hufflepuff':
			notes.append(float(array[18]))
	return notes

def get_notes_Ravenclaw(tab):
	notes = []
	for lines in tab:
		array = lines.split(',')
		if array[18] != '' and array[1] == 'Ravenclaw':
			notes.append(float(array[18]))
	return notes

def get_notes_Gryffindor(tab):
	notes = []
	for lines in tab:
		array = lines.split(',')
		if array[18] != '' and array[1] == 'Gryffindor':
				notes.append(float(array[18]))
	return notes

def get_range(tab):
	notes = []
	for lines in tab:
		if (lines != ''):
			array = lines.split(',')
			if array[18] != '':
					notes.append(float(array[18]))
	notes.sort()
	plt.axis([notes[0], notes[-1], 0, 200])

with open(sys.argv[1], 'r') as my_file:
	title = my_file.readline()
	title = title.split(',')
	file = my_file.read()
	tab = file.split('\n')
	tab.pop()
	x = array(get_notes_slytherin(tab))
	y = array(get_notes_Gryffindor(tab))
	z = array(get_notes_hufflepuff(tab))
	w = array(get_notes_Ravenclaw(tab))
	get_range(tab)

plt.hist(x, facecolor='green', alpha = 0.5)
plt.hist(y, facecolor='red', alpha = 0.5)
plt.hist(z, facecolor='yellow', alpha = 0.5)
plt.hist(w, facecolor='blue', alpha = 0.5)

plt.xlabel('Grade')
plt.ylabel('Numbers of students')
plt.title(title[18])
plt.grid(False)
plt.show()
