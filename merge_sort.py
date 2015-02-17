'''
Ian Laurain

This program implements the merge sort algorithm
'''

from merge import merge
from collections import deque
import sys


def merge_sort_rec(A):
    '''
    Returns a sorted array of the input
    array A
    '''
    if len(A) is 1:
        return A
    low = 0
    high = len(A)
    mid = 0 + (high - low)/2
    B = merge_sort_rec(A[low:mid])
    C = merge_sort_rec(A[mid:high])
    D = merge(B, C)
    return D


def merge_sort_iter(A):
    '''
    Returns a sorted array of the input
    array A
    '''
    queue = deque()
    # initialize queue
    for idx in xrange(len(A)):
        queue.append(A[idx:idx+1])

    # pop two arrays off, then merge
    while len(queue) is not 1:
        a1 = queue.popleft()
        a2 = queue.popleft()
        # merge two arrays into one
        a3 = merge(a1, a2)
        # enqueue merged array
        queue.append(a3)
    return queue[0]


def printer(queue):
    '''
    Prints out array contents into single line
    format that Rosalind autograder expects
    '''
    for item in queue:
        print item,
    print


if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        A = [map(int, line.strip().split()) for line in f.readlines()][1:][0]
        merged = merge_sort_iter(A)
        printer(merged)
