from collections import defaultdict

def parse_to_node_graph(file_name):
	"""
	Parses a text file of type:
	
		x,y
		t,v
		p,q
		
	Where each line represents the ends of 
	an edge in a graph. Each end will be 
	parsed into a ditionary as keys representing 
	nodes, where outgoing edges from
	a node will be represented as a value
	list of end-nodes in the dictionary. 
	So, given the following edges:
		
		6 7
		6 3
		5 6
		
	The resulting dictionary will be in this 
	form:
		
		{6: [7, 3, 5]}, 5: [6], 7: [6], 3: [6]}
			
	"""
	d = defaultdict(list)
	with open(file_name, 'r') as f:
		# start from index one so first line specifying n 
		# vertices and m edges is uneeded in the case 
		# of the algorithms used to solve this problem
		data = [tuple(map(int, line.strip().split())) for line in f.readlines()][1:]
			
	for x,y in data:
		d[x].append(y)
		d[y].append(x)
	return d
		
def degreeCounter(graph):
	degrees = []
	for i in range(1, len(graph) + 1):
		degrees.append(len(graph[i]))
	return degrees
	
if __name__ == "__main__":
	file_name = '/Users/QuantumIan/downloads/rosalind_deg.txt'
	graph = parse_to_node_graph(file_name)
	degrees = degreeCounter(graph)
	for deg in degrees:
		print deg,
	print