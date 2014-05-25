# All Pairs Shortest Path Implementation

import sys

# key are vertices; each edge has weight and that's encoded as well
graph = {0: {1: 2, 4:4},
         1: {2:3},
         2: {3:5, 4:1 },
         3: {0: 8},
         4: {3:3}}

past_fib = {}

def fibonacci(n):
    """Return nth fibonacci number memorizing past solutions"""

    if n in past_fib:
        return past_fib[n]
    
    if n == 0 or n == 1:
        past_fib[n] = 1
        return 1

    total = fibonacci(n-1) + fibonacci(n-2)
    past_fib[n] = total
    return total

def allPairsShortestPath(g):
    """Return distance structure as computed"""

    dist = {}
    pred = {}
    for u in g:
        dist[u] = {}
        pred[u] = {}
        for v in g:
            dist[u][v] = sys.maxint
            pred[u][v] = None

        dist[u][u] = 0
        pred[u][u] = None

        for v in g[u]:
            dist[u][v] = g[u][v]
            pred[u][v] = u

    for mid in g:
        for u in g:
            for v in g:
                newlen = dist[u][mid] + dist[mid][v]
                if newlen < dist[u][v]:
                    dist[u][v] = newlen
                    pred[u][v] = pred[mid][v]

    return (dist,pred)

        
def constructShortestPath(s, t, pred):
    """Reconstruct shortest path from s to t using information in pred"""
    path = [t]

    while t != s:
        t = pred[s][t]
        
        if t is None:
            return None
        path.insert(0, t)
    
    return path
