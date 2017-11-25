'''
python program to find if integer n is a palindrome
Inputs: n - int
Outputs: ans - boolean
How to do it?
Input n
Initialise mirror_n = 0
Repeat
	Find the last digit of n
	Include the last digit of n in mirror_n
	Remove the last digit of n
Test if n is equal to mirror_n
'''

import math

def isPalindrome():
	
	# input n
	n = int(input("n = "))
	
	# initialaze a variable equal to n to test at the end
	n2 = n
	
	# initialize the mirror of n to 0
	mirror_n = 0
	
	
	while n != 0:
		# find the last digit of n
		last = n%10
		# append last to mirror_n
		mirror_n = mirror_n * 10 + last
		# remove the last digit of n
		n = n//10
	
	if n2 == mirror_n:
		ans = True
		
	else:
		ans = False
		
	print("Is n palindrome? ", ans)
		
isPalindrome()