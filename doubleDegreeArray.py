from degreeAway import parse_to_node_graph

def sumNeighborDegrees(graph, v, e):
	"""
	Takes in a graph, number of vertices, and number
	of edges and outputs the sum of each vertex's 
	neighbor's vertices. 
	"""
	sums = []
	for i in range(1, len(graph) + 1):
		# sum degree counts from neighboring
		# nodes in graph
		n = sum([len(graph[node]) for node in graph[i]])
		sums.append(n)
		# must account for a dead node --
		# a node without outgoing edges
	if v > len(graph):
		num_dead_nodes = v - len(graph)
		for i in range(num_dead_nodes):
			sums.append(0)
	return sums
	
if __name__ == "__main__":
	file_name = "datasets/rosalind_ddeg.txt"
	graph, v, e = parse_to_node_graph(file_name)
	degree_sums = sumNeighborDegrees(graph, v, e)
	for deg in degree_sums:
		print deg,
	print