'''
This program uses the 2-way partition technique to partition
the items by choosing the first value in the array as the
pivot value and rearranging items in the array so that all items
less than or equal to the pivot are placed lower in the array than
the pivot, and all items greater than the pivot are placed higher
in the array

Ian Laurain
'''
import sys


def two_way_partition(alist):
    '''
    Returns an array alist, partitioned
    around a pivot value
    '''
    pivot = alist[0]
    low = []
    high = []
    for item in alist[1:]:
        if item <= pivot:
            low.append(item)
        else:
            high.append(item)
    return low+[pivot]+high


def parse_text_file(filename):
    '''
    Parses text file, ignoring first value in
    the file which indicates the length of the array
    '''
    with open(filename) as f:
        data = [map(int, line.strip().split()) for line in f.readlines()][1:]
        return data[0]


if __name__ == "__main__":
    filename = sys.argv[-1]
    data = parse_text_file(filename)
    partition = two_way_partition(data)
    for val in partition:
        print val,
    print
