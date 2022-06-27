from collections import *

"""
    Graph: Union Find

    e.g.
    n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
    
    nodes in each union
    0: {0, 2, 4, 5}
    1: {1, 6}
    3: {3}

    so, these are all the unreachable nodes from each node 
    0: 3
    1: 5
    2: 3
    3: 6
    4: 3
    5: 3
    5: 5
    Consider that an edge is bidirectonial, the result is half of the above sum

    Time    O(NlogN)
    Space   O(N)
    3259 ms, faster than 68.47%
"""


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        roots = Counter()
        for i in range(n):
            r = uf.find(i)
            roots[r] += 1
        res = 0
        for r in roots:
            count = roots[r]
            res += count * (n - count)
        return res // 2


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.roots = {}
        self.caps = {}
        for i in range(n):
            self.roots[i] = i
            self.caps[i] = 1

    def getCount(self):
        return self.count

    def find(self, key):
        if key not in self.roots:
            return None
        cur = key
        while cur != self.roots[cur]:
            cur = self.roots[cur]
        return cur

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        if self.caps[pId] < self.caps[qId]:
            self.roots[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.roots[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1

    def isConnect(self, p, q):
        return self.find(p) == self.find(q)
