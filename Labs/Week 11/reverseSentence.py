'''
word reverse a sentence from "input.txt" to "output.txt"
'''

def wordReverse():
	# open fin and fout
	fin = open("input.txt", "tr")
	fout = open("output.txt", "tw")
	
	# read the sentence into words
	sentence = fin.read()
	
	# remove the full stop 
	sentence = sentence.replace(".", "") # sentence = sentence[:len(sentence)-1]
	
	# split the sentence into words
	words = list(sentence.split())
	
	# reverse the words
	reverseWords = words[::-1]
	
	# make the reversed sentence
	reverse = ""
	for i in range(len(reverseWords)):
		if i < len(reverseWords)-1:
			reverse = reverse + reverseWords[i] + " "
		else:
			reverse = reverse + reverseWords[i] + "."
	
	fout.write(reverse)
	
	fin.close()
	fout.close()
	
wordReverse()