from cycloSeq import mass_dict, specParse
from theo_spec import mol_mass_dict, theoretical_spectrum

masses = mass_dict("/Users/QuantumIan/downloads/integer_mass_table.txt")
pep_mass_dict = mol_mass_dict("/Users/QuantumIan/downloads/integer_mass_table.txt")

def pepConvert(num_peptide):
	if num_peptide == '':
		return ''
	peptide = num_peptide.split('-')
	new_pep = ''
	for number in peptide:
		new_pep += masses[int(number)]
	return new_pep
		
def pepSum(num_pep):
	if num_pep == '':
		return 0
	nums = [int(num) for num in num_pep.split('-')]
	return sum(nums)
	
def pepScore(peptide, main_spec):
	if peptide == '':
		return 0
	pep_spec = theoretical_spectrum(peptide)
	score = 0
	p_iter = list(set(pep_spec))
	for p_pep in p_iter:
		p_count = pep_spec.count(p_pep)
		m_count = main_spec.count(p_pep)
		if p_count == 0 or m_count == 0:
			continue
		else:
			if p_count == m_count:
				score += max(p_count, m_count)
			else:
				score += min(p_count, m_count)
	return score
	
def pepCut(pep_list, main_spec, N):
	converted = []
	for pep in pep_list:
		new_pep = pepConvert(pep)
		pep_score = pepScore(new_pep, main_spec)
		converted.append((pep, pep_score))
		
	converted = sorted(converted, key=lambda x:x[1])[::-1][:N]
	return [x for x,y in converted]
	
def pepExpand(leader_board):
	new_leader_board = []
	pep_masses = [str(pep) for pep in sorted(masses.keys())]
	for p_mass in pep_masses:
		for k_mer in leader_board:
			new_pep = k_mer + '-' + p_mass
			new_leader_board.append(new_pep)
	return new_leader_board
	
def cycloSeq(spectrum, N):
	spec = sorted(specParse(spectrum))
	pep_masses = sorted(masses.keys())
	parent_mass = spec[-1]
	leader = ''
	leader_board = [str(mass) for mass in pep_masses]
	while len(leader_board) != 0:
		leader_board = pepExpand(leader_board)
		leaders = leader_board[:]
		for pep in leader_board:
			pep_sum = pepSum(pep)
			if pep_sum == parent_mass:
				pep_conv = pepConvert(pep)
				lead_conv = pepConvert(leader)
				pep_score = pepScore(pep_conv, spec)
				lead_score = pepScore(lead_conv, spec)
				if pep_score > lead_score:
					leader = pep
			elif pep_sum > parent_mass:
				leaders.remove(pep)
		leader_board = pepCut(leaders, spec, N)
	return leader
	
def convo_dict(spec, M):
	counts = {}
	sub_spec = spec[:-1]
	for val in spec:
		for num in sub_spec:
			diff = val - num
			if diff > 0:
				counts[diff] = counts.get(diff, 0) + 1
	new_counts = list(reversed(sorted(counts.items(), key=lambda x:x[1])))
	return [x for x,y in new_counts if int(x) >= 57 and int(x) <= 200][:M]
	
def convoExpand(leader_board, alphabet):
	new_leader_board = []
	for p_mass in alphabet:
		for k_mer in leader_board:
			new_pep = k_mer + '-' + p_mass
			new_leader_board.append(new_pep)
	return new_leader_board
	
def numCyclicSpectrum(peptide):
	subs = [0]
	pep_masses = [int(mass) for mass in peptide.split('-')]
	pep_copy = pep_masses[:]
	for pep in pep_masses:
		for i in range(1, len(pep_copy)):
			curr_pep = sum(pep_copy[:i])
			subs.append(curr_pep)
		pep_copy = pep_copy[1:] + [pep]
	subs.append(sum(pep_masses))
	return sorted(subs)
	
def convoPepScore(peptide, main_spec):
	if peptide == '':
		return 0
	pep_spec = numCyclicSpectrum(peptide)
	score = 0
	p_iter = list(set(pep_spec))
	for p_pep in p_iter:
		p_count = pep_spec.count(p_pep)
		m_count = main_spec.count(p_pep)
		if p_count == 0 or m_count == 0:
			continue
		else:
			if p_count == m_count:
				score += max(p_count, m_count)
			else:
				score += min(p_count, m_count)
	return score	
	
def convoPepCut(pep_list, main_spec, N):
	converted = []
	for pep in pep_list:
		pep_score = convoPepScore(pep, main_spec)
		converted.append((pep, pep_score))
		
	converted = sorted(converted, key=lambda x:x[1])[::-1][:N]
	return [x for x,y in converted]
			
def convoCycloSeq(spectrum, N, M):
	spec = sorted(specParse(spectrum))
	pep_masses = convo_dict(spec, M)
	parent_mass = spec[-1]
	leader = ''
	lead_score = 0
	leader_board = [str(mass) for mass in pep_masses]
	new_masses = leader_board
	while len(leader_board) != 0:
		leader_board = convoExpand(leader_board, new_masses)
		leaders = leader_board[:]
		for pep in leader_board:
			pep_sum = pepSum(pep)
			if pep_sum == parent_mass:
				pep_score = convoPepScore(pep, spec)
				#lead_score = convoPepScore(leader, spec)
				if pep_score > lead_score:
					leader = pep
					lead_score = pep_score
			elif pep_sum > parent_mass:
				leaders.remove(pep)
		leader_board = convoPepCut(leaders, spec, N)
	return leader	
		
		
	
		
