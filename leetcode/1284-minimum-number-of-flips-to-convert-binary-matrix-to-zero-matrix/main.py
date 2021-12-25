from collections import deque

"""
    1st: BFS + hashtable

    Time    O(2^RC)
    Space   O(2^RC)
    84 ms, faster than 33.46%
"""


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        q = deque()
        q.append((mat, 0))
        seen = set()
        while len(q) > 0:
            node, steps = q.popleft()
            key = self.genKey(node)
            if self.ifZero(key):
                return steps
            if key in seen:
                continue
            seen.add(key)
            for i in range(R):
                for j in range(C):
                    clone = self.copy(node)
                    clone[i][j] = (node[i][j] + 1) % 2
                    if i-1 >= 0:
                        clone[i-1][j] = (node[i-1][j] + 1) % 2
                    if i+1 < R:
                        clone[i+1][j] = (node[i+1][j] + 1) % 2
                    if j-1 >= 0:
                        clone[i][j-1] = (node[i][j-1] + 1) % 2
                    if j+1 < C:
                        clone[i][j+1] = (node[i][j+1] + 1) % 2
                    q.append((clone, steps + 1))
        return -1

    def genKey(self, mat):
        arr = []
        for row in mat:
            arr += row
        return tuple(arr)

    def ifZero(self, key):
        return not any(key)

    def copy(self, mat):
        R, C = len(mat), len(mat[0])
        res = []
        for i in range(R):
            res.append(C * [0])
            for j in range(C):
                res[i][j] = mat[i][j]
        return res
