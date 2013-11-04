def mendelFirstLaw(k,m,n):
	from itertools import combinations
	types = ['YY' for i in range(k)] + ['Yy' for i in range(m)] + ['yy' for i in range(n)]
	combos = list(combinations(types,2))
	probDict = {('YY','YY'):1.0,('YY','Yy'):1.0,('YY','yy'):1.0,('Yy','Yy'):0.75,('Yy','yy'):0.5,('yy','yy'):0.0}
	sum = 0
	for pair,val in probDict.items():
		sum += probDict[pair] * combos.count(pair)
	return round(sum/len(combos),5)
	
	
	