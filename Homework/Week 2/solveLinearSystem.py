'''
This program inputs a1, b1, c1, a2, b2, c2 to solve a linear
system in the form a1*x+b1*y=c1 and a2*x+b2*y=c2.
'''

# function to solve a linear system for x and y
def solveLinearSystem():
	# input a1, b1, c1
	a1, b1, c1 = map(float, input("Please enter a1, b1 and c1 seperated by commas: ").split(","))
	# input a2, b2, c2
	a2, b2, c2 = map(float, input("Please enter a2, b2 and c2 seperated by commas: ").split(","))
	
	# calculate x and y
	x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
	y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)

	# print x and y
	print("x = ", x)
	print("y = ", y)

# end def

solveLinearSystem()