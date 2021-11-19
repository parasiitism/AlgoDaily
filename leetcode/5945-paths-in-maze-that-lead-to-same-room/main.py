from collections import *
from bisect import *

"""
    1st: graph, brute force

    Time    O(N^3)
    Space   O(N^2)
    LTE 67 / 67 test cases passed, but took too long.
"""


class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        g = defaultdict(set)
        for u, v in corridors:
            g[u].add(v)
            g[v].add(u)

        for u in g:
            g[u] = sorted(list(g[u]))

        cands = []
        for i in g:
            A = g[i]
            for j in A:
                if j <= i:
                    continue
                B = g[j]
                for k in B:
                    if k <= j:
                        continue
                    cands.append([i, j, k])
        # print(cands)
        res = 0
        for chain in cands:
            head = chain[0]
            tail = chain[-1]
            if head in g[tail]:
                res += 1
        return res


"""
    2nd: graph, binary search

    Time    O(N^3)
    Space   O(N^2)
    LTE 67 / 67 test cases passed, but took too long.
"""


class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        g = defaultdict(set)
        for u, v in corridors:
            g[u].add(v)
            g[v].add(u)

        for u in g:
            g[u] = sorted(list(g[u]))

        cands = []
        for i in g:
            A = g[i]
            idxA = bisect_right(A, i)
            if idxA >= len(A):
                continue
            for _j in range(idxA, len(A)):
                j = A[_j]
                B = g[j]
                idxB = bisect_right(B, j)
                if idxB >= len(B):
                    continue
                for _k in range(idxB, len(B)):
                    k = B[_k]
                    cands.append([i, j, k])
        res = 0
        for chain in cands:
            head = chain[0]
            tail = chain[-1]
            if head in g[tail]:
                res += 1
        return res


"""
    3rd: optimize the 1) by only storing larger node IDs
    Time    O(N^3)
    Space   O(N^2)
    4140 ms, faster than 100.00% 
"""


class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        g = defaultdict(set)
        for u, v in corridors:
            _min = min(u, v)
            _max = max(u, v)
            g[_min].add(_max)
        cands = []
        for i in range(1, n+1):
            for j in g[i]:
                for k in g[j]:
                    cands.append([i, j, k])
        res = 0
        for chain in cands:
            head = chain[0]
            tail = chain[-1]
            if tail in g[head]:
                res += 1
        return res
