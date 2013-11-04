def dataParse(file_name):
	data = open(file_name, 'r')
	DNA = [line.strip() for line in data.readlines()]
	strand1 = DNA[0]
	strand2 = DNA[1]
	return strand1, strand2
	
def findMotif(data):
	dna = data[0]
	motif = data[1]
	motifPos = []
	foundAllMotif = False
	currentMotif = dna.find(motif)
	motifPos.append(currentMotif+1)
	while not foundAllMotif:
		currentMotif = dna.find(motif, currentMotif+1)
		if currentMotif == -1:
			foundAllMotif = True
			break
		else:
			motifPos.append(currentMotif+1)
	return motifPos
		