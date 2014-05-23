# mergesort using mmap

import shutil
import tempfile
import mmap
import os
import random
from time import time

def mergesort (A):
    """public method for using mergesort on array"""
    copy = list(A)
    mergesort_array (copy, A, 0, len(A))
    
def mergesort_array(A, result, start, end):
    """mergesort array in memory"""
    if end - start < 2:
        return
    if end - start == 2:
        if result[start] > result[start+1]:
            result[start],result[start+1] = result[start+1],result[start]
            return

    mid = (end + start)/2
    mergesort_array(result, A, start, mid)
    mergesort_array(result, A, mid, end)

    # merge A left-and right
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


def compareSortTimes():
    """compare sorting algorithms"""
    
    n = 128
    while n <= 262144:
        timeN = timeM = 0
        for t in range(10):
            a1 = [random.randint(1,n) for x in range(n)]
            a2 = list(a1)

            now = time()
            a1.sort()
            timeN += (time() - now)

            now = time()
            mergesort(a2)
            timeM += (time() - now)

            assert a1 == a2

        print n, '\t', timeN/10, '\t', timeM/10
        n *= 2

def output (src):
    """print numbers in file"""
    srcFile  = open(src, "a+b")
    srcMap   = mmap.mmap(srcFile.fileno(), 0)
    length   = os.stat(src).st_size
    
    while length > 0:
        print readInt(srcMap)
        length -= 4
    srcMap.close()
    srcFile.close()
    
def mergeSortFile (src):
    """external mergesort using mmap"""

    length = os.stat(src).st_size
    
    dest = tempfile.NamedTemporaryFile(delete=False)
    dest.close()
    shutil.copy(src, dest.name)
    
    srcFile  = open(src, "a+b")
    srcMap   = mmap.mmap(srcFile.fileno(), 0)
    destFile = open(dest.name, "a+b")
    destMap  = mmap.mmap(destFile.fileno(), 0)
    
    mergeSortMMap (destMap, srcMap, 0, length)
    srcMap.close()
    destMap.close()
    srcFile.close()
    destFile.close()

def readInt(m):
    """read four bytes as int"""
    b1 = ord(m.read_byte())
    b2 = ord(m.read_byte())
    b3 = ord(m.read_byte())
    b4 = ord(m.read_byte())

    ival= (b1 << 24) + (b2 << 16) + (b3 << 8) + (b4 << 0)
    return ival

def writeInt(m, n):
    """write int as four bytes"""
    b1 = (n >> 24) & 255
    b2 = (n >> 16) & 255
    b3 = (n >> 8) & 255
    b4 = n & 255

    m.write_byte(chr(b1))
    m.write_byte(chr(b2))
    m.write_byte(chr(b3))
    m.write_byte(chr(b4))
   
def mergeSortMMap(A, result, start, end):
    """recursively mergesort A[start:end] into result"""

    if end - start < 8:
      return

    if end - start == 8:
      result.seek(start)
      left = readInt(result)
      right = readInt(result)
      
      if left > right:
        result.seek(start)
        writeInt(result, right)
        writeInt(result, left)
      return

    mid = (end + start)/8*4;
    mergeSortMMap(result, A, start, mid);
    mergeSortMMap(result, A, mid, end);

    result.seek(start)
    
    i = start
    j = mid
    idx = start
    while idx < end:

        A.seek(i)
        Ai = readInt(A)
        Aj = 0;
        if j < end:
            A.seek(j)
            Aj = readInt(A)

        if j >= end or (i < mid and Ai < Aj):
            writeInt(result, Ai)
            i += 4
        else:
            writeInt(result, Aj)
            j += 4

        idx += 4
    
def createRandom(n, name, high=1000):
    """Create file containing n random integers with maximum value"""

    out = open(name, "wb")
    for i in range(n):
        val = random.randint(1,high)
        
        out.write(chr((val >> 24) & 255))
        out.write(chr((val >> 16) & 255))
        out.write(chr((val >> 8) & 255))
        out.write(chr(val & 255))
        
    out.close()
    
"""
Change Log
----------
2014.05.23 createRandom
           defect: out = open(name, "w")
           fix:    out = open(name, "wb")
"""
