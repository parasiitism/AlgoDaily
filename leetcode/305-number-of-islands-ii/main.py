"""
    2nd approach: union find
    - construct union find
    - for each operation: if coord not yet added
        1. add it to the union find
        2. union the cells if the adjacent cells are added

    Time    O(m*n + k*log(m*n))
    Space   O(m*n) union find
    656 ms, faster than 29.19%
"""


class UnionFind(object):
    def __init__(self, n):
        self.count = 0
        self.ids = {}
        self.caps = {}
        for i in range(n):
            self.ids[i] = -1
            self.caps[i] = 1

    def add(self, key):
        if key not in self.ids:
            return None
        self.ids[key] = key
        self.count += 1

    # O(logn) if balanced
    def find(self, key):
        # loop to find to ultimate root
        if key not in self.ids:
            return None
        cur = key
        while cur != -1 and cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    # O(logn) if balanced
    def union(self, p, q):
        if p not in self.ids or q not in self.ids:
            return
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


class Solution(object):

    def __init__(self):
        self.uf = None

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        self.uf = UnionFind(m*n)
        res = []
        for i, j in positions:
            self.putIsland(i, j, m, n)
            res.append(self.uf.count)
        return res

    def putIsland(self, i, j, row, col):
        if i < 0 or i >= row or j < 0 or j >= col:
            return
        x = col * i + j
        if self.uf.find(x) > -1:
            return
        self.uf.add(x)  # uf.count + 1
        if i - 1 >= 0:
            if self.uf.find(x-col) > -1:
                self.uf.union(x, x-col)  # uf.count - 1
        if i + 1 < row:
            if self.uf.find(x+col) > -1:
                self.uf.union(x, x+col)  # uf.count - 1
        if j - 1 >= 0:
            if self.uf.find(x-1) > -1:
                self.uf.union(x, x-1)  # uf.count - 1
        if j + 1 < col:
            if self.uf.find(x+1) > -1:
                self.uf.union(x, x+1)  # uf.count - 1


a = 3
b = 3
c = [[0, 0], [0, 1], [1, 2]]
print(Solution().numIslands2(a, b, c))

a = 3
b = 3
c = [[0, 0], [0, 1], [1, 2], [2, 1]]
print(Solution().numIslands2(a, b, c))

a = 3
b = 3
c = [[0, 1], [1, 0], [1, 2], [2, 1], [1, 1]]
print(Solution().numIslands2(a, b, c))

a = 1
b = 2
c = [[0, 1], [0, 0]]
print(Solution().numIslands2(a, b, c))
