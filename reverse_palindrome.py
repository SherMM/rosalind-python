from revC import reverseComp
from kmer import sub_parse
import re

def fastaParse(file_name):
	file = open(file_name ,'r')
	DNA = [line.strip() for line in file.readlines()]
	strand = ''
	for line in DNA[1:]:
		strand += line
	return strand
	
	
def reverse_palindrome(strand):
	sub_dict = {}
	for i in range(4,13):
		sub_dict[i] = sub_dict.get(i,[]) + sub_parse(strand,i)
	
	palindromes = []
	for key, sub_list in sub_dict.items():
		for sub in sub_list:
			sub_rev = reverseComp(sub)
			if sub == sub_rev:
				palindromes.append(sub)
	
	pos_dict = {}
	for pal in palindromes:
		pal_length = len(pal)
		pos = [m.start() for m in re.finditer(pal, strand)]
		for p in pos:
			if p not in pos_dict:
				pos_dict[p] = pos_dict.get(p,0) + pal_length
		
	return pos_dict
	
def pos_len_printer(pos_dict):
	for pos, length in pos_dict.items():
		print pos+1, length
		