def dataParse(file_name):
	file = open(file_name, 'r')
	lines = [line.strip() for line in file.readlines()]
	for i in range(1, len(lines)+1, 2):
		print lines[i]