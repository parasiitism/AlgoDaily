"""
    1st: sort + union find
    1. sort the logs by time
    2. union find each log
    3. if the total number of groups == 1, return that timestamp

    Time    O(nlogn)
    Space   O(n)
    108 ms, faster than 85.31%
"""


class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        logs = sorted(logs, key=lambda x: x[0])
        uf = UnionFind(N)
        for t, a, b in logs:
            uf.union(a, b)
            if uf.count == 1:
                return t
        return -1


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.ids = {}
        self.caps = {}
        for i in range(n):
            self.ids[i] = i
            self.caps[i] = 1

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
