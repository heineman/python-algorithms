Module 9 Single-Source Shortest Path

This module contains the SingleSourceShortestPath algorithm which determines
the shortest accumulated total cost to all vertices emanating from a single
source vertex. In addition to computing the cost, it records information 
that allows you to recover the actual shortest path between the source and
any vertex in the graph.

Files contained within this module include:

  * sssp.py            Implementation using adjacency list representation
  * bheap.py           Implementation of BInary Heap
  * project_bheap.py   Project demonstrating MinimumSpanningTree using BinaryHeap 
  * test_sssp.py       Testing code

To demonstrate the code in action use a graph representation such as the following:

graph = { 0: {1: 6, 3: 18, 2: 8},
          1: {4: 11},
          2: {3: 9},
          3: {},
          4: {5: 3},
          5: {3: 4, 2: 7}
         }

That is, graph is a dictionary whose keys are the vertices and the value is itself
a dictionary of vertex : weight pairs. Thus in the above representation, there
are three edges emanating from vertex 0: (0,1), (0,2), and (0,3). Edge (0,1) has a weight
of 6, edge (0,3) has a weight of 18, and edge (0,2) has a weight of 8.

With such a graph, invoke singleSourceShortestPathand be prepared to receive a 
dist and pred matrix containing the solution

   >>> dist, pred = singleSourceShortestPath(graph,0)
 
The dist structure is a dictionary whose value dist[i] represents the minimum 
cost of any path between the source vertex (in this case, 0) and j. pred[i] 
represents the previous vertex to use when traversing the shortest path from the
source vertex to i. To recover the solution, invoke following:

   >>> solution(s, v, dist, pred)

where s and v are vertices in the graph, dist is the distance structure and
pred is the predecessor link structure, both returned from singleSourceShortestPath


Change Log

1. 2014.05.24    bheap.py [insert function]
                 defect: allocate storage on insert otherwise insert
                         after deletion causes duplicate references.
                 fix:    self.elements[i] = [priority, id]
