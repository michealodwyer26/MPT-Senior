'''
python program to find the maximum 2 elements of a list with n elements.

Inputs:  n, l
Outputs: max1, max2

How to do it?
 - read n
 - read the list with n elems
 - find max1 and its position
 - find max2 and its position by skipping the index pos1
'''

import math
import listProcessing as listoper

def maxMax():
	# read n and l
	n = int(input("n = "))
	
	l = [] 
	for i in range(n):
		elem = int(input())
		l.append(elem)
		
	# l = list(map(int, input("elems: ").split()))
	
	# initialize max1, pos1
	max1, pos = -1000000, -1
	
	# traverse the list
	
	for i in range(n):
		if l[i] > max1:
			max1, pos1 = l[i], i
		
	# initialize max2 and pos2 
	max2, pos2 = -1000000, -1
	
	for i in range(n):
		if i != pos1 and l[i] > max2:
			max2, pos2 = l[i], i
			
	print("the max 2 elems: ", max1, max2)
	
def maxMax2(l):
	
	# find the max1 and pos1
	
	max1, pos1 = listoper.listMax(l)
	
	# alter the elen of pos1
	l[pos1] = -1000000
	
	max2, pos2 = listoper.listMax(l)
	
	return max1, max2

maxMax()
	