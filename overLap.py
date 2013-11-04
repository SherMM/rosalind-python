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
	
def overlap(data,k):
	adjList = []
	strands = data.items()
	for strand in strands:
		strand_name = strand[0]
		end_triplet = strand[1][(len(strand[1])-k):]
		for node in strands:
			node_name = node[0]
			start_triplet = node[1][:k]
			if strand_name != node_name:
				if end_triplet == start_triplet:
					adjList.append((strand_name, node_name))
	return adjList
	
def nodePrinter(data):
	for node in data:
		print node[0],node[1]