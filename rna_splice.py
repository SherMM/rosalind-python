from rna import dnaToRNA
from rnaToProtein import rnaToProtein

def fastaParse(file_name):
	data = open(file_name, 'r')
	DNA = [line.strip() for line in data.readlines()]
	# keep track of iteration for intron parse
	dna_iter = DNA[1:]
	# parse DNA strand data first
	dna_key = DNA[0][1:]
	dna_strand = ''
	for line in DNA[1:]:
		if line[0] == '>':
			break
		else:
			dna_strand += line
			dna_iter = dna_iter[1:]
				
	# parse intron data next
	intron_Dict = {}
	key = ''
	for line in dna_iter:
		if line[0] == '>':
			key = line[1:]
			intron_Dict[key] = ''
		else:
			intron_Dict[key] += line
	return (dna_key, dna_strand), intron_Dict
	
def intron_cut(dna_strand, intron_Dict):
	new_dna = dna_strand[:]
	intron_items = intron_Dict.items()
	for name, intron in intron_items:
		while new_dna.find(intron) != -1:
			new_dna = new_dna.replace(intron,'')
	rna = dnaToRNA(new_dna)
	protein = rnaToProtein(rna)
	return protein