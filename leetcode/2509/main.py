"""
    math, tree
    1. find the path
    2. find the LCA
    3. result = the length from nodeA to LCA + the length from nodeB to LCA

    Time    O(Q*logN)
    Space   O(logN)
"""


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        for a, b in queries:
            path_a = self.find_path(a)
            path_b = self.find_path(b)
            temp = self.find_LCA(path_a, path_b)
            res.append(temp)
        return res

    def find_path(self, x):
        path = []
        while x > 0:
            path.append(x)
            x //= 2
        return path

    def find_LCA(self, path_a, path_b):
        seen = {}
        for i in range(len(path_a)):
            x = path_a[i]
            seen[x] = i
        for i in range(len(path_b)):
            if path_b[i] in seen:
                L = seen[path_b[i]] + 1
                return i + L
        return -1
