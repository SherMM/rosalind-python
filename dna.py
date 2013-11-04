d = open("rosalind_dna-1.txt","r")
DNA = [line.strip() for line in d.readlines()][0]
data = {}
for letter in DNA:
	data[letter] = data.get(letter, 0) + 1

dnaL = sorted([letter for letter, value in data.items()])
for letter in dnaL:
	print data[letter],
