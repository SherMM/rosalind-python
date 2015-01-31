'''
2sum problem
Ian Laurain

This program, given a list of integer arrays, returns
two different indices if the values at those indices
sum to 0.
'''
import sys


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
    indices = []
    # create list of (index, val) tuples
    # sorted by value
    B = sorted(enumerate(A), key=get_key)
    A.sort()
    for idx1 in range(len(A)):
        idx2 = binary_search(A, -A[idx1])
        if (idx2 > idx1):
            if B[idx1][0] < B[idx2][0]:
                indices.append((B[idx1][0]+1, B[idx2][0]+1))
            else:
                indices.append((B[idx2][0]+1, B[idx1][0]+1))
    return indices


def get_key(item, index=1):
    '''
    Returns the data value at the
    passed index of item
    '''
    return item[index]


def problem_printer(indices):
    '''
    Prints out the indices of valid 2sums
    for this problem
    '''
    if len(indices) is 0:
        print -1
    else:
        print indices[0][0], indices[0][1]


if __name__ == "__main__":
    filename = sys.argv[-1]
    with open(filename) as f:
        arrays = [map(int, line.strip().split()) for line in f.readlines()][1:]
        for array in arrays:
            two_sums = two_sum(array)
            problem_printer(two_sums)
