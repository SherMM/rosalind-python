def data_parse(file_name):
	with open(file_name, 'r') as f:
		data = [line.strip().split() for line in f.readlines()]
		k, n = data[0]
		arrays = data[1:]
		return arrays, k, n
		
def findMajorityElement(arrays, k, n):
	"""
	For k arrays of size n containing positive
	integers not exceeding 10^5, returns an element
	occuring strictly more than n/2 times.
	
	Will use the Counter class from python collections
	module.
	"""
	from collections import Counter
	# will cull the most common integer from each array
	# into an array.
	majors = []
	for a in arrays:
		c = Counter(a)
		# find the integer occuring most frequently
		mc = max(c, key=c.get)
		if c[mc] > len(a)/2: majors.append(mc)
		else: majors.append(-1)
	return majors
	
		
if __name__ == "__main__":
	file_name = 'datasets/rosalind_maj.txt'
	arrays, k, n = data_parse(file_name)
	majors = findMajorityElement(arrays, k, n)
	for m in majors:
		print m,
	print
	
