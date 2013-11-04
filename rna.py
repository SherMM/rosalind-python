d = open("rosalind_rna.txt", "r")
dna = [line.strip() for line in d.readlines()][0]
rna = ""
for letter in dna:
	if letter == "T":
		rna += "U"
	else:
		rna += letter
print rna