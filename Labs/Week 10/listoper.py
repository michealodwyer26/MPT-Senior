'''
this file contains all the basic and fundamental processing methods with lists
The algorithms are for summation, product, maximum, minimum and counting.
'''

import math

def listInput(n):
	# input a list with n elements
	l = []
	
	for i in range(n):
		# read an element and append it to l
		elem = int(input())
		l.append(elem)
		
	return l
	
def listOutput(l):
	n = len(l)
	
	for i in range(n):
		# print l[i]
		print(l[i], end = " ")
		
def listSum(l):
	# calculate the sum of the list elements
	# step 1: initialize sum
	sum = 0
	# step 2: traverse the list elems
	n = len(l)
	
	for i in range(n):
		# increment sum with l[i]
		sum += l[i]
		
	return sum
	
def listProduct(l):
	# calculate the product of the list elements
	# step 1: initialize prod
	prod = 0
	# step 2: traverse the list elems
	n = len(l)
	
	for i in range(n):
		# increment prod with l[i]
		prod *= l[i]
		
	return prod
	
def listMax(l):
	# calculate the maximum elem and its position
	
	# step 1: initialize max with - infinity
	max, pos = -1000000, -1
	
	# step 2: traverse the list elems
	n = len(l)
	for i in range(n):
		# comapre l[i] vs max
		if l[i] > max:
			max, pos = l[i], i
			
	return max, pos
	
def listMin(l):
	# calculate the minimum elem and its position
	
	# step 1: initialize max with + infinity
	min, pos = 1000000, -1
	
	# step 2: traverse the list elems
	n = len(l)
	for i in range(n):
		# comapre l[i] vs min
		if l[i] < min:
			min, pos = l[i], i
			
	return min, pos
	
def listCount(elem, l):
	# calculate how many times elem occurs in l
	
	# step 1: initialize count = 0
	count = 0
	
	# step 2: traverse the list elems
	
	n = len(l)
	
	for i in range(n):
		# compare l[i] with elem
		if elem == l[i]:
			count += 1
			
	return count
	
def listSearch(elem, i):
	# linear search for elem position in l
	
	# step 1 - initialize pos = -1
	pos = -1
	
	#step 2 - traverse the list
	for i in range(len(l)):
		# compare elem with l[i]
		if elem == l[i]:
			pos = i 
			# break
			
	return pos

def listBubbleSort(l):
	# use 2 similar for loops
	for i in range(len(l)-1):
		for j in range(len(l)-1):
			# compare and swap l[j] and l[j+1]
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
				
	return l
	
