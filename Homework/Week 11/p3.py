'''
AIPO Preliminary Round Problem 2
Author: Michéal O'Dwyer
'''

def p3():
	input_file = open("input.txt", "tr")
	output_file = open("output.txt", "tw")
	
	line = input_file.readline()
	
	nucleobases = ["A", "T", "C", "G"]
	complementary_bases = ["T", "A", "G", "C"]
	
	complementary = ""
	
	for i in range(len(line)):
		if line[i] == nucleobases[0]:
			complementary += (complementary_bases[0])
			
		elif line[i] == nucleobases[1]:
			complementary += (complementary_bases[1])
			
		elif line[i] == nucleobases[2]:
			complementary += (complementary_bases[2])
			
		elif line[i] == nucleobases[3]:
			complementary += (complementary_bases[3])
	
	output_file.write(str(complementary))
	
	input_file.close()
	output_file.close()
	
p3()