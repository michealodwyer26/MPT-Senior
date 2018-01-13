'''
python program to find the dot product of two lists a and b
and with n elements.
'''

# import modules
import math

def readLists(n):
	# input a list with n elements
	a = [] 
	b = []
	
	print("Enter the values for the list a.")
	for i in range(n):
		# read an element and append it to a
		elem = int(input())
		a.append(elem)
		
	print("Enter the values for the list b.")
	for i in range(n):
		# read an element and append it to b
		elem = int(input())
		b.append(elem)
		
	return a, b
	
def getSum(l):
	s = 0
	n = len(l)
	
	for i in range(n):
		s += l[i]
		
	return s
	
def calculateDotProduct(a, b):
	c = []
	n = len(a)
		
	for i in range(n):
		c.append(a[i]* b[i]) 
	
	s = getSum(c)
	return s
	
def main():
	n = int(input("n = "))
	a, b = readLists(n)
	
	s = calculateDotProduct(a, b)
	
	print(s)
	
main()

