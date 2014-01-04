from kmer import kmer_combos_complete, sub_parse

def dataParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	return data

def outputParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip().split() for line in file.readlines()][0]
	return data
		
def kmer_find(kmer, strand, d):
	strand_copy = strand[:]
	while len(strand_copy) >= len(kmer):
		curr_sub = strand_copy[:len(kmer)]
		char_comp = zip(kmer, curr_sub)
		diff_counter = 0
		for pair in char_comp:
			if diff_counter > d:
				break
			else:
				if pair[0] != pair[1]:
					diff_counter += 1
		if diff_counter <= d:
			return True
		strand_copy = strand_copy[1:]
	return False
	
def motifEnum(strands, k, d):
	matches = []
	used_primes = []
	for strand in strands:
		strand_subs = sub_parse(strand, k)
		for sub in strand_subs:
			k_primes = kmer_combos_complete(sub, d)
			k_primes = list(set(k_primes) - set(used_primes))
			used_primes += k_primes
			for prime in k_primes:
				found_count = 0
				for dna in strands:
					if kmer_find(prime, dna, d):
						found_count += 1
					else:
						break
				if found_count == len(strands):
					matches.append(prime)
	return matches
	
def printer(matches):
	for m in matches:
		print m,
	print