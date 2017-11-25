'''
python program to invest amount of euro over a number of years.
Inputs: amount, rate, nrYears
Output: finalAmount
How to do it?
Repeat for nrYears
	calculate the profit and final amount
	print them
'''

import math

def invest():
	# read inputs
	amount = float(input("Initial amount: "))
	rate = float(input("Investment rate: "))
	nrYears = int(input("Number of years: "))
	
	finalAmount = amount
	
	# repeat for nrYears
	for year in range(nrYears):
		# invest for year
		initialAmount = finalAmount
		profit = int(initialAmount * rate * 100) / 100
		finalAmount = int((initialAmount + profit) * 100) / 100
		
		# print this info
		print("Year: ", year, "Initial: ", initialAmount, "Profit: ", profit, "Final: ", finalAmount)
		
	# end for
	
# end def

invest()