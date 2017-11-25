'''
python program to test if an integer n is prime
Input: n - int
Output: ans - boolean
How to do it?
Read the variable n
Test if n is two
Test if n is one
Test if is multiple of two up until the square root of n
If the number passes all these tests it is prime
'''

# import modules
import math

def isPrime():
	
	# read the variable n
	
	n = int(input("n = "))
	
	ans = True
	
	# test if n is two
	if n == 2:
		ans = True
		
	# test is n is one
	if n == 1:
		ans = False
		
	# test if it has a divisor from 2 to sqrt(n)
	for d in range(2, int(math.sqrt(n)) + 1):
		if n%d == 0:
			ans = False
	
	# print the result ans
	print("Is it prime? ", ans)
	
isPrime()