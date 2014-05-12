def parse_for_binary_search(file_name):
	with open(file_name) as f:
		_, _, xlist, ylist = [line.strip().split() for line in f.readlines()]
		xlist = [int(num) for num in xlist]
		ylist = [int(num) for num in ylist]
		return xlist, ylist
	
def binary_search(yvalue, xarray):
		x_beg = 0
		x_end = len(xarray)-1
		while x_beg <= x_end:
			x_mid = (x_beg + x_end)//2
			if xarray[x_mid] > yvalue: x_end = x_mid-1
			elif xarray[x_mid] < yvalue: x_beg = x_mid+1
			else:
				return x_mid+1
		return -1
		
def index_finder(xarray, yarray):
	indices = []
	for y in yarray:
		index = binary_search(y, xarray)
		indices.append(index)
	return indices
		
if __name__ == "__main__":
	import os
	file_directory = '/Users/QuantumIan/downloads/'
	files = os.listdir(file_directory)
	file_name = file_directory + [f for f in files if f.startswith('rosalind')][0]
	xarray, yarray = parse_for_binary_search(file_name)
	indices = index_finder(xarray, yarray)
	for i in indices:
		print i, 
	print 
	
			