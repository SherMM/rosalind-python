d = open("rosalind_revc.txt", "r")

reversed_DNA = [line.strip() for line in d.readlines()][0][::-1]

compDict = {"A":"T","C":"G","G":"C","T":"A"}

revComp = ""
for letter in reversed_DNA:
	revComp += compDict[letter]
	
print revComp
	
