Module 7 All Pairs Shortest Path

This module contains the AllPairsShortestPath algorithm which uses the technique
of Dynamic Programming to determine the shortest accumulated total of a path 
between any two vertices in a graph. In addition to computing the cost, it records
information that allows you to recover the shortest path between two vertices.

Files contained within this module include:

  * apsp.py           Implementation using adjacency matrix representation
  * project_apsp.py   Project demonstrating dynamic programming on minEditDistance
  * test_apsp.py      Testing code

To demonstrate the code in action use a graph representation such as the following:

graph = {0: {1: 2, 4:4},
         1: {2:3},
         2: {3:5, 4:1 },
         3: {0: 8},
         4: {3:3}}

That is, graph is a dictionary whose keys are the vertices and the value is itself
a dictionary of vertex : weight pairs. Thus in the above representation, there
are two edges emanating from vertex 0: (0,1) and (0,4). Edge (0,1) has a weight
of 2 while edge (0,4) has a weight of 4.

With such a graph, invoke allPairsShortestPath and be prepared to receive a 
dist and pred matrix containing the solution

   >>> dist, pred = allPairsShortestPath(graph)
 
The dist structure is a two-dimensional dictionary whose value dist[i][j] represents
the minimum cost of any path between vertices i and j. pred[i][j] represents the 
previous vertex to use when traversing the shortest path from vertex i to j. To 
recover the solutions, invoke following:

   >>> constructShortestPath(s, t, pred)

where s and t are vertices in the graph and pred is the structure returned by 
allPairseShortestPath
