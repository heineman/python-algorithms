# single-source shortest path

from bheap import BHeap
import sys

# sample graph with edge weights
graph = { 0: {1: 6, 3: 18, 2: 8},
          1: {4: 11},
          2: {3: 9},
          3: {},
          4: {5: 3},
          5: {3: 4, 2: 7}
         }
          
def singleSourceShortestPath(graph, s):
    """Compute and return (dist, pred) matrices of computation"""

    pq = BHeap(len(graph))
    dist = {}
    pred = {}
    
    for v in graph:
        dist[v] = sys.maxint
        pred[v] = None
    dist[s] = 0

    for v in graph:
        pq.insert(v, dist[v])

    while not pq.isEmpty():
        u = pq.smallest()
        for v in graph[u]:
            wt = graph[u][v]
            newLen = dist[u] + wt

            if newLen < dist[v]:
                pq.decreaseKey(v, newLen)
                dist[v] = newLen
                pred[v] = u
                
    return (dist, pred)

def solution(s, v, dist, pred):
    """Return path and total information for shortest path from s to v"""

    path = [v]
    total = dist[v]
    while v != s:
        v = pred[v]
        path.insert(0, v)

    return "length=" + str(total) + " " + str(path)
