'''
This program finds the positions of all common clumps in a 
genome represented as a string.
'''


def dataParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	vars = data[1].split()
	genome = data[0]
	k = int(vars[0])
	t = int(vars[2])
	L = int(vars[1])
	return (k, L, t, genome)
	
def urlParse(url):
	import urllib2 
	url = urllib2.urlopen(url)
	url_text = [line[:len(line)-1] for line in url]
	return url_text[0]
	
'''
returns all distinct clumps of length k appearing t times in a genome of length L 	
'''
def clumpFind(k, L, t, genome):
	genome_copy = genome[:]
	clumps = []
	while len(genome_copy) >= L:
		# tracks the number of clumps found for a given segment of genome
		window = genome_copy[:L]
		window_copy = window[:]
		while len(window_copy) >= k:
			clump = window_copy[0:k]
			k_mer_count = window.count(clump)
			if k_mer_count == t and clump not in clumps:
				clumps.append(clump)
			window_copy = window_copy[1:]
		genome_copy = genome_copy[1:]
	return clumps
	
def clumpPrinter(clumps):
	for clump in clumps:
		print clump,
	print