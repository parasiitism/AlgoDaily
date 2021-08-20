from collections import *

"""
    1st: BFS + hashtable
    - optimize the approach with a deque

    Time    O(N)
    Space   O(N)
    1736 ms, faster than 100.00%
"""


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        seen = set()
        connections = defaultdict(list)
        for u, v in edges:
            connections[u].append(v)
            connections[v].append(u)
        q = deque()
        q.append(start)
        while len(q) > 0:
            node = q.popleft()
            if node == end:
                return True
            if node in seen:
                continue
            seen.add(node)
            for nb in connections[node]:
                q.append(nb)
        return False
