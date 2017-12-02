'''
python program to test if three numbers a, b, c from a triangle
Inputs: a, b and c - int
Outputs: answer - True / False
How to do it?

Test if one is negative
else test if the triangle inequality holds
a + b > c
'''

import math

def triangle():
	
	# input a, b, c
	a, b, c = map(int, input("Triangle sides: ").split())
	
	answer = True
	# test if any is negative
	if a <= 0 or b <= 0 or c <= 0:
		answer = False
	# end if
	
	# test if any triangle inequality does not hold
	if a >= b+c or c >= a+b:
		answer = False
	#end if
	
	# print answer
	print("Numbers form triangle = ", answer)
	
# end def

triangle()