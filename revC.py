def dataParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()][0][::-1]
	return data
	
def reverseComp(data):
	revComp = ""
	compDict = {'A':'T','T':'A','C':'G','G':'C'}
	for letter in data:
		revComp += compDict[letter]
	return revComp
	
	
	