"""
    1st: union find
    - basically we, at least, need N-1 edge to connect N nodes
    - so we just have to find how many nodes which are not connected

    Time    O(NlogN) <- if connection tree(s) is balanced
    Space   O(N)
    564 ms, faster than 52.34%
"""


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.ids = {}
        self.caps = {}
        for vertex in range(n):
            self.ids[vertex] = vertex
            self.caps[vertex] = 1

    def getCount(self):
        return self.count

    def find(self, key):
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


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        uf = UnionFind(n)
        for a, b in connections:
            uf.union(a, b)
        return uf.getCount() - 1


"""
    2nd: idea but use arrays instead hashtable

    Time    O(NlogN) <- if connection tree(s) is balanced
    Space   O(N)
    536 ms, faster than 78.84%
"""


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.ids = []
        self.caps = n * [1]
        for i in range(n):
            self.ids.append(i)

    def find(self, key):
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


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        uf = UnionFind(n)
        for a, b in connections:
            uf.union(a, b)
        return uf.count - 1
