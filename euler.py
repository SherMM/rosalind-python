def CycleMaker(graph, start_node):
	from random import choice
	cycle = [start_node]
	while start_node in graph:
		end_node = choice(graph[start_node])
		graph[start_node].remove(end_node)
		if len(graph[start_node]) == 0:
			graph.pop(start_node)
		cycle.append(end_node)
		start_node = end_node
	return cycle
	
def ContigFinder(graph):
	contigs = []
	degrees = NodeDegreeRangler(graph)
	starts = [node for node in graph if degrees[node][0] != 1 or degrees[node][1] > 1]
	for start in starts:
		while start in graph:
			contig = ContigMaker(graph, degrees, start)
			contigs.append(contig)
	return sorted(contigs)
	
def ContigMaker(graph, degrees, start_node):
	from random import choice
	contig = start_node[0]
	stop = False
	while not stop:
		next_node = choice(graph[start_node])
		in_out_degree = degrees[next_node]
		graph[start_node].remove(next_node)
		if len(graph[start_node]) == 0:
			graph.pop(start_node)
		if next_node in graph:
			if in_out_degree == (1,1):
				contig += next_node[0]
				start_node = next_node
			else:
				contig += next_node
				stop = True
		else:
			contig += next_node
			stop = True
	return contig
												
def InOutDegree(graph, node):
	if node not in graph:
		return False
	out_degree = len(graph[node])
	if out_degree != 1:
		return False
	in_degree = 0
	for k in graph:
		for kmer in graph[k]:
			if kmer == node:
				in_degree += 1
			if in_degree > 1:
				return False
	return in_degree == 1
	
def NodeDegreeRangler(graph):
	from itertools import chain
	in_hits = list(chain.from_iterable(graph.values()))
	degrees = {}
	for node in graph:
		if node not in graph:
			out_degree = 0
		else:
			out_degree = len(graph[node])
		in_degree = in_hits.count(node)
		degrees[node] = degrees.get(node, ()) + (in_degree, out_degree)
		
	for n in set(in_hits):
		if n not in graph:
			out_degree = 0
			in_degree = in_hits.count(n)
			degrees[n] = degrees.get(n, ()) + (in_degree, out_degree)
	return degrees 
		
		
def PathWalk(graph, start_edge):
	graph_copy = graph[:]
	path = []
	starts = [x for x,y in graph_copy]
	if start_edge[0] not in starts:
		return path
	
	if len(graph_copy) > 1:
		path.append(start_edge)
	starts.remove(start_edge[0])
	graph_copy.remove(start_edge)
	out_edges = [edge for edge in graph_copy if edge[0] == start_edge[1]]
	for edge in out_edges:
		path += PathWalk(graph_copy, edge)
	return path
	
def FindStartNodeDict(graph):
	starts = graph.keys()
	for start in starts:
		out_degree = len(graph[start])
		in_degree = sum([1 for x,y in graph.items() if start in y])
		if out_degree > in_degree:
			start_node = start
			return start_node
			
def FindStartNodeTup(graph):
	starts = list(set([x for x,y in graph]))
	for start in starts:
		in_degree = sum([1 for x,y in graph if y == start])
		out_degree = sum([1 for x,y in graph if x == start])
		if out_degree > in_degree:
			return start

def EulerianPath(graph):
	from random import choice
	start_node = FindStartNodeDict(graph)
	edges = [start_node]
	output = []
	while len(edges) != 0:
		top_item = edges[-1]
		if top_item not in graph:
			output.append(edges.pop())
			continue
		out_edges = graph[top_item]
		if len(out_edges) > 0:
			edge = choice(out_edges)
			graph[top_item].remove(edge)
			edges.append(edge)
		elif len(out_edges) == 0:
			output.append(edges.pop())
	return output[::-1]
			
def EulerianCycle(graph):
	from random import choice
	start_node = choice(graph.keys())
	cycle = CycleMaker(graph, start_node)
	while len(graph) != 0:
		start_node = choice([node for node in cycle if node in graph])
		node_index = cycle.index(start_node)
		sub_cycle = CycleMaker(graph, start_node)
		cycle = cycle[node_index:] + cycle[1:node_index+1] + sub_cycle[1:]
	return cycle
	
def GeneralGraph(kmers):
	graph = {}
	for kmer in kmers:
		kmer_suffix = kmer[1:]
		for k in kmers:
			k_prefix = k[:-1]
			if kmer_suffix == k_prefix:
				graph[kmer] = graph.get(kmer, []) + [k]
	return graph
	
def GeneralNodeGraph(kmers):
	graph = {}
	for k in kmers:
		prefix = k[:-1]
		suffix = k[1:]
		graph[prefix] = graph.get(prefix, []) + [suffix] 
	return graph
		
		
def UniStringGraph(k):
	from itertools import product
	nums = [0,1]
	combos = list([p for p in product(nums, repeat=k)])
	subs = []
	for combo in combos:
		c = ''.join([str(i) for i in combo])
		subs.append(c)

	sub_dict = {}
	for sub in subs:
		overlap = sub[1:]
		sub_dict[sub] = sub_dict.get(sub, []) + [overlap + '1', overlap + '0']
	return sub_dict
	
def UniStringNodeGraph(k):
	from itertools import product
	nums = [0,1]
	combos = list([p for p in product(nums, repeat=k-1)])
	subs = []
	for combo in combos:
		c = ''.join([str(i) for i in combo])
		subs.append(c)
		
	sub_dict = {}
	for sub in subs:
		overlap = sub[1:]
		sub_dict[sub] = sub_dict.get(sub, []) + [overlap + '1', overlap + '0']
	return sub_dict
	
def ReadPairGraph(pairs):
	graph = {}
	for pair in pairs:
		pair_suffix = TupleSuffix(pair)
		for p in pairs:
			p_prefix = TuplePrefix(p)
			if pair_suffix == p_prefix and pair != p:
				graph[pair] = graph.get(pair, []) + [p]
	return graph
		
def ReadPairConstruct(pairs, d):
	k = len(pairs[0][0])
	graph = ReadPairGraph(pairs)
	path = EulerianPath(graph)
	strand = path[0][0]
	for t in path[1:]:
		strand += t[0][-1]
		
	second_read_index = len(path) - (k+d)
	for p in path[second_read_index:]:
		strand += p[1][-1]
	return strand
			
def TuplePrefix(pair):
	prefix = (pair[0][:-1], pair[1][:-1])
	return prefix
	
def TupleSuffix(pair):
	suffix = (pair[0][1:], pair[1][1:])
	return suffix
	
	
def UniStringConstruct(k):
	graph = UniStringNodeGraph(k)
	cycle = EulerianCycle(graph)
	strand = ''
	while len(cycle) >= 2:
		edge = cycle[0] + cycle[1][-1]
		strand += edge[0]
		cycle = cycle[1:]
	return strand
	
def StringReconstruct(graph):
	path = EulerianPath(graph)
	string = path[0]
	for sub in path[1:]:
		string += sub[-1]
	return string

def KDComposition(strand, k, d):
	comps = {}
	strand_copy = strand[:]
	comp_range = k+d+k
	while len(strand_copy) >= comp_range:
		start = strand_copy[:k]
		end = strand_copy[k+d:comp_range]
		curr_comp = start + end
		string_rep = '(' + start + '|' + end + ')'
		comps[curr_comp] = comps.get(curr_comp, '') + string_rep
		strand_copy = strand_copy[1:]
	
	lexi_comps = []
	for c in sorted(comps.keys()):
		composition = comps[c]
		lexi_comps.append(composition)
	return lexi_comps
			
def CyclePrinter(cycle):
	return '->'.join(map(str, cycle))
	
def nodeParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	graph = {}
	for nodes in data:
		node = nodes.split(' -> ')
		start = int(node[0])
		end = [int(x) for x in node[1].split(',')]
		graph[start] = graph.get(start, []) + end
	return graph

def nodeTupleParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	graph = []
	for nodes in data:
		node_data = nodes.split(' -> ')
		start_node = int(node_data[0])
		ends = node_data[1].split(',')
		for end in ends:
			end_node = int(end)
			graph.append((start_node, end_node))
	return graph
	
def ReadPairParse(file_name):
	file  = open(file_name, 'r')
	data = [tuple(line.strip().split('|')) for line in file.readlines()]
	return data
	
def string_parse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	graph = {}
	for nodes in data:
		node = nodes.split(' -> ')
		start_node =  node[0]
		end_node = node[1]
		graph[start_node] = [end_node]
	return graph
	
def kmer_parse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	return data
	
def eulerian_path_problem(file_name):
	graph = nodeParse(file_name)
	path = EulerianPath(graph)
	path_string = CyclePrinter(path)
	return path_string
	
def strand_reco_problem(file_name):
	graph = string_parse(file_name)
	strand = StringReconstruct(graph)
	return strand
	
def read_pairs_problem(file_name, d):
	pairs = ReadPairParse(file_name)
	strand = ReadPairConstruct(pairs, d)
	return strand
	
def contig_problem(file_name):
	kmers = kmer_parse(file_name)
	graph = GeneralGraph(kmers)
	return graph
	
def ContigPrinter(contigs):
	for c in contigs:
		print c,
	print