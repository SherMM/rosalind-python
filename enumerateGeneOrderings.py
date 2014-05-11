def findGeneOrderings(n):
    '''
    Takes a number n, and finds the total
    number of signed (- or +) permutations of
    length n, and returns a list of all such
    permutations.

    So, for examples, if n=2, then a possible
    ordering would be:

    [(-1,-2), (-2, -1), (-1, 2), (2, -1),
     (1, -2), (-2, 1), (1, 2), (2, 1)]
    '''
    # import required libraries
    from itertools import product, permutations
    # First, find the normal permutation
    p = [(num+1) for num in range(n)]
    for j in product(*[[-x, x] for x in p]):
        for perm in permutations(j):
            yield perm

def permutationPrinter(list_of_perms):
    print len(list_of_perms)
    for t in list_of_perms:
        for n in t:
            print n,
        print


if __name__ == "__main__":
    import os
    file_directory = '/Users/QuantumIan/downloads/'
    files = os.listdir(file_directory)
    file_name = [f for f in files if f.startswith('rosalind')][0]
    f = open(file_directory + file_name, 'r')
    n = int([line.strip() for line in f.readlines()][0])
    list_of_perms = list(findGeneOrderings(n))
    permutationPrinter(list_of_perms)
