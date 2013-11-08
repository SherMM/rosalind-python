def dataParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	return data[0], data[1], int(data[2])
	
def patternMatch(pattern, string, mismatches):
	mis_match_dict = {}
	string_copy = string[:]
	string_index = 0
	while len(string_copy) >= len(pattern):
		current_substring = string_copy[:len(pattern)]
		num_mismatches = 0
		for i in range(len(pattern)):
			if current_substring[i] != pattern[i]:
				num_mismatches += 1
		if num_mismatches <= mismatches:
			mis_match_dict[string_index] = mis_match_dict.get(string_index, '') + current_substring
		string_copy = string_copy[1:]
		string_index += 1
	return mis_match_dict.keys()
	
def patternPrinter(keys):
	sorted_positions = sorted(keys)
	for pos in sorted_positions:
		print pos,
	print 
		
				
	
	
