from collections import *

"""
    Minimum Spanning Tree: 
    - find out the minium cost/edges to connect all the nodes

	This appraoch is a classic approach using Union Find, aka. Kruskal Algorithm, to merge the edges with minimum weight
	1. basically we sort the input edges
	2. pop the edges one by one from minimum
	3. union the vertexs and put the vertexs in the result set if the vertexs are not connected
	5. the edges in the set are the result

	Optimization
	- if the weights are dicrete and the range is known, sort the edges with a bucket-sort in linear time O(n)

	⭐️ Kruskal vs Prim, we should use Kruskal
	- when the graph is sparse, number of edges(E) ~= number of vertices(V) ,like E ~= V
	- when the edges are already sorted or if we can sort them in linear time

	Time		O(E log E) + O(V log V) <= sort the edges + union find
	Space		O(V) edges in union find
  	E: number of edges, V: number of vertices

	ref: https://www.youtube.com/watch?v=5xosHRdxqHAs
"""


class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(N)
        connections = sorted(connections, key=lambda x: x[2])
        res = 0
        for a, b, c in connections:
            rootA = uf.find(a)
            rootB = uf.find(b)
            if rootA != rootB:
                uf.union(a, b)
                res += c
        # if the nodes are not in a same group
        if uf.count > 1:
            return []
        return res


class UnionFind(object):
    def __init__(self, N):
        self.count = N
        self.ids = {}
        self.caps = {}
        for i in range(1, N+1):
            self.ids[i] = i
            self.caps[i] = 1

    def get_count(self):
        return self.count

    def get_groups(self):
        groups = defaultdict(set)
        for node in self.ids:
            root = self.find(node)
            groups[root].add(node)
        return groups

    def find(self, key):
        # loop to find to ultimate root
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        # attach to the larger tree
        if self.caps[pId] < self.caps[qId]:
            self.ids[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.ids[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1
