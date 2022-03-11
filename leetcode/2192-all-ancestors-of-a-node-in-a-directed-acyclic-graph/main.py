from collections import *

"""
    1st: BFS

    Time    O(N)
    Space   O(N)
    2228 ms, faster than 11.11%
"""


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegrees = defaultdict(list)
        for u, v in edges:
            indegrees[v].append(u)
        res = []
        for i in range(n):
            seen = set()
            ancestors = []
            q = deque()
            q.append(i)
            while len(q) > 0:
                node = q.popleft()
                if node in seen:
                    continue
                if node != i:
                    ancestors.append(node)
                seen.add(node)
                for p in indegrees[node]:
                    q.append(p)
            res.append(sorted(ancestors))
        return res
