'''
python program to calculate the max and min of 4 variables a, b, c, d
Inputs: a, b, c, d as int
Outputs: max, min
How to do it?
find max1, min1 of a, b
find max2, min2 of c, d
find max of max1, max2
find min of min1, min2
write max and min
'''

import math

def max4Numbers():
	# read a, b, c, d
	a = int(input("a= "))
	b = int(input("b= "))
	c = int(input("c= "))
	d = int(input("d= "))
	
	# a, b, c, d = map(int, input("Input 4 numbers: ").split())
	# find max1 and min1 of a, b
	if a > b:
		max1, min1 = a, b
	else:
		max1, min1, = b, a
	# endif
	
	# find max2 and min2 of c, d
	if c > d:
		max2, min2 = c, d
	else:
		max2, min2 = d, c
	#endif
	
	# find max of max1, max2
	if max1 > max2:
		max = max1
	else:
		max = max2
	#endif
	
	# find min of min1 and min2
	if min1>min2:
		min = min2
	else:
		min = min1
	
	# print max min
	
	print("max = ", max)
	print("min = ", min)
	
# end def
max4Numbers()