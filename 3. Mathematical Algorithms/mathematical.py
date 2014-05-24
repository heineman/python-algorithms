# Mathematical Algorithms

import numpy
import random
from time import time

def exponent(x, n):
    """Returns the value of x raised to the nth power"""

    if n == 0:
        return 1
    if n == 1:
        return x

    if n % 2:
        return x * exponent (x*x, (n-1)/2)

    return exponent (x*x, n/2)

def exponent_nonr(x, n):
    """Non-recursive implementation of exponentiation"""

    if n == 0:
        return 1
    if n == 1:
        return x

    val = 1
    while n > 0:
        if n % 2:
            val *= x
            n -= 1
        n /= 2
        if n > 0:
            x *= x

    return val

def compareTrials_nonr(trials):
    """Compare performance on a number of runs"""

    base = 999
    timeN = timeR = 0

    for t in range(trials):
        now = time()
        check1 = exponent(base, t)
        timeR += (time() - now)

        now = time()
        check2 = exponent_nonr(base, t)
        timeN += (time() - now)

        if check1 != check2:
            raise Exception ("Invalid result")

    return (timeR, timeN)

def trialTable_nonr():
    """Output table of results for comparing nonr vs. recursive"""

    trial = 2
    while trial <= 2048:
        result = compareTrials_nonr(trial)
        print trial, '\t', result[0], '\t', result[1]

        trial *= 2

def exponent_mod(x, n, m):
    """Returns the value of x raised to the nth power modulo m"""

    if n == 0:
        return 1
    if n == 1:
        return x % m

    if n % 2:
        return x * exponent_mod (x*x % m, (n-1)/2, m) % m

    return exponent_mod (x*x, n/2, m) % m

def compareTrials(trials):
    """Compare performance on a number of runs"""

    base = 999
    mod = 17
    timeN = timeR = 0

    for t in range(trials):
        now = time()
        check1 = exponent_mod(base, t, mod)
        timeR += (time() - now)

        now = time()
        check2 = pow(base, t, mod)
        timeN += (time() - now)

        if check1 != check2:
            raise Exception ("Invalid result")

    return (timeR, timeN)

def trialTable():
    """Output table of results for comparison"""

    trial = 2
    while trial <= 2048:
        result = compareTrials(trial)
        print trial, '\t', result[0], '\t', result[1]

        trial *= 2

def randomMatrix(n):
    """Return a random nxn matrix"""
    r = []
    for i in range(n):
        r.append([random.random() for i in range(n)])

    base = numpy.array(r).reshape((n,n))
    return base

def exponent_mat(x, n):
    """Returns the value of x raised to the nth power"""
    if n == 0:
        return numpy.identity(len(x))
    if n == 1:
        return x

    if n % 2:
        return x.dot(exponent_mat (x.dot(x), (n-1)/2))

    return exponent_mat (x.dot(x), n/2)


def compareTrials_mat(trials, size):
    """Compare performance on a number of runs"""

    base = randomMatrix(size)
    timeN = timeR = 0

    for t in range(trials):
        now = time()
        check1 = exponent_mat(base, t)
        timeR += (time() - now)

        now = time()
        check2 = numpy.identity(len(base))
        for i in range(t):
            check2 = check2.dot(base)
        timeN += (time() - now)


    return (timeR, timeN)

def trialTable_mat():
    """Output table of results for comparison"""

    trial = 2
    size = 33
    while trial <= 512:
        result = compareTrials_mat(trial, size)
        print trial, '\t', result[0], '\t', result[1]

        trial *= 2

        
"""
Change Log

1. 2014.05.23   exponent_mat
                defect: return x.dot(exponent (x.dot(x), (n-1)/2))
                fix:    return x.dot(exponent_mat (x.dot(x), (n-1)/2))

                defect: return exponent (x.dot(x), n/2)
                fix:    return exponent_mat (x.dot(x), n/2)
"""
