def dataParse(file_name):
	file = open(file_name, 'r')
	string = [line.strip() for line in file.readlines()]
	return string[0].split()
	
def dictMaker(string):
	dict = {}
	for word in string:
		dict[word] = dict.get(word,0) + 1
	return dict
	
def dictPrinter(dict):
	items = dict.items()
	for pair in items:
		print pair[0], pair[1]
	
		