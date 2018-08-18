#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import array
# Still need to create a grid of histogram

def get_notes_slytherin(tab):
	notes = []
	for lines in tab:
		if (lines != ''):
			array = lines.split(',')
			if array[18] != '' and array[1] == 'Slytherin':
				notes.append(float(array[18]))
	return notes

def get_notes_hufflepuff(tab):
	notes = []
	for lines in tab:
		if (lines != ''):
			array = lines.split(',')
			if array[18] != '' and array[1] == 'Hufflepuff':
				notes.append(float(array[18]))
	return notes

def get_notes_Ravenclaw(tab):
	notes = []
	for lines in tab:
		if (lines != ''):
			array = lines.split(',')
			if array[18] != '' and array[1] == 'Ravenclaw':
				notes.append(float(array[18]))
	return notes

def get_notes_Gryffindor(tab):
	notes = []
	for lines in tab:
		if (lines != ''):
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
	minimal = notes[0]
	maximal = notes[-1]
	plt.axis([notes[0], notes[-1], 0, 200])

with open(sys.argv[1], 'r') as my_file:
	title = my_file.readline()
	title = title.split(',')
	file = my_file.read()
	tab = file.split('\n')
	x = array(get_notes_slytherin(tab))
	y = array(get_notes_Gryffindor(tab))
	z = array(get_notes_hufflepuff(tab))
	w = array(get_notes_Ravenclaw(tab))
	get_range(tab)

fig, axes = plt.subplots(nrows=2, ncols=2)
n_bins = 10
ax0, ax1, ax2, ax3 = axes.flatten()
colors = ['#7F0909','#EEE117','#0D6217','#000A90']
ax0.hist([x, y, z, w], n_bins, normed=1, histtype='bar', color=colors, label=colors)
ax0.legend(prop={'size': 10})
ax0.set_title('Flying')

#plt.hist(x, facecolor=slyt_color, alpha = 0.8)
#plt.hist(y, facecolor=gryff_color, alpha = 0.8)
#plt.hist(z, facecolor=huff_color, alpha = 0.8)
#plt.hist(w, facecolor=raven_color, alpha = 0.8)

#ax0.xlabel('Grade')
#ax0.ylabel('Numbers of students')
#labels= ["slytherin","gryffindor", "hufflepuff", "ravenclaw"]
#plt.legend(handles, labels)
#plt.title(title[18])
plt.grid(True)
plt.show()
