def dataParseStepic(file_name):
	file = open(file_name,'r')
	data = [line.strip() for line in file.readlines()]
	vars = data[0].split()
	string = vars[0]
	k = int(vars[1])
	d = int(vars[2])
	return string, k, d
	
def dataParseRosalind(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	vars = data[1].split()
	string = data[0]
	k = int(vars[0])
	d = int(vars[1])
	return string, k, d
	
def sub_parse(string, k):
	string_copy = string[:]
	subs = []
	while len(string_copy) >= k:
		sub = string_copy[:k]
		subs.append(sub)
		string_copy = string_copy[1:]
	return subs
	
def kmer_combos_complete(kmer, d, A = 'ACGT'):
	mis_matches = set()
	k_curr = [kmer]
	for n in range(d):
		new_matches = set()
		for k in k_curr:
			for i in range(len(kmer)):
				for j in range(len(A)):
					k_c = list(k)
					k_c[i] = A[j]
					new_kc = ''.join(k_c)
					new_matches.add(new_kc)
		mis_matches = mis_matches.union(new_matches)			
		k_curr = list(new_matches)
	return list(mis_matches)
	
def kmer_count(string, kmer, d):
	matches = []
	string_copy = string[:]
	kmer_len = len(kmer)
	while len(string_copy) >= kmer_len:
		comp_k = string_copy[:kmer_len]
		n = 0
		for i in range(len(kmer)):
			if n > d:
				break
			if kmer[i] != comp_k[i]:
				n += 1
		if n <= d:
			matches.append(comp_k)
		string_copy = string_copy[1:]
	return matches
	
def kmer_mis_matches(string, kmers, d):
	max_kmers = {}
	for kmer in kmers:
		if kmer not in max_kmers:
			kmer_data = kmer_count(string, kmer, d)
			max_kmers[kmer] = max_kmers.get(kmer, 0) + len(kmer_data)
	return max_kmers
		
def common_kmer_finder(kmer_dict):
	highest = max([val for val in kmer_dict.values()])
	most_common = [kmer for kmer,count in kmer_dict.items() if count == highest]
	return most_common
	
def combo_maker(kmers, d):
	combos = []
	for kmer in kmers:
		k_combos = kmer_combos_complete(kmer, d)
		combos += k_combos
	return combos
		
def most_common_combos(combos):
	combo_count = {}
	for combo in combos:
		combo_count[combo] = combo_count.get(combo,0) + 1
	return combo_count
	
def reverseComp(data):
	revComp = ""
	compDict = {'A':'T','T':'A','C':'G','G':'C'}
	for letter in data:
		revComp += compDict[letter]
	return revComp[::-1]
	
def sub_rev_counter(sub_combos):
	counts = {}
	total = {}
	for sub in sub_combos:
		counts[sub] = counts.get(sub,0) + 1
		rev_sub = reverseComp(sub)
		counts[rev_sub] = counts.get(rev_sub,0) + 1
		total[(sub,rev_sub)] = total.get((sub,rev_sub),0) + (counts[sub] + counts[rev_sub]) 
	return (total, counts)

def kmer_printer(kmers):
	for kmer in kmers:
		print kmer,
	print
	
def tuple_printer(kmer_tuple_list):
	for pair in kmer_tuple_list:
		for t in pair:
			print t,
	print
	
def main_problem(file_name):
	string, k, d = dataParseRosalind(file_name)
	subs = sub_parse(string, k)
	combos_k = combo_maker(subs, d)
	common_combos = most_common_combos(combos_k)
	common_kmer = common_kmer_finder(common_combos)
	kmer_printer(common_kmer)

def test_problem(string, k, d):
	subs = sub_parse(string, k)
	combos_k = combo_maker(subs, d)
	common_combos = most_common_combos(combos_k)
	common_kmer = common_kmer_finder(common_combos)
	kmer_printer(common_kmer)
	
def rev_problem(string, k, d):
	subs = sub_parse(string, k)
	sub_combos = combo_maker(subs, d)
	total, counts = sub_rev_counter(sub_combos)
	common_groups = common_kmer_finder(total)
	tuple_printer(common_groups)
	
	