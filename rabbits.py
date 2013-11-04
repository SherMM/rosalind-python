def rabbits(n,k):
    if n <= 2:
        return 1
    else:
        return rabbits(n-1,k) + k*rabbits(n-2,k)
 
memoTable = {}
       
def memoRabbits(n,k):
	if n <= 2:
		return 1
	if n in memoTable:
		return memoTable[n]
	memoTable[n] = memoRabbits(n-1,k) + k*memoRabbits(n-2,k)
	return memoTable[n]
		
		
		