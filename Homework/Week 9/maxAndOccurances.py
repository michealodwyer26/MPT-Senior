'''
python program to find the maximum element in a list and find
the number of occurances in the list
'''

import math

def readList(n):
	# input a list with n elements
	l = []
	
	for i in range(n):
		# read an element and append it to l
		elem = int(input())
		l.append(elem)
		
	return l
	
def maxInList(l):
	# calculate the maximum elem
	max = -1000000
	
	# step 2: traverse the list elems
	n = len(l)
		
	for i in range(n):
		# comapre l[i] vs max
		if l[i] > max:
			max = l[i]
			
	return max
	
def countOccurances(elem, l):
	# calculate how many times elem occurs in l
	count = 0
		
	n = len(l)
	
	for i in range(n):
		# compare l[i] with elem
		if elem == l[i]:
			count += 1
			
	return count
	
	
def main():
	n = int(input("n = "))	
	a = readList(n)
	
	max = maxInList(a)
	occurances = countOccurances(max, a)
	
	print("maximum element in list: ", max)
	print("number of occurances: ", occurances)
	
main()
	