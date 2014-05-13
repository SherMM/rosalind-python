"""
Solves the independent alleles problem from Roslaind.info website
"""

def binomial(n, k):
    if k > n - k:
        k = n - k
    total = 1
    for i in range(1, k + 1):
        total *= (n - (k - i))
        total /= i
    return total
	
def prob(n, k):
	return binomial(2**k, n) * 0.25**n * 0.75**(2**k - n)
	
def probFinder(k, N):
	return 1 - sum(prob(n, k) for n in range(N))
	
if __name__ == "__main__":
	file_name = "/Users/QuantumIan/downloads/rosalind_lia.txt"
	with open(file_name, 'r') as f:
		data = [line.strip().split() for line in f.readlines()][0]
		k, N = int(data[0]), int(data[1])
		
	print probFinder(k, N)