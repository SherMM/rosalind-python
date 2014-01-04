from cycloSeq import specParse

def convolution(spectrum):
	spec = sorted(specParse(spectrum))
	sub_spec = spec[:-1]
	diffs = []
	for val in spec:
		for num in sub_spec:
			diff = val - num
			if diff > 0:
				diffs.append(diff)
	return diffs
	
def convo_dict(spectrum, M):
	counts = {}
	spec = sorted(specParse(spectrum))
	sub_spec = spec[:-1]
	for val in spec:
		for num in sub_spec:
			diff = val - num
			if diff > 0:
				counts[diff] = counts.get(diff, 0) + 1
	return list(reversed(sorted(counts.items(), key=lambda x:x[1])))[:M]
	
def convoPrinter(convolution):
	for num in convolution:
		print num,
	print
	
def main_problem(spectrum):
	c = convolution(spectrum)
	convoPrinter(c)
			
			