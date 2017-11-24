'''
This program calculates interest on an amount of money after 2 years.
The bank offers two interest rates. One is chosed if it is greater
or less than an amount, amount1.
Inputs: rate1, rate2, amount1, initAmount - float
Outputs: out_amount - float
How to do it?
Read the input variables
Check that all variables are positive
If initAmount is less than amount1 use rate1
Else use rate2
Calculate the amount after one year
Calculate the amount after two years
'''

# import modules
import math

# function calculates the amount of money after 2 years
def calculateAmount():
	'''
	calculateAmount calculates interest based on two rates
	The final amount is printed after 2 years
	'''
	# read rate1, rate2, amount1, initAmount
	rate1, rate2 = map(float, input("Please enter the two interest rates: "))
	amount1 = float(input("amount1 = ")
	initAmount = float(input("initAmount = ")
	
	# Calculate the interestRate by comparing with amount1
	if initAmount < amount1:
		interestRate = rate1
	else:
		interestRate = rate2
		
	# end if
	
	# Calculate the finalAmount after 1 year
	interest = amount1 * interestRate
	finalAmount = amount1 + interest
	
	# Calculate the finalAmount after 2 years
	amount2 = finalAmount1
	interest = amount2 * interestRate
	finalAmount = amount2 + interest
	
	print("Final amount after 2 years: ")

# end def