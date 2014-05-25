# Heap implementation

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

def heapsort(A):
    """Perform heapsort on A"""
    
    buildHeap(A)
    for i in range(len(A)-1, 0, -1):
        A[0],A[i] = A[i],A[0]
        heapify(A, 0, i)
