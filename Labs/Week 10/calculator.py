'''
AIPO P2: Calculator
Author: Sabin Tabirca
'''

import math

def p2():
	# make the number list
	numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", \
				"thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen"]
	
	
	# read the input and split it into numbers
	line = input("Input the expression: ")
	l = list(line.split())
	
	nr1 = l[0]
	nr2 = l[2]
	
	# find the number index in the list 
	index1 = numbers.index(nr1)
	index2 = numbers.index(nr2)
	
	# calculate their sum and translate it to a string
	index = index1+index2
	sum = numbers[index]
	
	print(sum)
	
p2()
	
	