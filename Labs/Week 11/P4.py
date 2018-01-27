'''
AIPO 2018 P4 - Cool Number
Author: Sabin Tabirca
'''

import math

def decomposition(n, b):
	# find base b decomposition of n
	digits = []
	
	while n != 0:
		# divide n by b and place remainder in digits
		rem = n % b
		digits.append(rem)
		
		n = n // b
		
	return digits
	
def p4():
	# read the number n from input.txt
	fin = open("input2.txt", "tr")
	fout = open("output2.txt", "tw")
	
	n = int(fin.read())
	# find the maximum number of 4s in the range 0, 1, ..., n
	max = -1000000
	for i in range(n+1):
		
		# find the base 4 composition of i
		digits = decomposition(i, 5)
		
		# find the numbers of 4s
		nr = digits.count(4)
		
		# compare nr with max
		if max < nr:
			max = nr
		
	# write the result to output.txt
	fout.write(str(max)); print(max)
	
	fin.close()
	fout.close()
	
p4()