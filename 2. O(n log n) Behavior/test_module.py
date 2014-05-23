# test Module

from merge import *
from insertion import *

import random

x = []
assert([] == copymergesort([]))
assert([2] == copymergesort([2]))
       
assert([1,2] == copymergesort([1,2]))
assert([1,2] == copymergesort([2,1]))

# random trials
x = range(128)
random.shuffle(x)

assert(range(128) == copymergesort(x))

x = range(128)
random.shuffle(x)

mergeSort(x)
assert(range(128) == x)

# test insertion sort as well

x = range(128)
random.shuffle(x)

insertion(x)
assert(range(128) == x)
