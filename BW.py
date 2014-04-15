def LTFMap(bwt):
	first_col = ''.join(sorted(bwt))
	bd = {}
	ld = {}
	for i in range(len(bwt)):
		b_letter = bwt[i]
		l_letter = first_col[i]
		bd[b_letter] = bd.get(b_letter, []) + [i]
		ld[l_letter] = ld.get(l_letter, []) + [i]
	
	ltf = {}
	for letter in bd:
		for i in range(len(bd[letter])):
			last = bd[letter][i]
			first = ld[letter][i]
			ltf[last] = first
	return ltf
	
def BWMatching(last_col, pattern):
	top = 0
	bottom = len(last_col)
	ltf = LTFMap(last_col)
	while top <= bottom:
		if len(pattern) > 0:
			symbol = pattern[-1]
			pattern = pattern[:-1]
			curr_last_col = last_col[top:bottom+1]
			if symbol in curr_last_col:
				top_index = last_col.find(symbol, top)
				bottom_index = last_col.rfind(symbol, top, bottom + 1)
				top = ltf[top_index]
				bottom = ltf[bottom_index]
			else:
				return 0
		else:
			return (bottom - top) + 1

def FirstOccurrence(text):
	f = {}
	letters = list(set(list(text)))
	for letter in letters:
		index = text.find(letter)
		f[letter] = index
	return f			
				
def BetterBWMatching(last_col, pattern):
	top = 0
	bottom = len(last_col)
	first_col = ''.join(sorted(last_col))
	first_occ = FirstOccurrence(first_col)	
	while top <= bottom:
		if len(pattern) > 0:
			symbol = pattern[-1]
			pattern = pattern[:-1]
			curr_last_col = last_col[top:bottom+1]
			if symbol in curr_last_col:
				top = first_occ[symbol] + last_col[:top].count(symbol)
				bottom = first_occ[symbol] + last_col[:bottom+1].count(symbol) - 1
			else:
				return 0
		else:
			return (bottom - top) + 1
						
def BWT(text):
	rotations = [text]
	curr = text
	while curr.index('$') != len(text)-2:
		new_curr = curr[-1] + curr[0:-1]
		rotations.append(new_curr)
		curr = new_curr
	
	s = sorted(rotations)
	bwt = ''
	for string in s:
		bwt += string[-1]
	return bwt
	
def BWTReverse(bwt):
	lex = ''.join(sorted(bwt))
	bd = {}
	ld = {}
	for i in range(len(bwt)):
		b_letter = bwt[i]
		l_letter = lex[i]
		bd[b_letter] = bd.get(b_letter, []) + [i]
		ld[l_letter] = ld.get(l_letter, []) + [i]

	start = bd['$'][0]
	text = '$'
	while len(text) < len(bwt):
		curr = lex[start]
		text += curr
		lnum = ld[curr].index(start)
		bnum = bd[curr][lnum]
		start = bnum
	return text[1:] + text[0]
	
def BWTMatchPositions(text, patterns):
	import re
	positions = []
	for pattern in patterns:
		curr_pos = [m.start() for m in re.finditer('(?=' + pattern + ')', text)]
		positions += curr_pos
	return sorted(positions)
	
def ApproxPatternMatch(text, patterns, d):
	import regex
	positions = []
	for pattern in patterns:
		subs = regex.findall(r'(?:' + pattern + '){s<=' + d + '}', text)]
		for sub in subs:
			pos = text.find(sub)
			positions.append(pos)
	return sorted(positions)
	
def PartialSuffixArray(text, k):
	indices = range(len(text))
	s = sorted(indices, key=lambda x: buffer(text,x))
	m = [(i,s[i]) for i in range(len(s)) if s[i] % k == 0]
	return m
	
def bwt_problem(file_name):
	from mutations import simple_parse
	text = simple_parse(file_name)
	bwt = BWT(text)
	return bwt
	
def reverse_problem(file_name):
	from mutations import simple_parse
	bwt = simple_parse(file_name)
	text = BWTReverse(bwt)
	return text

def matching_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	bwt = data[0]
	patterns = data[1].split()
	for p in patterns:
		print BWMatching(bwt, p),
	print

def better_matching_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	bwt = data[0]
	patterns = data[1].split()	
	for p in patterns:
		print BetterBWMatching(bwt, p),
	print	
	
def par_suff_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	text = data[0]
	k = int(data[1])
	suff_array = PartialSuffixArray(text, k)
	for x,y in suff_array:
		print str(x) + ',' + str(y)
		
def pattern_position_problem(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]	
	text = data[0]
	patterns = data[1:]
	positions = BWTMatchPositions(text, patterns)
	for p in positions:
		print p,
	print