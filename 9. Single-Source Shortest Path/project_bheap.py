# Prim's MST Algorithm using BHeap

import sys
from bheap import BHeap

graph = { 0: {1: 2, 4: 4, 3: 8},
          1: {0:2, 2: 3},
          2: {1: 3, 4: 1, 3: 5},
          3: {2: 5, 4: 7, 0: 8},
          4: {0: 4, 2: 1, 3: 7}
         }

# Note Prim's algorithm needs to know whether PQ contains vertex. This
# operation is not supported (since it won't be efficient). Fortunately
# with O(n) extra storage, this function creates inqueue[] dictionary
# to keep track of the vertices in the PQ.
def computeMST(graph):
    """Return set of edges that forms MST starting search from s"""

    key = {}
    pred = {}
    inqueue = {}
    for v in graph:
        key[v] = sys.maxint
        pred[v] = None

    # choose any vertex to start from. Use last from previous loop
    key[v] = 0
    pq = BHeap(len(graph))
    for v in graph:
        pq.insert(v, key[v])
        inqueue[v] = True

    while not pq.isEmpty():
        u = pq.smallest()
        inqueue[u] = False
        
        for v in graph[u]:
            if inqueue[v]:
                wt = graph[u][v]
                if wt < key[v]:
                    pred[v] = u
                    key[v] = wt
                    pq.decreaseKey(v, wt)

    return pred

def solution(pred):
    """Produce edge list for MST"""
    
    edges = []
    for v in pred:
        if pred[v] is not None:
            edges.append((pred[v], v))

    return edges
