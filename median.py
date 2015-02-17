'''
This program implements the partion, quicksort,
randomized select, and randomized partition algorithms
'''
from itertools import izip_longest
from random import randrange
from numpy.random import randint
from copy import copy
import sys


def partition(blist, first, last):
    '''
    Partions integers in alist around
    a chosen pivot point.
    '''
    pivot = blist[last]
    back = first - 1
    for front in xrange(first, last):
        if blist[front] <= pivot:
            back += 1
            swap(blist, back, front)
    swap(blist, back+1, last)
    return back+1


def randomized_partition(blist, first, last):
    '''
    Partitions array around a randomly
    selected pivot point
    '''
    pivot = randrange(first, last)
    swap(blist, last, pivot)
    return partition(blist, first, last)


def swap(alist, index1, index2):
    '''
    Swaps elements in alist at index1
    and index2
    '''
    temp = alist[index1]
    alist[index1] = alist[index2]
    alist[index2] = temp


def quicksort(alist, first, last):
    '''
    Sort alist using quicksort algorithm
    '''
    blist = copy(alist)
    _quicksort(blist, first, last)
    return blist


def _quicksort(blist, first, last):
    '''
    Sorts a list using the quicksort
    algorithm
    '''
    if first < last:
        pivot = partition(blist, first, last)
        _quicksort(blist, first, pivot-1)
        _quicksort(blist, pivot+1, last)


def randomized_quicksort(alist, first, last):
    '''
    Sorts a list using quicksort algorithm
    with the use of a random partition
    '''
    blist = copy(alist)
    _randomized_quicksort(blist, first, last)
    return blist


def _randomized_quicksort(blist, first, last):
    '''
    Helper method for sorting a list using
    quicksort algorithm and random parition
    '''
    if first < last:
        pivot = randomized_partition(blist, first, last)
        _randomized_quicksort(blist, first, pivot-1)
        _randomized_quicksort(blist, pivot+1, last)


def randomized_select(alist, first, last, i):
    '''
    Returns the i-th smallest item in alist
    '''
    blist = copy(alist)
    return _randomized_select(blist, first, last, i)


def _randomized_select(blist, first, last, i):
    '''
    Helper method for returning the i-th smallest
    item in a alist
    '''
    if first is last:
        return blist[first]
    pivot = randomized_partition(blist, first, last)
    k = pivot - first + 1
    if i is k:
        return blist[pivot]
    elif i < k:
        return _randomized_select(blist, first, pivot-1, i)
    else:
        return _randomized_select(blist, pivot+1, last, i-k)


def select(alist, i):
    '''
    Finds the i-th smallest item in alist
    '''
    if len(alist) is 1:
        return alist[0]
    # split list into groups of 5 elements
    groups = grouper(alist)
    # sort each group and find the median in each
    medians = []
    for group in groups:
        med = sorted(group)[(len(group)-1)/2]
        medians.append(med)
    pivot = select(medians, len(medians)/2)

    # partition array alist around pivot
    lower = []
    equal = []
    upper = []
    for item in alist:
        if item < pivot:
            lower.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            upper.append(item)
    if i <= len(lower) - 1:
        return select(lower, i)
    elif i <= len(lower) + len(equal) - 1:
        return pivot
    else:
        return select(upper, i - (len(lower) + len(equal)))


def partition_with_pivot(alist, first, last, pivot):
    '''
    Partions alist around a pivot
    '''
    # find pivot index
    print "List: ", alist
    print "First: ", first
    print "Last: ", last
    print "Pivot: ", pivot
    index = alist.index(pivot)
    print
    # move pivot to the end
    if index is not -1:
        swap(alist, first, last)

    back = first - 1
    for front in xrange(first, last):
        if alist[front] < pivot:
            back += 1
            swap(alist, back, front)
    swap(alist, back+1, last)
    print "Partitioned: ", alist
    return back+1


def grouper(alist, size=5):
    '''
    Splits alist into lists with size elements
    '''
    groups = [iter(alist)] * size
    return ([x for x in z if x is not None] for z in izip_longest(*groups))


def parse_text_file(filename):
    '''
    Parses textfile with inputs for select function
    '''
    with open(filename) as f:
        _, array = [map(int, line.strip().split()) for line in f.readlines()]
        return array


if __name__ == "__main__":
    '''
    a = randint(100, size=25)
    print a
    print quicksort(a, 0, len(a)-1)
    print a
    print

    b = randint(100, size=25)
    print b
    print randomized_quicksort(b, 0, len(b)-1)
    print b
    print

    c = randint(100, size=10)
    print c
    print randomized_quicksort(c, 0, len(c)-1)
    print randomized_select(c, 0, len(c)-1, 4)
    print c
    print

    e = randint(100, size=100)
    print e
    print select(e.tolist(), len(e)/2)
    print randomized_quicksort(e, 0, len(e)-1)

    print "Test to kind k-th smallest element of an array"
    f = randint(100, size=17)
    print f
    k = 11
    print "k: ", k
    print select(f.tolist(), k-1)
    print randomized_quicksort(f, 0, len(f)-1)
    '''

    filename = sys.argv[-1]
    array = parse_text_file(filename)
    q = randomized_quicksort(array, 0, len(array)-1)
    for num in q:
        print num,
    print
