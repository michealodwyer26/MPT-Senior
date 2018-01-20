'''
program to calculate the average of the positive numbers
find the sum of the positives and then count how many there are.
Find the average if exists
'''

def positives(l):
	# find sum and count of positives 
	
	# stage 1 - initialize sum and count
	sum, count = 0, 0
	
	# stage 2 - traverse the list and test if l[i] is positive
	for i in range(len(l)):
		if l[i] > 0:
			count += 1
			sum += l[i]
			
	# test if any positives
	if count > 0:
		print("average = ", sum/count)
	else:
		print("average does not exist")
		
positives()