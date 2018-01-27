'''
AIPO 2012 - Zero Duplicates Problem
Author: Michéal O'Dwyer
'''

import math
	
def hasOccuredBefore(n, l, pos):
	numbersBefore = l[:pos]
	for i in range(len(numbersBefore)):
		if numbersBefore[i] == n:
			return True
			
	return False

def zeroDupes():
	numbers = list(map(int, input("Input list of numbers: ").split()))
	
	for i in range(len(numbers)):
		if not hasOccuredBefore(numbers[i], numbers, i):
			print(numbers[i], end=" ")
		else:
			print("0", end=" ")

zeroDupes()