from rnaToProtein import rnaCodeDict

codes = rnaCodeDict("/Users/QuantumIan/downloads/rnaCodes.txt")
reverse_codon_dict = {}
for rna, amino_acid in codes.items():
	reverse_codon_dict[amino_acid] = reverse_codon_dict.get(amino_acid,0) + 1
	
def protein_reverse(protein):
	amino_count = {}
	for acid in protein:
		amino_count[acid] = amino_count.get(acid,0) + reverse_codon_dict[acid]
	
	product = 1	
	for amino_acid,count in amino_count.items():
		product = (product * count) % 1000000
	return (product*3)
	