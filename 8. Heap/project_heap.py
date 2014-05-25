# Efficiently locate kth largest element

def kthSmallest(collection, k):
    """Return kth smallest element in collection for valid k >=1 """

    A = collection[:k]
    buildHeap(A)

    for i in range(k, len(collection)):
        if collection[i] < A[0]:
            A[0] = collection[i]
            heapify(A, 0, k)
    
    return A[0]

def buildHeap(A):
    """Construct heap from array A"""
    n = len(A)
    for i in range(n/2-1, -1, -1):
        heapify(A, i, n)

def heapify (A, idx, maxIdx):
    """Ensure structure rooted at A[idx] is a heap"""
    left = 2*idx+1
    right = 2*idx+2
    if left < maxIdx and A[left] > A[idx]:
        largest = left
    else: 
        largest = idx
    if right < maxIdx and A[right] > A[largest]:
        largest = right

    if largest != idx:
        A[idx],A[largest] = A[largest],A[idx]
        heapify(A, largest, maxIdx)

