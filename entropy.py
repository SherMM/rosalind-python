from kmer import sub_parse

def matrixParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	return data
	
def Consensus(matrix):
	alpha = ['A', 'C', 'G', 'T']
	profile = sorted(Profile(matrix).items(), key=lambda x:x[0])
	columns = zip(*[y for x,y in profile])
	consensus = ''
	for col in columns:
		max_val = max(col)
		best_letter = alpha[col.index(max_val)]
		consensus += best_letter
	return consensus		
		
def Score(matrix):
	consensus = Consensus(matrix)
	score = HammingDist(consensus, matrix)
	return score

def Count(matrix):
	columns = zip(*matrix)
	counts = {'A':[], 'C':[], 'G':[], 'T':[]}
	for col in columns:
		for letter in counts.keys():
			col_count = sum([col.count(letter), col.count(letter.lower())])
			counts[letter] = counts.get(letter, []) + [col_count]
	return counts
	
def pseudoCount(matrix):
	columns = zip(*matrix)
	counts = {'A':[], 'C':[], 'G':[], 'T':[]}
	for col in columns:
		for letter in counts.keys():
			col_count = sum([col.count(letter), col.count(letter.lower())])
			counts[letter] = counts.get(letter, []) + [col_count + 1]
	return counts
	
def pseudoProfile(matrix):
	count_matrix = pseudoCount(matrix)
	length = float(len(matrix))
	profile_matrix = {}
	for letter in count_matrix:
		for val in count_matrix[letter]:
			percent = val/length
			profile_matrix[letter] = profile_matrix.get(letter, []) + [percent]
	return profile_matrix	
	
def Profile(matrix):
	count_matrix = Count(matrix)
	length = float(len(matrix))
	profile_matrix = {}
	for letter in count_matrix:
		for val in count_matrix[letter]:
			percent = val/length
			profile_matrix[letter] = profile_matrix.get(letter, []) + [percent]
	return profile_matrix
	
def entropy_calc(column):
	import math
	col_sum = -1*sum([val*math.log(val,2) for val in column if val != 0])
	return col_sum
			
def Entropy(matrix):
	profile_matrix = Profile(matrix)
	motif_length = len(matrix[0])
	columns = zip(*[y for x,y in profile_matrix.items()])
	total = 0
	for col in columns:
		col_sum = entropy_calc(col)
		total += col_sum
	return total
	
def HammingDist(pattern, strands):
	diff_sum = 0
	for strand in strands:
		copy_strand = strand[:]
		#set initial min_diff to arbitrary high number
		min_diff = len(strand) + 1
		while len(copy_strand) >= len(pattern):
			curr_sub = copy_strand[:len(pattern)]
			diff_count = 0
			for i in range(len(pattern)):
				if diff_count > min_diff:
					break
				if pattern[i] != curr_sub[i]:
					diff_count += 1
			if diff_count <= min_diff:
				min_diff = diff_count
			copy_strand = copy_strand[1:]
		diff_sum += min_diff
	return diff_sum
	
def MedianString(strands, k):
	from itertools import product
	alphabet = ['A', 'C', 'G', 'T']
	patterns = [''.join(combo) for combo in product(alphabet, repeat=k)]
	best_pattern = ''
	best_dist = sum([len(s) for s in strands]) + 1
	for pattern in patterns:
		curr_dist = HammingDist(pattern, strands)
		if curr_dist < best_dist:
			best_pattern = pattern
			best_dist = curr_dist
	return best_pattern
			
def parseProfile(file_name):
	file = open(file_name, 'r')
	file_data = [line.strip() for line in file.readlines()]
	data = []
	for col in file_data:
		new_col = [float(num) for num in col.split()]
		data.append(new_col)
	data = zip(*data)	
	profile = {'A':(), 'C':(), 'G':(), 'T':()}
	profile['A'] = data[0]
	profile['C'] = data[1]
	profile['G'] = data[2]
	profile['T'] = data[3]
	return profile
	
def probableKmer(strand, k, profile):
	subs = sub_parse(strand, k)
	best = ''
	best_prob = 0.0
	for sub in subs:
		prob = 1
		for i in range(len(sub)):
			curr_prob = profile[sub[i]][i]
			prob *= curr_prob
		if prob > best_prob:
			best_prob = prob
			best = sub
		elif prob == best_prob:
			if best == '':
				best = sub
	return best
	
def greedyMotifSearch(strands, k):
	best_motifs = []
	for strand in strands:
		kmer = strand[:k]
		best_motifs.append(kmer)
	best_score = Score(best_motifs)
	
	subs = sub_parse(strands[0], k)
	for sub in subs:
		motifs = [sub]
		for d_strand in strands[1:]:
			sub_profile = Profile(motifs)
			p_kmer = probableKmer(d_strand, k, sub_profile)
			motifs.append(p_kmer)
		sub_score = Score(motifs)
		if sub_score < best_score:
			best_motifs = motifs
			best_score = sub_score
	return best_motifs
	
def pseudoGreedy(strands, k):
	best_motifs = []
	for strand in strands:
		kmer = strand[:k]
		best_motifs.append(kmer)
	best_score = Score(best_motifs)
	
	subs = sub_parse(strands[0], k)
	for sub in subs:
		motifs = [sub]
		for d_strand in strands[1:]:
			sub_profile = pseudoProfile(motifs)
			p_kmer = probableKmer(d_strand, k, sub_profile)
			motifs.append(p_kmer)
		sub_score = Score(motifs)
		if sub_score < best_score:
			best_motifs = motifs
			best_score = sub_score
	return best_motifs
	
def randomMotifMaker(strands, k):
	from random import randrange
	motifs = []
	for strand in strands:
		strand_len = len(strand) + 1
		index = randrange(strand_len - k)
		kmer = strand[index:index+k]
		motifs.append(kmer)
	return motifs
	
def mostProbableMotif(strands, k, profile):
	motif = []
	for strand in strands:
		kmer = probableKmer(strand, k, profile)
		motif.append(kmer)
	return motif
	
def RandomizedMotifSearch(strands, k):
	best_motif = []
	best_score = None
	for i in range(1000):
		curr_motif = randomMotifMaker(strands, k)
		curr_profile = pseudoProfile(curr_motif)
		curr_score = Score(curr_motif)
		found = False
		while not found:
			motif = mostProbableMotif(strands, k, curr_profile)
			motif_profile = pseudoProfile(motif)
			motif_score = Score(motif)
			if motif_score < curr_score:
				curr_motif = motif
				curr_score = motif_score
				curr_profile = motif_profile
			else:
				if best_score is None or curr_score < best_score:
					best_motif = curr_motif
					best_score = curr_score
				else:
					break 
	return best_motif
	
def kmerProb(kmer, profile):
	from operator import mul
	probabilities = []
	for i in range(len(kmer)):
		probability = profile[kmer[i]][i]
		probabilities.append(probability)
	return reduce(mul, probabilities)
	
def GibbsRandom(strand, profile, k):
	from random import uniform
	subs = sub_parse(strand, k)
	probs = []
	cumm_probs = []
	for i in range(len(subs)):
		sub_prob = kmerProb(subs[i], profile)
		probs.append(sub_prob)
		sum_probs = sum(probs)
		cumm_probs.append(sum_probs)
	
	rand = uniform(0.0, max(cumm_probs))
	for i in range(len(cumm_probs)):
		if cumm_probs[i] > rand:
			return subs[i]
				
def GibbsSampler(strands, k, t, N):
	from random import randrange
	best_motif = []
	best_score = None
	for i in range(20):
		motif = randomMotifMaker(strands, k)
		if best_score is None:
			best_motif = motif
			best_score = Score(motif)
		for i in range(N):
			rand = randrange(t)
			new_motif = [motif[i] for i in range(len(motif)) if i != rand]
			new_profile = pseudoProfile(new_motif)
			rand_strand = GibbsRandom(strands[rand], new_profile, k)
			motif[rand] = rand_strand
			new_motif = motif
			new_score = Score(new_motif)
			if new_score < best_score:
				best_motif = new_motif
				best_score = new_score
	return best_motif
			
			
def greedyParse(file_name):
	file = open(file_name,'r')
	data = [line.strip() for line in file.readlines()]
	return data

	
	 
		
				
	

		
				