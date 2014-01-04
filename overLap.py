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
		
def AdjList(strands):
	adj_dict = {}
	for strand in strands:
		for curr_strand in strands:
			if strand[1:] == curr_strand[:-1]:
				adj_dict[strand] = adj_dict.get(strand, []) + [1]
			else:
				adj_dict[strand] = adj_dict.get(strand, []) + [0]
	return adj_dict
		
def StepicOverlap(strands):
	sorted_strands = sorted(strands)
	adj_dict = AdjList(strands)
	over_lap = []
	for strand in sorted_strands:
		for i in range(len(adj_dict[strand])):
			if adj_dict[strand][i] == 1:
				strand_rep = strand + ' -> ' + strands[i]
				over_lap.append(strand_rep)
	return over_lap
	
def OverLap(strands):
	sorted_strands = sorted(strands)
	over_lap = []
	for strand in sorted_strands:
		for curr_strand in strands:
			if strand[1:] == curr_strand[:-1]:
				strand_rep = strand + ' -> ' + curr_strand
				over_lap.append(strand_rep)
	return over_lap
	
def DeBrujinStrand(strand, k):
	from kmer import sub_parse
	subs = sub_parse(strand, k)
	graph = {}
	for edge in subs:
		node = edge[:-1]
		next_node = edge[1:]
		graph[node] = graph.get(node, []) + [next_node]
	return graph

def DeBrujinKmer(kmers):
	graph = {}
	for edge in kmers:
		prefix = edge[:-1]
		suffix = edge[1:]
		graph[prefix] = graph.get(prefix, []) + [suffix]
	return graph
	
	
def graphPrinter(graph):
	for s,t in sorted(graph.items(), key=lambda x:x[0]):
		strand_rep = s + ' -> ' + ','.join(t)
		print strand_rep
	
def overParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	return data
	
def DeBrujin_problem(file_name):
	data = overParse(file_name)
	k, strand = int(data[0]), data[1]
	graph = DeBrujinStrand(strand, k)
	graphPrinter(graph)
	
def deb_kmers_problem(file_name):
	strands = overParse(file_name)
	graph = DeBrujinKmer(strands)
	graphPrinter(graph)
	