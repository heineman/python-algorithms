# MergeSort Implementation

def copymergesort(A):
    """Mergesort of A and return a new collection"""
    if len(A) < 2:
        return A

    mid = len(A)/2
    left = copymergesort(A[:mid])
    right = copymergesort(A[mid:])

    i = j = 0
    B = []

    while len(B) < len(A):
        if j >= len(right) or (i < mid and left[i] < right[j]):
            B.append(left[i])
            i += 1
        elif j < len(right):
            B.append(right[j])
            j += 1

    return B


def mergeSort(A):
    """merge sort A in place"""
    copy = list(A)

    mergesort_array(copy, A, 0, len(A))


def mergesort_array(A, result, start, end):
    """Mergesort array in memory with given range"""
    if end - start < 2:
        return
    if end - start == 2:
        if result[start] > result[start+1]:
            result[start],result[start+1] = result[start+1],result[start]
        return

    mid = (end + start)/2
    mergesort_array(result, A, start, mid)
    mergesort_array(result, A, mid, end)
    
    # merge is now ready. Merge from A back into result
    i = start
    j = mid
    idx = start
    while idx < end:
        if j >= end or (i < mid and A[i] < A[j]):
            result[idx] = A[i]
            i += 1
        else:
            result[idx] = A[j]
            j += 1
            
        idx += 1
