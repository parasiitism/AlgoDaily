"""
    BFS + hashtable

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        restricted_set = set(restricted)
        res = 0
        q = [0]
        seen = set()
        while len(q) > 0:
            node = q.pop(0)
            if node in restricted_set:
                continue
            if node in seen:
                continue
            seen.add(node)
            res += 1
            for nb in g[node]:
                q.append(nb)
        return res
