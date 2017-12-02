'''
python program to generate all prime numbers less than or equal to n whose mirror is also prime
'''

import math

def isPrime(n):
	ans = True
	
	if n == 0 or n == 1:
		ans = False
		return ans
		
	if n != 0 and n % 2 == 0:
		ans = False
		return ans
	
	
	for d in range(3, int(math.sqrt(n)) + 1, 2):
		if n % d == 0:
			ans = False
			return ans
			
	return ans
	
def allMirrorPrimes(n):
	
	for i in range(n + 1):
		if isPrime(i) and isPrime(reverse(i)):
			print(i, end=" ")
			
def reverse(n):
	
	mirror = 0
	
	while n != 0:
		last = n%10
		n = n // 10
		mirror = mirror * 10 + last
		
	return mirror
	
def main():
	
	n = int(input("n = "))
	allMirrorPrimes(n)
	
main()
	