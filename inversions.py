'''
Coursera

Algorithms: Design and Analysis, Part 1

Ian Laurain

This program uses a merge sort procedure to
calculate the number of inversion in an array
'''

import sys


def get_num_inversions(alist):
    '''
    Returns the sorted array alist and
    the number of inversions in an
    array alist
    '''
    size = len(alist)
    if size > 1:
        mid = size/2
        bottom = alist[:mid]
        top = alist[mid:]
        bottom, bcount = get_num_inversions(bottom)
        top, tcount = get_num_inversions(top)
        middle, mcount = count_inversions(bottom, top)
        return middle, bcount+tcount+mcount
    else:
        return alist, 0


def count_inversions(alist, blist):
    '''
    Counts and returnas the number of
    inversions in two arrays, alist and blist
    '''
    count = 0
    merged = []
    while alist and blist:
        if alist[0] <= blist[0]:
            merged.append(alist.pop(0))
        else:
            count += len(alist)
            merged.append(blist.pop(0))
    merged += alist + blist
    return merged, count


def parse_text_file(filename):
    '''
    Parse text file of integers into
    an array
    '''
    with open(filename) as f:
        data = [map(int, line.strip().split()) for line in f.readlines()][1:]
        return data[0]


if __name__ == "__main__":
    filename = sys.argv[-1]
    data = parse_text_file(filename)
    print get_num_inversions(data)
