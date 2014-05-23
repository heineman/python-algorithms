# test code from module

from binary import *
from bst import *
import random

sample = [1,2]
assert(contains(sample, 1))
assert(contains(sample, 2))
assert(not contains(sample, 3))

sample = [1,2,3,4]
assert(bs_contains(sample,1) == 0)
assert(bs_contains(sample,2) == 1)
assert(bs_contains(sample,3) == 2)
assert(bs_contains(sample,4) == 3)

assert(bs_contains([],1) == -1)

x = [1, 2, 3]
insertInPlace(x, 4)
assert([1,2,3,4] == x)
insertInPlace(x, 0)
assert([0,1,2,3,4] == x)
insertInPlace(x, 2.5)
assert([0,1,2,2.5,3,4] == x)


# binary tree tests
bt = BinaryTree()
assert(bt.root == None)

# check ranomd insertion and validate presence
x = range(128)
random.shuffle(x)
for i in x:
    bt.add(i)

for i in range(128):
    assert(bt.contains(i))

# delete one by one, and validate remaining ones are present
# Note: this test case caught misnamed attributed 'val'
for i in range(128):
    bt.remove(i)
    assert(not bt.contains(i))
    for j in range(i+1, 128):
        assert(bt.contains(j))

        


