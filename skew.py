'''
This program calculates the skew of a genome for i ranging from 0 to length of genome
'''
def dataParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	return data[0]
	
def skewCalc(genome):
	G = 0
	C = 0
	skews = {}
	for i in range(len(genome)):
		if genome[i] == 'G':
			G += 1
		elif genome[i] == 'C':
			C += 1
		diff = G - C
		skews[diff] = skews.get(diff, []) + [(genome[i],i+1)]
	return skews[min(skews)]
	
def skewPrinter(skews):
	for skew in skews:
		print skew[1],
	print
	
			
	
	