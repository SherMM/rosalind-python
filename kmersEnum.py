def dataParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	return (data[0].split(), int(data[1]))
	
def kmersEnum(data):
	from itertools import product
	alpha = data[0]
	repeats = data[1]
	permutations = [x for x in product(alpha, repeat = repeats)]
	k_mers = []
	for pair in permutations:
		km = pair[0] + pair[1]
		k_mers.append(km)
	return k_mers
	
def kmersPrinter(data):
	for k in data:
		print k
	