'''
 Given a specific pattern, this program finds all such patterns
 and returns their positions in a string of text. 
'''
def dataParse(file_name):
	file = open(file_name, 'r')
	data = [line.strip() for line in file.readlines()]
	return data
	
def patternMatch(data):
	import re
	pattern = data[0]
	strand = data[1]
	match_pos = [m.start(0) for m in re.finditer("%s(?=%s)" % (pattern[0],pattern[1:]), strand)]
	return match_pos
	
def patternPrinter(matches):
	for match in matches:
		print match,
	print 