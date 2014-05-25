# test module and project code

from heap import *
from project_heap import *

x = range(20)
heapsort(x)
assert(range(20) == x)

x = [2]
heapsort(x)
assert([2] == x)

# evaluate projects also

assert(2 == kthSmallest(range(10),3))
assert(0 == kthSmallest(range(10),1))
assert(9 == kthSmallest(range(10),10))
