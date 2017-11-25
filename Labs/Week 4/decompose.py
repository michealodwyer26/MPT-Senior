'''
python program for prime number decomposition of n
Input: n - int
Output: primes with their power
How to?
repeat for each potential prime divisor
	test if is divisor
		extract its power and write them
'''

import math

def primeDecomp():
	# read input
	n = int(input("n = "))
	
	# repeat for potential divisors
	for d in range(2, n+1):
		# test if d is a div of n
		if n%d == 0:
			# find the power of d
			power = 0
			while n%d == 0:
				power = power + 1
				n = n // d
			# end while
			
			# print d and power
			print(d, "**", power)
			
		# end if
		
	# end for
	
# end def
primeDecomp()
