def dataParse(file_name):
	data = open(file_name, 'r')
	RNA = [line.strip() for line in data.readlines()][0]
	return RNA
	
def sub_parse(string, k):
	strand = string[:]
	subs = []
	while len(strand) >= k:
		sub = strand[:k]
		subs.append(sub)
		strand = strand[k:]
	return subs

def rnaCodeDict(file_name):
	file = open(file_name, 'r')
	code_list = [line.strip().split() for line in file.readlines()]
	codes = {}
	for pair in code_list:
		if len(pair) != 1:
			codes[pair[0]] = codes.get(pair[0],'') + pair[1]
		else:
			codes[pair[0]] = codes.get(pair[0],'')
	return codes	

def rnaToProtein(rna):
	codes = rnaCodeDict("/Users/QuantumIan/downloads/rnaCodes.txt")
	strand = rna[:]
	protein = ''
	subs = sub_parse(rna, 3)
	for sub in subs:
		if codes.get(sub) != '':
			protein += codes.get(sub)
		else:
			break
	return protein
		
		
		
		
	
	