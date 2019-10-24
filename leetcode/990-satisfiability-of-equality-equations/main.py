"""
    1st: union find
    - get all the symbols
    - process the equations with ==, union the connected symbols in groups
    - process the equations with !=, in each equation, if two symbols are in a same group, return False
    - return True if no contradiction is found

    Time    O(NlogN -> N^2) logN if the distribution of the symbols is balanced
    Space   O(N)
    32 ms, faster than 69.32%
"""


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        symbols = set()
        for eq in equations:
            symbols.add(eq[0])
            symbols.add(eq[3])
        uf = UnionFind(symbols)
        for eq in equations:
            if eq[1:3] == '==':
                uf.union(eq[0], eq[3])
        for eq in equations:
            if eq[1:3] == '!=':
                rootA = uf.find(eq[0])
                rootB = uf.find(eq[3])
                if rootA == rootB:
                    return False
        return True


class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.ids = {}
        self.caps = {}
        for vertex in vertices:
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
