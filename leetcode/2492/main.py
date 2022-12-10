"""
    graph: BFS, hashtable
    - run a BFS to see which edges are connect to the network where 1 and N are in
    - the result is the min cost amongst all the connected edges

    Time    O(E)
    Space   O(E)
    3473 ms, faster than 66.67%
"""


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for i in range(len(roads)):
            u, v, d = roads[i]
            g[u].append((v, i))
            g[v].append((u, i))
        q = [1]
        used_road_ids = set()
        while len(q) > 0:
            node = q.pop(0)
            for nb, idx in g[node]:
                if idx in used_road_ids:
                    continue
                used_road_ids.add(idx)
                q.append(nb)
        min_score = 2**32
        for road_id in used_road_ids:
            min_score = min(min_score, roads[road_id][2])
        return min_score
