'''
This program finds if the real numbers a, b, c form a right angled triangle
Inputs: a, b, c - float
Output: ans - boolean
How to do it?
Input a, b, c as float
Test if the variables are positive
Test if the variables form a triangle
Test if the variables satisfy Pythagoras Theorem
'''

# import modules
import math

# function to find if a, b, c form a Pythagorean triangle
def isPythagoreanTriangle():
	'''
	isPythagoreanTriangle will return a boolean value true if the values
	a, b, c satisfy Pythagoras Theorem
	'''
	
	
	# input a, b, c
	a, b, c = map(float, input("Please enter a, b, c : ").split())
	
	ans = True

	# test if the variables are positive
	if a <= 0 or b <= 0 or c <= 0:
		ans = False
	# end if
		
	# test if the variables form a triangle
	if a >= b+c or b >= a+c or c >= a+b:
		ans = False
	# end if
		
	# Test if the variables satisfy Pythagoras Theorem
	if a**2 + b**2 != c**2:
		ans = False
		
	else:
		ans = True
	# end if
		
	# print the result ans
	print("Forms a right angled triangle = ", ans)
	
# end def

	