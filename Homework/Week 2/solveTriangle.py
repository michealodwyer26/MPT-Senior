'''
This program inputs the sides a, b, c and calculates
the angles, perimeter and the area of the triangle.
'''

# import modules
import math

# function to solve out a triangle
def solveTriangle():
	
	# input float a, b, c
	a = float(input("a = "))
	b = float(input("b = "))
	c = float(input("c = "))
	
	# calculate and print the perimeter
	perimeter = a + b + c
	print("Perimeter = ", perimeter)
	
	# calculate and print the area
	p = (a + b + c) / 2
	area = math.sqrt(p * (p - a) * (p - b) * (p -c))
	print("Area = "area)
	
	# calculate and print the angles A, B, C
	cosA = (b*b + c*c - a*a) / (2 * b * c)
	A = math.degrees(math.acos(cosA)) # math.acos() = cos**-1() or cos to the power of -1
	print("A = ", A)
	
	cosB = (a*a + c*c - b*b) / (2 * a * c)
	B = math.degrees(math.acos(cosB))
	print("B = ", B)
	
	cosC = (a*a + b*b - c*c) / (2 * a * b)
	C = math.degrees(math.acos(cosC))
	print("C = ", C)
	
# end def

solveTriangle()
	
	