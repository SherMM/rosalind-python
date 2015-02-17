'''
Ian Laurain

This program merges two sorted arrays
'''


def merge(A, B):
    '''
    merges sorted array A  with
    sorted array B and return result
    as an array C
    '''
    C = []
    idx = 0
    jdx = 0
    while idx < len(A) and jdx < len(B):
        if A[idx] <= B[jdx]:
            C.append(A[idx])
            idx += 1
        else:
            C.append(B[jdx])
            jdx += 1
    # the rest of either A or B can be
    # added to the end of C
    if idx < len(A):
        C += A[idx:]
    else:
        C += B[jdx:]
    return C


if __name__ == "__main__":
    A = [2, 4, 10, 18]
    B = [-5, 11, 12]
    print merge(A, B)
