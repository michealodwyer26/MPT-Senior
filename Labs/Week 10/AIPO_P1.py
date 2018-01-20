'''
AIPO P1: Luke Skywalker
Author: Sabin Tabirca
'''

import math

def p1():
	# read and process the first line of input
	line = input("First input line")
	
	l = list(line.split())
	n = int(l[0])
	names = l[1:]
	
	# read and process the second line of input
	line2 = input("Second input line")
	
	l2 = list(line2.split())
	m = int(l2[0])
	relations = l2[1:]
	
	# sort names and relationships
	names.sort()
	relations.sort()
	
	# generate the output messages
	for i in range(n):
		# generate all messages for names[i]
		for j in range(m):
			# generate the output for the names[i] and relations[i]
			print(names[i] + ", I am your " + relations[j] + ".")
			
	
# end def

p1()