'''
some functions to work with primes.
	isPrime(n) - test if n is prime
	reverse(n) - compute the reverse of n
	allPrimes(n) - gemerate all primes <= n
'''

import math

def isPrime(n):
	
	answer = True
	
	# test 0 and 1
	if n == 0 or n == 1:
		answer = False
		return answer
	# end if
	
	# test even number
	if n!= 2 and n%2 == 0:
		answer = False
		return answer
	# end if
	
	# test if there is a proper odd divisor
	for d in range(3, int(math.sqrt(n))+1, 2):
		if n%d == 0:
			answer = False
		# end if
	# end for
	
	return answer
# end def

def allPrimes(n):
	'''
	print all primes <= n
	print 2
	traverse all odds and test primality
	'''
	
	print(2, end=" ")
	
	for i in range(3, n+1, 2):
		if isPrime(i):
			print(i, end = " ")
		# end if
	# end for
# end def

def allTwinPrimes(n):
	'''
	print all primes <= n
	print 2
	traverse all odds and test primality
	'''
	
	print(2, end=" ")
	
	for i in range(3, n+1, 2):
		if isPrime(i) and isPrime(i+2):
			print(i, i+2)
			
		# end if
	# end for
# end def

def allPalindromePrimes(n):
	'''
	print all primes <= n
	print 2
	traverse all odds and test primality
	'''
	
	print(2, end=" ")
	
	for i in range(3, n+1, 2):
		if isPrime(i) and i == reverse(i):
			print(i, end = " ")
			
		# end if
	# end for
# end def

def reverse(n):
	mirror = 0
	
	while n != 0:
		# get the last digit and remove it
		last = n%10
		n = n // 10
		
		# add last to mirror
		mirror = mirror * 10 + last
		
	# end while
	
	return mirror
	
# end def
	
