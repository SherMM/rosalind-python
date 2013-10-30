'''
This program to find common clumps in a genome represented as a string.
'''


def dataParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()][0]
	return data
	
'''
returns all distinct clumps of length k appearing t times in a genome of length L 	
'''
def clumpFind(k, t, genome):
	genome_copy = genome[:]
	clumps = []
	while len(genome_copy) >= k:
		# tracks the number of clumps found for a given segment of genome
		clump = genome_copy[0:k]
		k_mer_count = genome_copy.count(clump)
		if k_mer_count == t:
			clumps.append(clump)
		genome_copy = genome_copy[1:]
	return clumps