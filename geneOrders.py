def geneOrders(n):
	'''
	takes an integer n as input and
	returns a list of all possible 
	permutations from 1-n
	'''
	from itertools import permutations
	n_list = [i for i in range(1,n+1)]
	p = list(set(permutations(n_list)))
	return p
	
def permPrinter(data):
	'''
	prints the permutation data calculated above
	'''
	print len(data)
	for p in data:
		for v in p:
			print v,
		print