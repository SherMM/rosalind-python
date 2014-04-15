def LCS(s1, s2):
	from suffix_tree import GeneralisedSuffixTree
	seqs = [s1, s2]
	us1 = unicode(s1, 'utf-8')
	us2 = unicode(s2, 'utf-8')
	stree = GeneralisedSuffixTree([us1, us2])
	longs = set()
	for shared in stree.sharedSubstrings():
		for seq, start, stop in shared:
			sub = seqs[seq][start:stop]
			longs.add(sub)
	return max(longs, key=len)

def PrefixTrieMatching(text, trie):
	v = 1
	i = 0
	letter = text[i]
	pattern = ''
	leaf = False
	while not leaf:
		if letter in trie[v]:
			pattern += letter
			v = trie[v][letter]
			i += 1
			if i >= len(text):
				continue
			letter = text[i]
		elif len(trie[v]) == 0:
			leaf = True
		else:
			pattern = ''
			break
	return pattern
			
def TrieMatching(text, trie):
	pos = []
	for i in range(len(text)):
		prefix = PrefixTrieMatching(text[i:], trie)
		if prefix != '':
			pos.append(i)
	return pos

def TrieMaker(patterns):
	trie = ['root', {}]
	i = 2
	for pattern in patterns:
		j = 1
		for letter in pattern:
			if letter in trie[j]:
				j = trie[j][letter]
			else:
				trie[j][letter] = i
				trie.append({})
				j = i
				i += 1
	return trie
	
def SuffixTree(patterns):
	pass
				
def AdjListPrinter(patterns):
	trie = TrieMaker(patterns)
	for i in range(1, len(trie)):
		if len(trie[i]) > 0:
			for letter in trie[i]:
				print i,
				print trie[i][letter],
				print letter
				
def PatternProcess(text):
	text_copy = text[:]
	patterns = []
	while len(text_copy) > 0:
		new_pattern = text_copy[:]
		patterns.append(new_pattern)
		text_copy = text_copy[1:]
	return patterns
	
def RepeatFind(patterns, text):
	longest = ''
	for pattern in patterns:
		if text.count(pattern) > 1:
			longest = pattern
			break
	return longest
	
def SuffixOrder(text):
	indices = range(len(text))
	s = sorted(indices, key=lambda x: buffer(text,x))
	return s
	
	
def LRSubstring(text, n):
	from itertools import chain
	subd = {}
	longest = ''
	while n < len(text):
		d = {}
		if len(subd) == 0:
			indices = range(len(text))
		else:
			indices = list(chain.from_iterable(subd.values()))
		for i in indices:
			sub = text[i:i+n]
			if text.count(sub) > 1:
				if len(sub) >= len(longest):
					d[sub] = d.get(sub, []) + [i]
					longest = sub
		if len(d) == 0:
			break
		n += 1
		subd = d
	return longest
	
def SuffixTreeStepic(text):
	from suffix_tree import SuffixTree
	utext = unicode(text[:-1], 'utf-8')
	stree = SuffixTree(utext)
	for l in stree.preOrderNodes:
		print l.edgeLabel 
	

def simple_parse(file_name):
	file = open(file_name, 'r')
	string = [line.strip() for line in file.readlines()]
	return string[0]
	
def simple_double_parse(file_name):
	file = open(file_name, 'r')
	strings = [line.strip() for line in file.readlines()]	
	string1 = strings[0]
	string2 = strings[1]
	return string1, string2				

def trie_problem(file_name):
	file = open(file_name, 'r')
	patterns = [line.strip() for line in file.readlines()]
	AdjListPrinter(patterns)	

def matching_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	text = data[0]
	patterns = data[1:]
	trie = TrieMaker(patterns)
	positions = TrieMatching(text, trie)
	return positions
	
def suffix_array_problem(file_name):
	text = simple_parse(file_name)
	order = SuffixOrder(text)
	print ', '.join([str(x) for x in order])
	
def suffix_tree_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	text = data[0]
	SuffixTreeStepic(text)
	
def lcs_problem(file_name):
	strings = simple_double_parse(file_name)
	s1 = strings[0]
	s2 = strings[1]
	longest = LCS(s1, s2)
	return longest