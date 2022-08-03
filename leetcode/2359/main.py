"""
    Graph
    - BFS from both nodes
    - the result is the min amongst min(distFromA, distFromB)

    Time    O(N)
    Space   O(N)
    2096 ms, faster than 40.00%
"""


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def bfs(start):
            seen = set()
            distances = n * [None]
            q = [(start, 0)]
            while len(q) > 0:
                node, steps = q.pop(0)
                if node == -1:
                    continue
                if node in seen:
                    continue
                seen.add(node)
                distances[node] = steps
                dest = edges[node]
                if steps < distances[node]:
                    continue
                q.append([dest, steps + 1])
            return distances

        destsFromA = bfs(node1)
        destsFromB = bfs(node2)

        res_idx = -1
        res_dist = 2**32
        for i in range(n):
            a = destsFromA[i]
            b = destsFromB[i]
            if a == None or b == None:
                continue
            dist = max(a, b)
            if dist < res_dist:
                res_idx = i
                res_dist = dist

        return res_idx
