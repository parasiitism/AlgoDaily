"""
    1st: DFS + BFS
    - backtracking to find the cycle
    - get the cycle from the starting node
    - BFS to get rest of the nodes from each node in the cycle

    Time    O(N)
    Space   O(N)
    9667 ms, faster than 9.09%
"""


class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        # step 1: backtracking to find the cycle
        route = []
        visited = set()

        def find_cycle(node, parent):
            if node in visited:
                return (True, node)
            for nb in g[node]:
                if nb == parent:
                    continue
                visited.add(node)
                route.append(node)
                foundVisited, res = find_cycle(nb, node)
                if foundVisited:
                    return (foundVisited, res)
                route.pop()
                visited.remove(node)

            return (False, None)

        _, start = find_cycle(0, None)

        # step 2: get the cycle from the starting node
        idx = route.index(start)
        cycle_nodes = route[idx:]

        # step 3: BFS to get rest of the nodes from each node in the cycle
        res = n * [2**32]
        q = [(node, 0) for node in cycle_nodes]
        while len(q) > 0:
            node, steps = q.pop(0)
            if steps >= res[node]:
                continue
            res[node] = steps
            for nb in g[node]:
                q.append((nb, steps + 1))
        return res
