def dataParse(file_name):
	data = open(file_name, 'r')
	DNA = [line.strip() for line in data.readlines()]
	dnaDict = {}
	key = ''
	for line in DNA:
		if line[0] == '>':
			key = line[1:]
			dnaDict[key] = ''
		else:
			dnaDict[key] += line
	return dnaDict
	
def gc(data):
	gc_percentages = {}
	for strand in data:
		gc_percentages[strand] = 100*(gc_percentages.get(strand, 0) + data[strand].count('C') + data[strand].count('G'))/float(len(data[strand]))
	return gc_percentages
	
def gc_max(data):
	max_gc = max(data, key=data.get)
	return max_gc,round(data[max_gc],6)
			
	