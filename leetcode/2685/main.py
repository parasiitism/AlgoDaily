from collections import *

"""
    DFS
    - we can do the same using Union Find

    Time    O(NN)
    Space   O(N)
"""


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        G = defaultdict(set)
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
        seen = set()
        groups = []
        for i in range(n):
            if i in seen:
                continue
            # BFS
            group = []
            q = [i]
            while len(q) > 0:
                node = q.pop(0)
                if node in seen:
                    continue
                seen.add(node)
                group.append(node)
                for nb in G[node]:
                    q.append(nb)
            groups.append(group)
        # print(groups)
        res = 0
        for group in groups:
            m = len(group)
            complete = True
            for i in range(m):
                for j in range(m):
                    if i == j:
                        continue
                    u = group[i]
                    v = group[j]
                    if v not in G[u]:
                        complete = False
                        break
                if complete == False:
                    break
            res += complete
        return res
