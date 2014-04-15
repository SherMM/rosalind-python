def BackBuild(v, w, z):
	backtrack = [[[0 for num in range(len(z)+1)] for num in range(len(w)+1)] for num in range(len(v)+1)]
	
	for i in range(len(v)+1):
		for j in range(len(w)+1):
			for k in range(len(z)+1):
				if i != 0:
					if j == 0 and k == 0:
						backtrack[i][j][k] = 4
					elif j == 0 and k != 0:
						backtrack[i][j][k] = 5
					elif j != 0 and k == 0:
						backtrack[i][j][k] = 6
				else:
					if j == 0 and k != 0:
						backtrack[i][j][k] = 1
					elif j != 0 and k == 0:
						backtrack[i][j][k] = 2
					elif j != 0 and k != 0:
						backtrack[i][j][k] = 3
	return backtrack
					
						
					

def MultipleLCS(v, w, z):
	s = [[[0 for num in range(len(z)+1)] for num in range(len(w)+1)] for num in range(len(v)+1)]
	backtrack = BackBuild(v, w, z)
	
	for i in range(len(z)+1):
		s[0][0][i] = -1*i
	for j in range(len(w)+1):
		s[0][j][0] = -1*j
	for k in range(len(v)+1):
		s[k][0][0] = -1*k
		
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			for k in range(1, len(z)+1):
				down = s[i-1][j][k]
				right = s[i][j-1][k] 
				forward = s[i][j][k-1]
				dr = s[i-1][j-1][k]
				df = s[i-1][j][k-1]
				rf = s[i][j-1][k-1]
				if v[i-1] == w[j-1] == z[k-1]:
					drf = s[i-1][j-1][k-1] + 1
				else:
					drf = s[i-1][j-1][k-1]
				s[i][j][k] = max([down, right, forward, dr, df, rf, drf])
				
				if s[i][j][k] == drf:
					backtrack[i][j][k] = 7
				elif s[i][j][k] == rf:
					backtrack[i][j][k] = 6
				elif s[i][j][k] == df:
					backtrack[i][j][k] = 5
				elif s[i][j][k] == dr:
					backtrack[i][j][k] = 4
				elif s[i][j][k] == forward:
					backtrack[i][j][k] = 3
				elif s[i][j][k] == right:
					backtrack[i][j][k] = 2
				else:
					backtrack[i][j][k] = 1
					
	return s, backtrack
	
def MultipleLCSOutput(backtrack, v, w, z, i, j, k):
	string1 = ''
	string2 = ''
	string3 = ''
	while i > 0 or j > 0 or k > 0:
		if backtrack[i][j][k] == 1:
			i -= 1
			string1 += v[i]
			string2 += '-'
			string3 += '-'
		elif backtrack[i][j][k] == 2:
			j -= 1
			string1 += '-'
			string2 += w[j]
			string3 += '-'
		elif backtrack[i][j][k] == 3:
			k -= 1
			string1 += '-'
			string2 += '-'
			string3 += z[k]
		elif backtrack[i][j][k] == 4:
			i -= 1
			j -= 1
			string1 += v[i]
			string2 += w[j]
			string3 += '-'
		elif backtrack[i][j][k] == 5:
			i -= 1
			k -= 1
			string1 += v[i]
			string2 += '-'
			string3 += z[k]
		elif backtrack[i][j][k] == 6:
			j -= 1
			k -= 1
			string1 += '-'
			string2 += w[j]
			string3 += z[k]
		else:
			i -= 1
			j -= 1
			k -= 1
			string1 += v[i]
			string2 += w[j]
			string3 += z[k]
	return string1[::-1], string2[::-1], string3[::-1]


def LinearSpaceAlignment(top, bottom, left, right):
	#finish later
	pass

def MiddleEdgeAlignment(v, w, mid, score):
	s = [[0 for num in range(len(w)+1)] for num in range(len(v)+1)]
	backtrack = [[None for num in range(len(w)+1)] for num in range(len(v)+1)]
	for i in range(1, len(v)+1):
		s[i][0] = s[i-1][0] - 5
		backtrack[i][0] = 'D---'
	for j in range(1, len(w)+1):
		s[0][j] =  s[0][j-1] - 5
		backtrack[0][j] = 'R---'
	
	mid_scores = [s[0][mid]]
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			down = s[i-1][j] - 5
			right = s[i][j-1] - 5
			u = score[(v[i-1], w[j-1])]
			diagonal = s[i-1][j-1] + u
			s[i][j] = max([down, right, diagonal])
			if j == mid:
				mid_scores.append(s[i][j])
			
			if s[i][j] == diagonal:
				backtrack[i][j] = '\\\\'
			elif s[i][j] == right:
				backtrack[i][j] = 'R---'
			else:
				backtrack[i][j] = 'D---'
	
	return s, backtrack, mid_scores
	
def MiddleEdgeFinder(v, w, score):
	mid = len(w)/2
	source_to_mid = MiddleEdgeAlignment(v, w, mid, score)
	sm_backtrack = source_to_mid[1]
	sm_scores = source_to_mid[2]
	
	rev_v = v[::-1]
	rev_w = w[::-1]
	new_mid = len(w)/2 + 1
	mid_to_sink = MiddleEdgeAlignment(rev_v, rev_w, new_mid, score)
	ms_backtrack = mid_to_sink[1]
	ms_scores = mid_to_sink[2][::-1]
	
	max_score = -1*float("inf")
	m_edge = (0,0)
	for i in range(len(sm_scores)):
		curr_max = sm_scores[i] + ms_scores[i]
		if curr_max >= max_score:
			max_score = curr_max
			m_edge = (i, mid)
	
	i, j = m_edge[0], m_edge[1]
	direction = sm_backtrack[i][j]
	if direction == '\\\\':
		s_edge = (i+1, j+1)
	elif direction == 'R---':
		s_edge = (i, j+1)
	return m_edge, s_edge
	

def AffineAlignment(v, w, o_penalty, e_penalty, score):
	s_lower = [[(-1*float("inf")) for num in range(len(w)+1)] for num in range(len(v)+1)]
	s_middle = [[0 for num in range(len(w)+1)] for num in range(len(v)+1)]
	s_upper = [[(-1*float("inf")) for num in range(len(w)+1)] for num in range(len(v)+1)]
	backtrack_lower = [[None for num in range(len(w)+1)] for num in range(len(v)+1)]
	backtrack_middle = [[None for num in range(len(w)+1)] for num in range(len(v)+1)]
	backtrack_upper = [[None for num in range(len(w)+1)] for num in range(len(v)+1)]
	
	s_lower[0][0] = -1 * o_penalty
	for i in range(1, len(v)+1):
		s_lower[i][0] = s_lower[i-1][0] - e_penalty
		s_middle[i][0] = s_lower[i-1][0] - e_penalty
		backtrack_lower[i][0] = 'D---'
		backtrack_middle[i][0] = 'DC--'
	
	s_upper[0][0] = -1 * o_penalty	
	for j in range(1, len(w)+1):
		s_upper[0][j] = s_upper[0][j-1] - e_penalty
		s_middle[0][j] = s_upper[0][j-1] - e_penalty
		backtrack_upper[0][j] = 'R---'
		backtrack_middle[0][j] = 'RC--'
		
	max_node = -1*float("inf")
	max_pos = (0,0)	
	matrix = ''
	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			lower_l = s_lower[i-1][j] - e_penalty
			lower_m = s_middle[i-1][j] - o_penalty
			s_lower[i][j] = max([lower_l, lower_m])
			if s_lower[i][j] == lower_l:
				backtrack_lower[i][j] = 'D---'
			else:
				backtrack_lower[i][j] = 'CD--'
			
			upper_u = s_upper[i][j-1] - e_penalty
			upper_m = s_middle[i][j-1] - o_penalty
			s_upper[i][j] = max([upper_u, upper_m])
			if s_upper[i][j] == upper_u:
				backtrack_upper[i][j] = 'R---'
			else:
				backtrack_upper[i][j] = 'CR--'
			
			middle_l = s_lower[i][j]
			u = score[(v[i-1],w[j-1])]
			middle_m = s_middle[i-1][j-1] + u
			middle_u = s_upper[i][j]
			s_middle[i][j] = max([middle_l, middle_m, middle_u])
			if s_middle[i][j] == middle_l:
				backtrack_middle[i][j] = 'DC--'
			elif s_middle[i][j] == middle_m:
				backtrack_middle[i][j] = '\\\\'
			else:
				backtrack_middle[i][j] = 'RC--'
			
			if i == len(v) and j == len(w):
				lower_max = s_lower[i][j]
				upper_max = s_upper[i][j]
				middle_max = s_middle[i][j]
				curr_max = max([lower_max, upper_max, middle_max])
				if curr_max > max_node:	
					max_node = curr_max
					max_pos = (i,j)
					if curr_max == lower_max:
						matrix = 'LOWER'
					elif curr_max == upper_max:
						matrix = 'UPPER'
					else:
						matrix = 'MIDDLE'
				
	
	s_matrices = s_lower, s_upper, s_middle
	back_matrices = backtrack_lower, backtrack_upper, backtrack_middle
	return s_matrices, back_matrices, max_node, max_pos, matrix
	
# works for some, but index errors when s2 longer than s1
def AffineOutput(backtracks, s1, s2, max_pos, matrix):
	string1 = ''
	string2 = ''
	i = max_pos[0]
	j = max_pos[1]
	b_lower = backtracks[0]
	b_upper = backtracks[1]
	b_middle = backtracks[2]
	curr_mat = matrix
	while i != 0 or j != 0:
		if curr_mat == 'LOWER':
			l_data = LowerBacktrack(b_lower, s1, (i,j))
			gap = l_data[0]
			sub = l_data[1]
			i = l_data[2][0]
			j = l_data[2][1]
			string2 += gap
			string1 += sub
			curr_mat = 'MIDDLE'
		elif curr_mat == 'UPPER':
			u_data = UpperBacktrack(b_upper, s2, (i,j))
			gap = u_data[0]
			sub = u_data[1]
			i = u_data[2][0]
			j = u_data[2][1]
			string1 += gap
			string2 += sub
			curr_mat = 'MIDDLE'
		else:
			if b_middle[i][j] == '\\\\':
				string1 += s1[i-1]
				string2 += s2[j-1]
				i = i - 1
				j = j - 1
			elif b_middle[i][j] == 'DC--':
				curr_mat = 'LOWER'
			elif b_middle[i][j] == 'RC--':
				curr_mat = 'UPPER'
	return string1[::-1], string2[::-1]					
	
def LowerBacktrack(b_lower, s1, pos):
	gap = ''
	sub = ''
	i = pos[0]
	j = pos[1]
	while b_lower[i][j] != 'CD--':
		gap += '-'
		i = i - 1
		sub += s1[i]
	gap += '-'
	i = i - 1
	sub += s1[i]
	return gap, sub, (i, j)

def UpperBacktrack(b_upper, s2, pos):
	gap = ''
	sub = ''
	i = pos[0]
	j = pos[1]
	while b_upper[i][j] != 'CR--':
		gap += '-'
		j = j - 1
		sub += s2[j]
	gap += '-'
	j = j - 1
	sub += s2[j]
	return gap, sub, (i, j)	


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
	
def affine_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	string1 = data[0]
	string2 = data[1]
	o_pen = 11
	e_pen = 1
	score = score_matrix_parse('/Users/QuantumIan/downloads/BLOSUM62.txt')
	aff_data = AffineAlignment(string1, string2, o_pen, e_pen, score)
	backtracks = aff_data[1]
	max_node = aff_data[2]
	max_pos = aff_data[3]
	matrix = aff_data[4]
	strings = AffineOutput(backtracks, string1, string2, max_pos, matrix)
	print max_node
	print strings[0]
	print strings[1]
	
def middle_edge_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	string1 = data[0]
	string2 = data[1]
	score = score_matrix_parse('/Users/QuantumIan/downloads/BLOSUM62.txt')
	edges = MiddleEdgeFinder(string1, string2, score)
	for edge in edges:
		print edge,
	print	
	
def linear_space_problem(file_name):
	score = score_matrix_parse('/Users/QuantumIan/downloads/BLOSUM62.txt')
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
	
def multiple_lcs_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	string1 = data[0]
	string2 = data[1]
	string3 = data[2]	
	m_data = MultipleLCS(string1, string2, string3)
	scores = m_data[0]
	max_score = scores[len(string1)][len(string2)][len(string3)]
	backtrack = m_data[1]
	strings = MultipleLCSOutput(backtrack, string1, string2, string3, len(string1), len(string2), len(string3))
	print max_score
	print strings[0]
	print strings[1]
	print strings[2]
	
def matrix_printer(matrix):
	for line in matrix:
		for l in line:
			print l
		print