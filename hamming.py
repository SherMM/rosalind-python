def dataParse(file_name):
	data = open(file_name, 'r')
	DNA = [line.strip() for line in data.readlines()]
	return DNA
	
def hammingIndex(data):
	strand1 = data[0]
	strand2 = data[1]
	hamming_index = len([pair for pair in zip(strand1,strand2) if pair[0] != pair[1]])
	return hamming_index
	