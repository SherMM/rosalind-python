def dataParse(file_name):
	file = open(file_name,'r')
	data = [line.strip() for line in file.readlines()]
	return data[0],int(data[1])
	
def commonKmer(data,k):
	kmers = {}
	for i in range(len(data)):
		strand = data[i:]
		kmer = strand[:k]
		if kmer not in kmers:
			kmer_freq = strand.count(kmer)
			kmers[kmer_freq] = kmers.get(kmer_freq,[]) + [kmer]
	
	commonKmer = max(kmers.keys())
	return kmers[commonKmer]
	
		