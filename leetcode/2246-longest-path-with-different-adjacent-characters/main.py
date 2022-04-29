from heapq import *

"""
    1st: DFS + heap
    - at each node, calculate 2 of the longest paths from branches

    Time    O(Nlog2) -> O(N)
    Space   O(N)
    2601 ms, faster than 40.49%
"""


class Solution:

    def __init__(self):
        self.res = 0

    def longestPath(self, parent: List[int], s: str) -> int:
        tree = [[] for i in range(len(s))]
        for idx, p in enumerate(parent):
            if p >= 0:
                tree[p].append(idx)

        def dfs(idx):
            minheap = [0]
            for child in tree[idx]:
                length = dfs(child)
                if s[idx] != s[child]:
                    minheap.append(length)

            minheap = nlargest(2, minheap)
            self.res = max(self.res, sum(minheap) + 1)
            return max(minheap) + 1

        dfs(0)
        return self.res
