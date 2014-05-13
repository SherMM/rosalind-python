def insertion_sort(array):
	swaps = 0
	for i in range(1, len(array)):
		k = i - 1
		curr = array[i]
		while (k >= 0) and (array[k] > curr):
			array[k+1] = array[k]
			swaps += 1
			k -= 1
		array[k+1] = curr
	return array, swaps
	
		