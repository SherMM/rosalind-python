import theo_spec

def mass_dict(file_name):
	mol_dict = {}
	file = open(file_name, 'r')
	data = [line.strip().split() for line in file.readlines()]
	for pair in data:
		mol_dict[int(pair[1])] = mol_dict.get(pair[1],'') + pair[0]
	return mol_dict
	
masses = mass_dict("/Users/QuantumIan/downloads/integer_mass_table.txt")
pep_mass_dict = theo_spec.mol_mass_dict("/Users/QuantumIan/downloads/integer_mass_table.txt")

def specParse(input_spec):
	data = input_spec.split()
	numbers = [int(n) for n in data]
	return numbers
	
def pepSum(peptide):
	sum = 0
	for letter in peptide:
		sum += pep_mass_dict[letter]
	return sum

def cycloSeq(spectrum):
	spec = specParse(spectrum)
	pep_list = []
	for num in spec[1:]:
		if num in masses:
			pep_list.append(masses[num])
	
	pep_set = pep_mass_dict.keys()
	copy_pep = list(set(pep_list))
	for i in range(len(pep_list)-1):
		h_list = []
		for p in pep_set:
			for c in copy_pep:
				pep_sum = pep_mass_dict[p] + pepSum(c)
				if pep_sum in spec:
					new_pep = c+p
					h_list.append(new_pep)
		copy_pep = h_list
	
	matches = []
	for peptide in copy_pep:
		if theo_spec.theoretical_spectrum(peptide) == spec:
			matches.append(peptide)
	return matches
			
	
def pepConverter(pep_list):
	p_set = set()
	for pep in pep_list:
		peps = list(pep)
		pep_masses = [str(pep_mass_dict[letter]) for letter in peps]
		num_pep = '-'.join(pep_masses)
		p_set.add(num_pep)
	return list(p_set)
	
def pepPrinter(p_list):
	for p in p_list:
		print p,
	print 
	
def main_problem(spectrum):
	peps = cycloSeq(spectrum)
	p_list = pepConverter(peps)
	pepPrinter(p_list)
	