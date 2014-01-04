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


def motifFinder(strandDict):
	subStrings = set()
	strands = list(strandDict.values())
	keySub = strands[0]
	while keySub != "":
		for j in range(1,len(keySub)+1):
			subStrings.add(keySub[:j])
		keySub = keySub[1:]
	subStrings = sorted(list(subStrings), key=len)
	motifs = list(reversed(subStrings))
	
	longest = ""
	for motif in motifs:
		longest = motif
		for strand in strands:
			if strand.find(motif) == -1:
				longest = ""
				break
		if longest != "":
			break
	return longest
			
			
		
	

	
	