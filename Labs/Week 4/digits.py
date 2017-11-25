'''
python program to generate the digits of a number n
Input: n - int
Output: the digits
How to do it?
repeat while possible
	find the last digit and remove it
	print last
'''

import math

def digits():
	
	# read input
	n = int(input("n = "))
	
	# repear while the number is valid
	while n != 0:
		# find the last digit and remove it
		last = n%10
		n = n // 10
		
		# print last
		print(last)
	# end while
	
# end def

digits()
	