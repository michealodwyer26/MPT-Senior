'''
some i/o functions for python
'''

def readWriteList():
	'''
	read a list from list.txt with the first line representing the number of elems 
	and the elems then on sepererate line, and then write to even.txt those elems which are even
	'''
	
	# open fin and font
	fin = open("list.txt", "tr")
	fout = open("even.txt", "tw")
	
	# read n from fin
	n = int(fin.readline())
	
	elems = []
	
	# make the list with n elems read from fin
	for i in range(n):
		elem = int(fin.readline())
		elems.append(elem)
	
	# traverse the list and write to fount only the even elems
	for i in range(n):
		if elems[i] % 2 == 0:
			fout.write(str(elems[i]) + "\n")
		
	# close the files
	fin.close()
	fout.close()
	

def readList():
	'''
	read a list from list.txt with the first number representing the list length
	and all the other numbers on the same line
	'''
	
	# open the file
	fin = open("list.txt", "tr")
	
	# read the number of elems
	n = int(fin.readline())
	
	# read the elems from one line
	elems = list(map(int, fin.readline().strip().split()))
	# close the file
	fin.close()
	
	return elems
	
readWriteList()