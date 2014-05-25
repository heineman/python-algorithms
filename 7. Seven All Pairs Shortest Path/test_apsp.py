# testing code for module (including project)

from apsp import *
from project_apsp import *

assert(89 == fibonacci(10))

dist,pred = allPairsShortestPath(graph)
assert(7 == dist[0][3])

assert([0,4,3] == constructShortestPath(0,3,pred))

assert(15 == dist[1][0])
assert([1, 2, 4, 3, 0] == constructShortestPath(1,0,pred))

assert([2] == constructShortestPath(2,2,pred))
       
assert(0 == minEditDistance('test', 'test'))
assert(4 == minEditDistance('test', ''))
assert(4 == minEditDistance('', 'test'))

assert(3 == minEditDistance('Grates', 'Create'))
assert(3 == minEditDistance('Create', 'Grates'))
assert(1 == minEditDistance('walk', 'talk'))

# simply replace each letter one at a time
assert(4 == minEditDistance('walk', 'pore'))

# remove first and last letter
assert(2 == minEditDistance('waltz', 'malt'))
