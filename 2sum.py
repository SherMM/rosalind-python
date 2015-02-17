'''
2sum problem
Ian Laurain

This program, given a list of integer arrays, returns
two different indices if the values at those indices
sum to 0.
'''
import sys
from collections import defaultdict


def binary_search(A, item):
    '''
    Returns item if found in array A,
    otherwise returns -1
    '''
    first = 0
    last = len(A)-1
    found = False
    index = -1

    while first <= last and not found:
        mid = first + (last - first)/2
        if A[mid] == item:
            found = True
            index = mid
        else:
            if item < A[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


def two_sum(A):
    '''
    Takes an array A and returns the two
    indices, if any, if the integer values
    stored at those indices sum to 0
    '''
    two_sums = []
    indices = defaultdict(list)
    for idx in xrange(len(A)):
        item = A[idx]
        if -item in indices:
            two_sum = (indices[-item][0], idx+1)
            two_sums.append(two_sum)
        indices[item].append(idx+1)
    if len(two_sums) is 0:
        return -1
    return two_sums


if __name__ == "__main__":
    filename = sys.argv[-1]
    with open(filename) as f:
        arrays = [map(int, line.strip().split()) for line in f.readlines()][1:]
        for array in arrays:
            two_sums = two_sum(array)
            if two_sums is -1:
                print -1
            else:
                print two_sums[0][0], two_sums[0][1]
