"""
    Kruskal
    - imagine "digging a new well" = "connect a pipe to a hidden House-0"

    Time    O(NlogN)
    Space   O(N)
    734 ms, faster than 33.55% 
"""


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        uf = UnionFind(n)

        # crux
        for i in range(1, n+1):
            pipes.append([0, i, wells[i-1]])

        # Kruskal's
        connections = sorted(pipes, key=lambda x: x[2])
        res = 0
        for a, b, c in connections:
            rootA = uf.find(a)
            rootB = uf.find(b)
            if rootA != rootB:
                uf.union(a, b)
                res += c
        return res


class UnionFind(object):
    def __init__(self, N):
        self.count = N
        self.ids = {}
        self.caps = {}
        for i in range(N+1):
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
