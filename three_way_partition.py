'''
This program uses the three-way-partition
technique to partition into an array so
that keys equal to the pivot are in the ~middle
of the array, keys less than the pivot are at the
bottom of the array, and keys greater than the pivot
are at the top of the array

Ian Laurain
'''
import sys


def three_way_partition(a, first, last):
    '''
    Partitions array around a pivot (1st array a item)
    and returns the partitioned array
    '''
    pivot = a[first]
    lt = first
    gt = last
    idx = first + 1
    while idx <= gt:
        if a[idx] < pivot:
            swap(a, idx, lt)
            lt += 1
            idx += 1
        elif a[idx] > pivot:
            swap(a, idx, gt)
            gt -= 1
        else:
            idx += 1
    return a


def swap(a, index1, index2):
    '''
    Swaps items at index1 and index2
    in an array a
    '''
    temp = a[index1]
    a[index1] = a[index2]
    a[index2] = temp


def parse_text_file(filename):
    '''
    Takes a textfile of 2 lines (size of array,
    numbers in array) and parses the second line
    into an array of integers and returns it.
    The first line is ignored.
    '''
    with open(filename) as f:
        data = [map(int, line.strip().split()) for line in f.readlines()]
        return data[1]
if __name__ == "__main__":
    filename = sys.argv[-1]
    data = parse_text_file(filename)
    p = three_way_partition(data, 0, len(data)-1)
    for number in p:
        print number,
    print
