from rnaToProtein import rnaToProtein
from revC import reverseComp
from kmer import sub_parse
from rna import dnaToRNA


def peptide_encode(strand, peptide):
	sub_length = len(peptide)*3
	subs = sub_parse(strand, sub_length)
	peptides = []
	for sub in subs:
		sub_rna = dnaToRNA(sub)
		sub_rev = reverseComp(sub)
		rev_rna = dnaToRNA(sub_rev)
		sub_pep = rnaToProtein(sub_rna)
		rev_pep = rnaToProtein(rev_rna)
		if sub_pep == peptide or rev_pep == peptide:
			peptides.append(sub)
	return peptides
	
def peptide_printer(peptides):
	for peptide in peptides:
		print peptide
		
def main_problem(strand, peptide):
	peptides = peptide_encode(strand, peptide)
	peptide_printer(peptides)
			
	
	
	
	