# Binary Search template file
from time import time

def contains(collection, target):
    """Determine whether collection contains target."""
    return target in collection

def insertInPlace(ordered, target):
    """Insert target into its proper location in the ordered collection"""
    for i in range(len(ordered)):
        if ordered[i] > target:
            ordered.insert(i, target)
            return

    ordered.append(target)
    

def performance():
    """Demonstrate execution performance of contains"""
    n = 1024
    while n < 50000000:
        sorted = range(n)
        now = time()

        # Code whose performance is to be evaluated
        insertInPlace(sorted, n/2)

        done = time()

        print n, (done-now)*1000
        n *= 2


        
