"""
    graph: indegree to sum the source index

    Time    O(N)
    Space   O(N)
    1802 ms, faster than 33.33%
"""


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        indegrees = defaultdict(int)
        for i in range(n):
            dest = edges[i]
            indegrees[dest] += i
        max_score = 0
        res = -1
        for key in indegrees:
            score = indegrees[key]
            if score > max_score:
                max_score = score
                res = key
            elif score == max_score and key < res:
                res = key
        return res
