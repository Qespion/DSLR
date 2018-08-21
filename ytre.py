#!/usr/bin/python

import sys

with open(sys.argv[1], 'r') as my_file:
	title = my_file.readline()
	title = title.split()
	file = my_file.read()
	tab = file.split('\n')
	for lines in tab:
		lines = lines.split(',')
	print(title)
	print("____")
	r = 50
	while (r < 70):
		print("c pas moi ")