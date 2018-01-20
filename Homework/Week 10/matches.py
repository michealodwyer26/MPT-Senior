'''
AIPO Preliminary Round 2015 - Matches Problem
Author: Michéal O'Dwyer
'''

import math

def matches():
	print("Please enter the input.")
	
	line1 = input().split()
	
	n = int(line1[0])
	width = int(line1[1])
	length = int(line1[2])
	
	match_lengths = []
	
	for i in range(n):
		match_lengths.append(int(input()))
		
	bottom_of_box = (width**2 + length**2) ** 0.5 # calculates the hypotenuse
		
	results = []

	for match_length in match_lengths:
		if match_length <= bottom_of_box:
			results.append("YES")
		else:
			results.append("NO")
			
	for result in results:
		print(result)
	
matches()