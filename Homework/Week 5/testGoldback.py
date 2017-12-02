'''
python program to test the Goldback Conjecture for an even number n
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
	
def testGoldback(n):
	for p1 in range(1, n+1):
		for p2 in range(1, n+1):
			if isPrime(p1) and isPrime(p2):
				if p1 + p2 == n:
					return p1, p2
					
	return "False Conjecture"
					
					
def main():
	n = int(input("Please enter an even integer: "))
	p1, p2 = testGoldback(n)
	print(p1, "+", p2, "=", n)
	
main()