'''
This is a program to solve problem REVC from the rosalind.info site.
This program finds the reverse compliment for a DNA strand.
For example: if the DNA strand is AAAACCCGGT, then its reverse
compliment will be ACCGGGTTTT. 
'''

def dataParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()][0]
	return data
	
def reverseComp(data):
	revComp = ""
	compDict = {'A':'T','T':'A','C':'G','G':'C'}
	for letter in data:
		revComp += compDict[letter]
	return revComp[::-1]
	
	
	