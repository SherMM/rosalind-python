def dataParse(file_name):
	file = open(file_name, "r")
	data = [line.strip().split() for line in file.readlines()][0]
	numbers = []
	for number in data:
		numbers.append(int(number))
	return numbers
		

def offspring(n):
	probList = [1.0,1.0,1.0,0.75,0.50,0.0]
	sum = 0
	for i in range(len(n)):
		sum += 2*n[i]*probList[i]
	return sum
