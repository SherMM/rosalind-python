from degreeAway import parse_to_node_graph

def sumNeighborDegrees(graph):
	sums = []
	for i in range(1, len(graph) + 1):
		# sum degree counts from neighboring
		# nodes in graph
		n = sum([len(graph[node]) for node in graph[i]])
		sums.append(n)
	return sums
	
if __name__ == "__main__":
	file_name = "doubleDegreeArrayTest.txt"
	graph = parse_to_node_graph(file_name)
	degree_sums = sumNeighborDegrees(graph)
	for deg in degree_sums:
		print deg,
	print