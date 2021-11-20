"""
    1st: union find
    - for every request, loop thru the restrictions and see if we should connect

    Time    O(ABlogN) A: requests, B: restrictions
    Space   O(N)
    6788 ms, faster than 29.55%
"""


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        res = []
        for u, v in requests:
            shouldConnect = True
            a, b = uf.find(u), uf.find(v)
            if a != b:
                for _u, _v in restrictions:
                    x, y = uf.find(_u), uf.find(_v)
                    if (a, b) == (x, y) or (a, b) == (y, x):
                        shouldConnect = False
                        break
            if shouldConnect:
                uf.union(u, v)
            res.append(shouldConnect)
        return res


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.roots = {}
        self.caps = {}
        for i in range(n):
            self.roots[i] = i
            self.caps[i] = 1

    def find(self, key):
        if key not in self.roots:
            return None
        cur = key
        while cur != self.roots[cur]:
            cur = self.roots[cur]
        return cur

    def union(self, p, q):
        if p not in self.roots or q not in self.roots:
            return
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
        if p not in self.roots or q not in self.roots:
            return None
        return self.find(p) == self.find(q)
