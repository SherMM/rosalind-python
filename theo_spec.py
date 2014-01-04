def mol_mass_dict(file_name):
	mol_dict = {}
	file = open(file_name, 'r')
	data = [line.strip().split() for line in file.readlines()]
	for pair in data:
		mol_dict[pair[0]] = mol_dict.get(pair[0],0) + int(pair[1])
	return mol_dict
	
mol_masses = mol_mass_dict("/Users/QuantumIan/downloads/integer_mass_table.txt")

def cyclic_parse(peptide):
	subs = []
	pep_copy = peptide[:]
	for pep in peptide:
		for i in range(1,len(pep_copy)):
			curr_pep = pep_copy[:i]
			subs.append(curr_pep)
		pep_copy = pep_copy[1:] + pep
	subs.append(peptide)
	return subs
			
def theoretical_spectrum(peptide):
	cyclo_spec = [0]
	sub_peps = cyclic_parse(peptide)
	for sub in sub_peps:
		total = 0
		for s in sub:
			total += mol_masses.get(s, 0)
		cyclo_spec.append(total)
	return sorted(cyclo_spec)
			