"""
    Minimum Spanning Tree:
    - find out the minium cost/edges to connect all the nodes

	This appraoch is a classic approach using Prim's Algorithm
	- I did it with a heap and a hashtable

	Optimization
	- use finbonacci heap to sort the edges

	️️⭐️ Kruskal vs Prim, we should use Prim
	- when the graph is dense, number of edges(E) > number of vertices(V) ,like E > V^2

	Time	O(E log V) E: number of edges, V: number of vertices
	Space	O(E + V) hashtable + heap

	ref:
	- https://www.youtube.com/watch?v=YyLaRffCdk4
"""
import heapq
from collections import defaultdict


class Solution(object):
    def minimumCost(self, edges):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(edges) == 0:
            return []
        visited = {}
        for edge in edges:
            visited[edge[0]] = False
            visited[edge[1]] = False
        res = []
        pq = []
        # establish connections table
        connections = defaultdict(list)
        for a, b, cost in edges:
            connections[a].append((a, b, cost))
            connections[b].append((b, a, cost))
        # pick the first vertex as a starting point
        start = edges[0][0]
        visited[start] = True
        for edge in edges:
            if edge[0] == start or edge[1] == start:
                heapq.heappush(pq, (edge[2], edge[0], edge[1]))
        # always get the edge with smallest route from the min-heap
        while len(pq) > 0:
            cost, a, b = heapq.heappop(pq)
            foundA = visited[a]
            foundB = visited[b]
            # put the ajacent nodes into the min-heap
            if foundA and foundB:
                continue
            elif foundA:
                visited[b] = True
                res.append((a, b, cost))
                for edge in connections[b]:
                    heapq.heappush(pq, (edge[2], edge[0], edge[1]))
            elif foundB:
                visited[a] = True
                res.append((a, b, cost))
                for edge in connections[b]:
                    heapq.heappush(pq, (edge[2], edge[0], edge[1]))

        # if there is any unvisited node, it means there is no edge can reach to the node, therefore return []
        for key in visited:
            if visited[key] == False:
                return []

        return res
