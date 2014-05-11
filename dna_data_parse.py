def dna_data_parse(file_name):
    '''
    Parses a DNA text file with the following format:

        >Rosalind_0209
        GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
        AGTACGGGCATCAACCCAGTT
        >Rosalind_2200
        TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
        GGTACGAGTGTTCCTTTGGGT

    Lines beginning with ">" will be recorded as DNA string names acting
    as keys in a python dictionary. Any lines following a line beginning
    with the ">" character and preceding subsequent lines beginning with
    ">", will be concatenated as the DNA string for hat key name.
    '''
    data = {}
    with open(file_name, 'rt') as f:
        for line in f.readlines():
            curr_line = line.strip()
            if curr_line[0] == '>':
                key_line = curr_line
                data[key_line] = ''
            else:
                data[key_line] += curr_line
    return data



