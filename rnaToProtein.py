def dataParse(file_name):
	data = open(file_name, 'r')
	RNA = [line.strip() for line in data.readlines()][0]
	return RNA

def rnaCodeDict(file_name):
	file = open(file_name, 'r')
	codes = [line.strip().split() for line in file.readlines()]
	codeDict = {}
	for pair in codes:
		codeDict[pair[0]] = pair[1]
	return codeDict

codes = rnaCodeDict("/Users/QuantumIan/downloads/rnaCodes.txt")		

def rnaToProtein(rna):
	strand = rna
	protein = ''
	stopped = False
	while not stopped:
		if len(strand) < 3:
			group = strand
		else:
			group = strand[:3]
		if codes[group] == 'Stop':
			stopped = True
			break
		protein += codes[group]
		strand = strand[3:]
	return protein

		
		
		
		
	
	