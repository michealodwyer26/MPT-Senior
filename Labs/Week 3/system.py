'''
python program to solve a linear system.

Inputs: a1, b1, c1, a2, b2, c3 - the coeficients for the two equations
Output: x, yield
How to do it?
calculate d = a1*b2 - a2*b1, d1 = c1*b2-c2*b1 and d2 = a1*c2-a2*c1
test if d is not zero and calculate x and y with the formulae
otherwise test if d1 is zero and print the correct message
'''

import math

def solveSystem():
	
	# input a1, b1, c1
	a1, b1, c1 = map(float, input("coeficients of equation 1: ").split())
	# input a2, b2, c2
	a2, b2, c2 = map(float, input("coeficients of equation 2: ").split())
	
	# calculate d, d1 and d2
	d = a1*b2 - a2*b1
	d1 = c1*b2 - c2*b1
	d2 = a1*c2 - a2*c1
	
	# test if d is not zero, calculate x, y and print them
	if d != 0:
		x, y = d1/d, d2/d
		print("Solution is: ", x, y)
	else:
		# else test d1 again and print the right message
		if d1 != 0:
			print("No solution")
		else:
			print("Infinit number of solutions")
		#endif
	#endif
# end def

solveSystem()