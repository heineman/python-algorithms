from time import time
import random

def performance_sum():
    """Evaluate performance of sum"""
        
    scores = {}
    trial = 1
    while trial <= 20:
        numbers = [random.randint(1,9) for i in range(2**trial)]
        now = time()
        sum = 0
        for d in numbers:
            sum = sum + d
        done = time()

        scores[trial] = (done-now)
        trial += 1

    for i in scores:
        print 2**i, '\t', scores[i]
        
def performance_sort():
    """Evaluate performance of sorting"""

    scores = {}

    trial = 1

    while trial <= 16:
        numbers = [random.randint(1,2**trial) for i in range(2**trial)]
        now = time()
        numbers.sort()
        done = time()
        
        scores[trial] = (done-now)
        trial += 1

    for i in scores:
        print 2**i, '\t', scores[i]

def hasDuplicates(X):
    """Determine whether X contains a duplicate value"""
    for i in range(len(X)-1):
        for j in range(i+1,len(X)):
            if X[i] == X[j]:
                return True
    return False

def hasDuplicateOrNone(X):
    """Determine whether X contains None or a duplicate value"""
    for i in range(len(X)):
        if X[i] == None:
            return True
    for i in range(len(X)-1):
        for j in range(i+1,len(X)):
            if X[i] == X[j]:
                return True
    return False

