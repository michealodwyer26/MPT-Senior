'''
AIPO Preliminary Round Problem 3
Author: Michéal O'Dwyer
'''

def count(num, l):
	count = 0
	for i in range(len(l)):
		if l[i] == num:
			count += 1
	return count

def isDraw(l, N):
	topContestants = N + 1
	l = l[-topContestants:]

	for num in l:
		timesAppeared = count(num, l)
		if timesAppeared > 1:
			return False
			
	return True
		

def p5():
	input_file = open("input.txt", "tr")
	output_file = open("output.txt", "tw")
	
	N = int(input_file.readline())
	
	P = int(input_file.readline())
	difficulty = list(map(int, input_file.readline().split()))
	
	C = int(input_file.readline())
	expertise = list(map(int, input_file.readline().split()))
	
	noOfProblemsContestantsSolved = []
	possible = False
	
	if N <= C:
		possible = True
	
	expertise.sort()
	difficulty.sort()
	
	for contestant in expertise:
		noSolved = 0
		for problem in difficulty:
			if contestant >= problem:
				noSolved += 1
				
		noOfProblemsContestantsSolved.append(noSolved)
	
	
	possible = isDraw(noOfProblemsContestantsSolved, N)
	
	if possible:
		output_file.write("yes")
	else:
		output_file.write("no")
	
	input_file.close()
	output_file.close()
	
p5()