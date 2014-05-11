def orderKmersLexicographically(letters, n, lex='', order=[]):
    if n > 0:
        for letter in letters:
            order.append(lex + letter)
            orderKmersLexicographically(letters, n - 1, lex + letter, order)
    return order
	
	
if __name__ == "__main__":
	from kmersEnum import dataParse
	letters, n = dataParse('/Users/QuantumIan/downloads/rosalind_lexv.txt')
	kmers = orderKmersLexicographically(letters, n)
	for k in kmers:
		print k
		
		