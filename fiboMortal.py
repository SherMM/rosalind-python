MemoTable = {}
def memoFib(n):
	if n <=2:
		return 1
	if n in MemoTable:
		return MemoTable[n]
	MemoTable[n] = memoFib(n-1) + memoFib(n-2)
	return MemoTable[n]
	


k = 19
fibT = {}
def fiboMortal(n):
	if n <= k:
		return memoFib(n)
	if n in fibT:
		return fibT[n]
	for i in range(2,k+1):
		fibT[n] = fibT.get(n,0) + fiboMortal(n-i)
	return fibT[n]	
		
		