'''
the euclidian algorithm to find the GCD of 2 integers.
repeat diving first to second while remainder is not zero
gcd - last nonzero remainder
'''

def euclidean(a, b):
	
	# initialize first and second
	first, second = a, b
	
	# repeat while possible
	while True:
		# make a division
		result, remainder = first // second, first % second
		
		# test remainder
		if remainder == 0:
			break
			
		# new division
		first, second = second, remainder
		
	# end while
	
	return second
	
# end def