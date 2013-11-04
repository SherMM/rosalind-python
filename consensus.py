def dataParse(file_name):
	data = open(file_name, 'r')
	DNA = [line.strip() for line in data.readlines()]
	dnaDict = {}
	key = ''
	for line in DNA:
		if line[0] == '>':
			key = line[1:]
			dnaDict[key] = ''
		else:
			dnaDict[key] += line
	return dnaDict
	
def countData(data):
	profileDict = {}
	for strand in data.values():
		for i in range(len(strand)):
			profileDict[i] = profileDict.get(i,[]) + [strand[i]]

	countDict = {}
	for index,letters in profileDict.items():
		tempDict = {}
		for letter in set(letters):
			tempDict[letter] = tempDict.get(letter,0) + letters.count(letter)
		countDict[index] = countDict.get(index,tempDict)
	return countDict
	
def profileData(data):
	profileDict = {}
	for strand in data.values():
		for i in range(len(strand)):
			profileDict[i] = profileDict.get(i, []) + [strand[i]]
	
	countDict = {}
	for index,letters in profileDict.items():
		maxLetter = max(letters,key=letters.count)
		maxCount = letters.count(maxLetter)
		countDict[index] = countDict.get(index,()) + (maxLetter, maxCount)
	return countDict
	
	
def consensus(data):
	cons = ''
	for i in range(len(data)):
		cons += data[i][0]
	return cons

def profilePrinter(data):
	letters = ['A','C','G','T']
	for letter in letters:
		print (letter) + ":",
		for i in range(len(data)):
			print data[i].get(letter,0),
		print 
			
			
	

	
	
		
		