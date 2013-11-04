def dataParse(file_name):
	file = open(file_name, 'r')
	data  = [line.strip() for line in file.readlines()]
	return data
	
def urlMake(data):
	url_starter = "http://www.uniprot.org/uniprot/"
	url_ender = ".fasta"
	urls = []
	for code in data:
		url = url_starter + code + url_ender
		urls.append((code, url))
	return urls
	
def urlParse(urls):
	import urllib
	ids_and_strands = []
	for url in urls:
		url_info = list(urllib.urlopen(url[1]))
		url_lines = [line[:len(line)-1] for line in url_info[1:]]
		strand = ''.join(url_lines)
		ids_and_strands.append((url[0], strand))
	return ids_and_strands
	
def motifFinder(strandData):
	import re
	motifDict = {}
	for strand in strandData:
		hits = [m.start(0) + 1 for m in re.finditer('N(?=[^P][S|T][^P])', strand[1])]
		if hits != []:
			motifDict[strand[0]] = motifDict.get(strand[0],[]) + hits
	return motifDict
	
def printer(data):
	info = data.items()
	for pair in info:
		print pair[0]
		for num in pair[1]:
			print num,
		print

		