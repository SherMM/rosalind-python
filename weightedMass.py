def monoIsoParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip().split() for line in file.readlines()]
	weightDict = {pair[0] : float(pair[1]) for pair in data}
	return weightDict
	
def proteinWeight(strand, file_name):
	weight = 0
	weightDict = monoIsoParse(file_name)
	for letter in strand:
		weight += weightDict.get(letter, 0)
	return weight