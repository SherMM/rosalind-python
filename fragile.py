def SharedKmers(x, y, k):
	pairs = []
	x_subs = SubDict(x,k,rev = True)
	y_subs = SubDict(y,k)
	x_keys = [km for km in x_subs.keys() if km in y_subs]
	for k in x_keys:
		for i in x_subs[k]:
			for j in y_subs[k]:
				pairs.append((i,j))
	return pairs	
	
def SubDict(x, k, rev = False):
	from revC import reverseComp
	subDict = {}
	i = 0
	while i <= (len(x) - k):
		sub = x[i:i+k]
		subDict[sub] = list(set(subDict.get(sub,[]) + [i]))
		if rev:
			revc = reverseComp(sub)
			subDict[revc] = list(set(subDict.get(sub,[]) + [i]))
		i += 1
	return subDict

def TwoBreakDistance(P, Q):
	from random import choice
	graph = BreakPointGraphMaker(P, Q)
	num_blocks = BlockCounter(P)
	
	cycles = []
	while len(graph) != 0:
		start = choice(graph.keys())
		cycle = [start]
		while start in graph:
			curr = choice(graph[start])
			graph[start].remove(curr)
			graph[curr].remove(start)
			if len(graph[start]) == 0:
				graph.pop(start)
			if len(graph[curr]) == 0:
				graph.pop(curr)
			cycle.append(curr)
			start = curr
		cycles.append(cycle)	
	return num_blocks - len(cycles)
			
def BlockCounter(genome):
	count = 0
	for g in genome.split(')('):
		g_nodes = g.strip('(').strip(')').split()
		c = list(set([int(x) for x in g_nodes]))
		count += len(c)
	return count		
		
def BreakPointGraphMaker(P, Q):
	p = genome_parse(P)
	q = genome_parse(Q)
	genomes = p + q
	graph = {}
	for gene in genomes:
		graph[gene[0]] = list(set(graph.get(gene[0],[]) + [gene[1]]))
		graph[gene[1]] = list(set(graph.get(gene[1],[]) + [gene[0]]))
	return graph
	
	
def GreedySorting(perm):
	P = permutation_parse(perm)
	revDist = 0
	for i in range(1, len(P)+1):
		if i not in P:
			pos = P.index(-1*i)
		else:
			pos = P.index(i)
		if pos != i - 1:
			switch = [(-1*n) for n in P[i-1:pos+1][::-1]]
			P = P[:i-1] + switch + P[pos+1:]
			revDist += 1
			print permutation_to_string(P)
		if P[i-1] < 0:
			P[i-1] = -1*P[i-1]
			revDist += 1
			print permutation_to_string(P)
	return revDist
	
def BreakpointCounter(P):
	n = 1
	for i in range(len(P)-1):
		if P[i+1] != P[i] + 1:
			n += 1
	return n 

def permutation_to_string(p):
	'''
	converts list-form permutation to 
	string-form permutation.
	'''
	string = '(' + ' '.join([('+' + str(x)) if x > 0 else str(x) for x in p]) + ')'
	return string
	
def genome_parse(G):
	genomes = []
	for g in G.split(')('):
		g_nodes = g.strip('(').strip(')').split()
		c = [int(x) for x in g_nodes]
		for i in range(len(c)-1):
			curr_node = c[i]
			next_node = -1*c[i+1]
			curr_gene = (curr_node, next_node)
			genomes.append(curr_gene)
		genomes.append((c[-1], -1*c[0]))
	return genomes		

def permutation_parse(P):
	p = [int(x) for x in P[1:-1].split()]
	return p	
	
def greedy_sorting_problem(file_name):
	file = open(file_name, 'r')
	p = [line.strip() for line in file.readlines()][0]
	rev_distance = GreedySorting(p)
	return rev_distance
	
def breakpoints_problem(file_name):
	file = open(file_name, 'r')
	perm = [line.strip() for line in file.readlines()][0]
	p = permutation_parse(perm)
	break_points = BreakpointCounter(p)
	return break_points	
	
def two_break_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	P = data[0]
	Q = data[1]
	two_break_distance = TwoBreakDistance(P,Q)
	return two_break_distance
	
def shared_kmers_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	k = int(data[0])
	string1 = data[1]
	string2 = data[2]
	positions = SharedKmers(string1, string2, k)
	return positions
	
def string_import(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	return data	