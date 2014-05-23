# insertion sort

def insertion(A):
    """Insertion sort list"""
    for i in range(1,len(A)):
        insert(A, i, A[i])

def insert(A, idx, value):
    """insert value into proper location A[:idx]"""

    i = idx-1
    while i>=0 and A[i] > value:
        A[i+1] = A[i]
        i = i-1
        
    A[i+1] = value

