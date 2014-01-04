def OverlapAlignment(v,w):
	s = [[0 for num in range(len(w)+1)] for num in range(len(v)+1)]
	backtrack = [[None for num in range(len(w)+1)] for num in range(len(v)+1)] 
	
	max_node = -1*float("inf")
	max_pos = (0,0)
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			down = s[i-1][j] - 2
			right = s[i][j-1] - 2
			if v[i-1] == w[j-1]:
				diagonal = s[i-1][j-1] + 1
			else:
				diagonal = s[i-1][j-1] - 2
			s[i][j] = max([down, right, diagonal])
			if i == len(v):
				curr_max = s[i][j]
				if curr_max > max_node:
					max_node = curr_max
					max_pos = (i,j)
			if s[i][j] == diagonal:
				backtrack[i][j] = '\\\\'
			elif s[i][j] == right:
				backtrack[i][j] = 'R---'
			else:
				backtrack[i][j] = 'D---'
	return s, backtrack, max_node, max_pos
	
def OverlapOutput(backtrack, s1, s2, max_pos):
	string1 = ''
	string2 = ''
	i = max_pos[0]
	j = max_pos[1]
	while j != 0 and i != 0:
		if backtrack[i][j] == 'D---':
			string2 += '-'
			string1 += s1[i-1]
			i = i - 1
		elif backtrack[i][j] == 'R---':
			string1 += '-'
			string2 += s2[j-1]
			j = j - 1
		else:
			string1 += s1[i-1]
			string2 += s2[j-1]
			i = i - 1
			j = j - 1
	return string1[::-1], string2[::-1]		
	

def FitAlignment(v, w):
	s = [[0 for num in range(len(w)+1)] for num in range(len(v)+1)]
	backtrack = [[0 for num in range(len(w)+1)] for num in range(len(v)+1)]
	for i in range(len(v)+1):
		s[i][0] = 0
		backtrack[i][0] = 'D---'
	for j in range(1, len(w)+1):
		s[0][j] = -1*j
		backtrack[0][j] = 'R---'
	
	max_node = 0
	max_pos = (0,0)
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			down = s[i-1][j] - 1
			right = s[i][j-1] - 1
			if v[i-1] == w[j-1]:
				diagonal = s[i-1][j-1] + 1
			else:
				diagonal = s[i-1][j-1] - 1
			s[i][j] = max([down, right, diagonal])
			if j == len(w):
				curr_max = s[i][j]
				if curr_max > max_node:
					max_node = curr_max
					max_pos = (i,j)
			if s[i][j] == diagonal:
				backtrack[i][j] = '\\\\'
			elif s[i][j] == right:
				backtrack[i][j] = 'R---'
			else:
				backtrack[i][j] = 'D---'
	return s, max_pos, max_node, backtrack

def FitOutput(backtrack, s1, s2, max_pos):
	string1 = ''
	string2 = ''
	i = max_pos[0]
	j = max_pos[1]
	while j != 0:
		if backtrack[i][j] == 'D---':
			string2 += '-'
			string1 += s1[i-1]
			i = i - 1
		elif backtrack[i][j] == 'R---':
			string1 += '-'
			string2 += s2[j-1]
			j = j - 1
		else:
			string1 += s1[i-1]
			string2 += s2[j-1]
			i = i - 1
			j = j - 1
	return string1[::-1], string2[::-1]	

def EditDistance(v, w):
	s = [[0 for num in range(len(w)+1)] for num in range(len(v)+1)]
	for j in range(len(w)+1):
		s[0][j] = j
	for i in range(len(v)+1):
		s[i][0] = i
		
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			down = s[i-1][j] + 1
			right = s[i][j-1] + 1
			if v[i-1] == w[j-1]:
				diagonal = s[i-1][j-1]
			else:
				diagonal = s[i-1][j-1] + 1
			s[i][j] = min([down, right, diagonal])
		
	return s[len(s)-1][len(s[0])-1]

def DPChange(money, coins):
	MinNumCoins = {}
	MinNumCoins[0] = 0
	for i in range(1, money+1):
		MinNumCoins[i] = float('inf')
		for coin in coins:
			if i >= coin:
				if MinNumCoins[i-coin] + 1 < MinNumCoins[i]:
					MinNumCoins[i] = MinNumCoins[i-coin] + 1
	return MinNumCoins[money]
	
def ManhattanTourist(n, m, down, right):
	s = [[None for i in range(m+1)] for i in range(n+1)]
	s[0][0] = 0
	for i in range(1,n+1):
		s[i][0] = s[i-1][0] + down[i-1][0]
	for j in range(1,m+1):
		s[0][j] = s[0][j-1] + right[0][j-1]
	for i in range(1, n+1):
		for j in range(1, m+1):
			s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])
	return s[n][m]
	
def ManhattanTouristDiagnol(n,m,down,right,diagnol):
	s = [[None for i in range(m+1)] for i in range(n+1)]
	s[0][0] = 0
	for i in range(1,n+1):
		s[i][0] = s[i-1][0] + down[i-1][0]
	for j in range(1,m+1):
		s[0][j] = s[0][j-1] + right[0][j-1]
	for i in range(1, n+1):
		for j in range(1, m+1):
			s[i][j] = max([s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1], diagnol[i-1][j-1]])
	return s[n][m]	
	
def LocalAlignment(v, w, score):
	#DRY!!!!
	s = [[0 for num in range(len(w)+1)] for num in range(len(v)+1)]
	backtrack = [[0 for num in range(len(w)+1)] for num in range(len(v)+1)]
	for i in range(len(v)+1):
		backtrack[i][0] = 'D---'
	for j in range(len(w)+1):
		if j != 0:
			backtrack[0][j] = 'R---'
	
	max_node = 0
	pos = (0,0)
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			z_weight = 0
			down = s[i-1][j] - 5
			right = s[i][j-1] - 5
			u = score[(v[i-1],w[j-1])]
			diagonal = s[i-1][j-1] + u
			s[i][j] = max([z_weight, down, right, diagonal])
			if s[i][j] >= max_node:
				max_node = s[i][j]
				pos = (i,j)
			if s[i][j] == diagonal:
				backtrack[i][j] = '\\\\'
			elif s[i][j] == right:
				backtrack[i][j] = 'R---'
			elif s[i][j] == down:
				backtrack[i][j] = 'D---'
			else:
				backtrack[i][j] = 'Z---'
	return s, backtrack, max_node, pos
		
def OutputLocalAlignment(backtrack, s1, s2, pos):
	string1 = ''
	string2 = ''
	i = pos[0]
	j = pos[1]
	while i != 0 and j != 0:
		if backtrack[i][j] == 'Z---':
			break
		if backtrack[i][j] == 'D---':
			string2 += '-'
			string1 += s1[i-1]
			i = i - 1
		elif backtrack[i][j] == 'R---':
			string1 += '-'
			string2 += s2[j-1]
			j = j - 1
		else:
			string1 += s1[i-1]
			string2 += s2[j-1]
			i = i - 1
			j = j - 1
	return string1[::-1], string2[::-1] 	
	
def GlobalAlignment(v, w, score):
	#DRY!!!!
	s = [[0 for num in range(len(w)+1)] for num in range(len(v)+1)]
	backtrack = [[None for num in range(len(w)+1)] for num in range(len(v)+1)]
	for i in range(len(v)+1):
		if i != 0:
			s[i][0] = s[i-1][0] - 5
		backtrack[i][0] = 'D---'
	for j in range(len(w)+1):
		if j != 0:
			s[0][j] = s[0][j-1] - 5
			backtrack[0][j] = 'R---'
		
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			down  =  s[i-1][j] - 5
			right =  s[i][j-1] - 5
			u = score[(v[i-1], w[j-1])]
			diagonal = s[i-1][j-1] + u
			s[i][j] = max([down, right, diagonal])
			
			if s[i][j] == diagonal:
				backtrack[i][j] = '\\\\'
			elif s[i][j] == right:
				backtrack[i][j] = 'R---'
			else:
				backtrack[i][j] = 'D---'
	return s, backtrack
	
def OutputGlobalLCS(backtrack, s1, s2, i, j):
	string1 = ''
	string2 = ''
	while i != 0 or j != 0:
		if backtrack[i][j] == 'D---':
			string2 += '-'
			string1 += s1[i-1]
			i = i - 1
		elif backtrack[i][j] == 'R---':
			string1 += '-'
			string2 += s2[j-1]
			j = j - 1
		else:
			string1 += s1[i-1]
			string2 += s2[j-1]
			i = i - 1
			j = j - 1
	return string1[::-1], string2[::-1]
			
	
def LCS(v, w):
	#DRY!!!!
	s = [[None for num in range(len(w)+1)] for num in range(len(v)+1)]
	backtrack = [[None for num in range(len(w)+1)] for num in range(len(v)+1)]
	for i in range(len(v)+1):
		s[i][0] = 0
	for j in range(len(w)+1):
		s[0][j] = 0
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			down = s[i-1][j]
			right = s[i][j-1]
			if v[i-1] == w[j-1]:
				diagonal = s[i-1][j-1] + 1
				s[i][j] = max([down, right, diagonal])
			else:
				diagonal = s[i-1][j-1]
				s[i][j] = max([down, right, diagonal])
			if s[i][j] == diagonal and v[i-1] == w[j-1]:
				backtrack[i][j] = '\\\\'
			elif s[i][j] == right:
				backtrack[i][j] = 'R---'
			else:
				backtrack[i][j] = 'D---'
	return backtrack

def OutPutLCS(backtrack, v, i, j):
	string = ''
	while i != 0 and j != 0:
		if backtrack[i][j] == 'D---':
			i = i - 1
		elif backtrack[i][j] == 'R---':
			j = j - 1
		else:
			string += v[i-1]
			i = i - 1
			j = j - 1 
	return string[::-1]	

def HasIncomingEdges(graph, node):
	for n in graph:
		if node in graph[n]:
			return True
	return False
	
def TopologicalOrdering(input_graph, source):
	from copy import deepcopy
	from itertools import chain
	from random import choice
	graph = deepcopy(input_graph)
	node_list = []
	candidates = set()
	for node in graph:
		if not HasIncomingEdges(graph, node):
			candidates.add(node)
	
	while len(candidates) != 0:
		node_b = choice(list(candidates))
		node_list.append(node_b)
		candidates.remove(node_b)
		while node_b in graph:
			node_a = choice(graph[node_b])
			graph[node_b].remove(node_a)
			if len(graph[node_b]) == 0:
				graph.pop(node_b)
			if not HasIncomingEdges(graph, node_a):
				candidates.add(node_a)
	if len(graph) != 0:
		return "The input graph is not a DAG"
	else:
		return node_list[node_list.index(source):]
		
def LongestPath(p_graph, w_graph, source, sink):
	t_order = TopologicalOrdering(p_graph, source)
	visited = {source}
	s = {}
	paths = {source: str(source)}
	for node in t_order:
		if node == source:
			s[node] = 0
		else:
			s[node] = -1 * float("inf")

	for node in t_order[1:]:
		edges = [n for n in w_graph if n[1] == node and n[0] in visited]
		if len(edges) == 0:
			continue
		weight = -1 * float("inf")
		path = ''
		for x,y in edges:
			visited.add(y)
			curr_weight = s[x] + w_graph[(x,y)]
			curr_path = paths[x] + '->' + str(y)
			if curr_weight > weight:
				weight = curr_weight
				path = curr_path
		s[node] = weight
		paths[node] = path			
	max_node = max(s, key=s.get)
	max_length = s[max_node]
	max_path = paths[max_node]
	return max_length, max_path		
							
def data_parse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	n = int(data[0])
	m = int(data[1])
	down = []
	right = []
	space_index = data.index('-')
	for line in data[2:space_index]:
		l = [int(x) for x in line.split()]
		down.append(l)
		
	for line in data[space_index+1:]:
		l = [int(x) for x in line.split()]
		right.append(l)
		
	return n,m,down,right
	
def topo_data_parse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	n = int(data[0])
	m = int(data[1])
	edges = data[2:]
	weight_graph = {}
	graph = {}
	for edge in edges:
		node_data = edge.split('->')
		start = int(node_data[0])
		end = int(node_data[1].split(':')[0])
		weight = int(node_data[1].split(':')[1])
		weight_graph[(start,end)] = weight_graph.get((start,end), 0) + weight
		graph[start] = graph.get(start, []) + [end]
	return n, m, graph, weight_graph
	
def score_matrix_parse(file_name):
	score = {}
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	letters = [None] + data[0].split()
	for i in range(1, len(data)):
		x_lett = letters[i]
		vals = data[i].split()
		for j in range(1, len(letters)):
			y_lett = letters[j]
	 		val = int(vals[j])
	 		score[(x_lett, y_lett)] = score.get((x_lett, y_lett), 0) + val
	return score			
	
def manhatt_problem(file_name):
	data = data_parse(file_name)
	n = data[0]
	m = data[1]
	down = data[2]
	right = data[3]
	length = ManhattanTourist(n,m,down,right)
	return length
	
def LCS_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	string1 = data[0]
	string2 = data[1]
	backtrack = LCS(string1, string2)
	string = OutPutLCS(backtrack, string1, len(backtrack)-1, len(backtrack[0])-1)
	return string
	
def longest_path_problem(file_name):
	data = topo_data_parse(file_name)
	source = data[0]
	sink = data[1]
	p_graph = data[2]
	w_graph = data[3]
	paths = SourceToSinkPaths(p_graph, source, sink)
	path_data = TotalPathWeight(w_graph, paths)
	path_weight = path_data[0]
	path_string = path_data[1]
	return path_weight, path_string
	
def global_problem(file_name):
	score = score_matrix_parse('/Users/QuantumIan/downloads/score.txt')
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	string1 = data[0]
	string2 = data[1]
	s_and_b = GlobalAlignment(string1, string2, score)
	score_mat = s_and_b[0]
	backtrack = s_and_b[1]
	alignment = OutputGlobalLCS(backtrack, string1, string2, len(backtrack)-1, len(backtrack[0])-1)
	print score_mat[len(backtrack)-1][len(backtrack[0])-1]
	print alignment[0]
	print alignment[1]
	
def local_problem(file_name):
	score = score_matrix_parse('/Users/QuantumIan/downloads/PAM250.txt')
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	string1 = data[0]
	string2 = data[1]
	local_data = LocalAlignment(string1, string2, score)
	s_mat = local_data[0]
	backtrack = local_data[1]
	max_node = local_data[2]
	max_pos = local_data[3]
	alignment = OutputLocalAlignment(backtrack, string1, string2, max_pos)
	print max_node
	print alignment[0]
	print alignment[1]
	
def edit_distance_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	string1 = data[0]
	string2 = data[1]
	edit_distance = EditDistance(string1, string2)
	return edit_distance
	
def fit_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	string1 = data[0]
	string2 = data[1]
	fit_data = FitAlignment(string1, string2)
	max_node = fit_data[2]
	max_pos  = fit_data[1]
	backtrack = fit_data[3]
	strings = FitOutput(backtrack, string1, string2, max_pos)
	print max_node
	print strings[0]
	print strings[1]	
	
def overlap_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	string1 = data[0]
	string2 = data[1]
	overlap_data = OverlapAlignment(string1, string2)
	max_node = overlap_data[2]
	max_pos = overlap_data[3]
	backtrack = overlap_data[1]
	strings = OverlapOutput(backtrack, string1, string2, max_pos)
	print max_node
	print strings[0]
	print strings[1]