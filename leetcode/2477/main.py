"""
    DFS
    - In each DFS, the minimum liter of gas required is the math.ceil(ppl/seat)

    Time    O(N)
    Space   O(H)
    5166 ms, faster than 9.09%
"""


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1

        # build the graph from the edges
        g = {}
        for i in range(n):
            g[i] = []
        for u, v in roads:
            g[u].append(v)
            g[v].append(u)

        # run a DFS
        seen = set()
        seen.add(0)

        def dfs(node):
            if node in seen:
                return 0, 0
            seen.add(node)
            liters, ppl = 0, 1
            for nb in g[node]:
                _liters, _ppl = dfs(nb)
                liters += _liters
                ppl += _ppl
            liters += math.ceil(ppl/seats)
            return liters, ppl

        return sum(dfs(x)[0] for x in g[0])
