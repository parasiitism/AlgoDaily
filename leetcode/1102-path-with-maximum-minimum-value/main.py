import heapq

"""
    1st approach: Dijkstra
    - use a priority queue to choose the next step with the maximum value
    - keep track of the mininum value along the path

    learned from others
    - https://leetcode.com/problems/path-with-maximum-minimum-value/discuss/322926/Simple-Python-Priority-Queue-Solution

    Time    O(RC)
    Space   O(RC)
    1404ms beats 54%
"""


class Solution(object):
    def maximumMinimumPath(self, matrix):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rl, cl = len(matrix), len(matrix[0])
        q = [(-matrix[0][0], 0, 0)]
        seen = set()
        while len(q) > 0:
            # we pop the top item from maxHeap
            # so we can ensure that this path must have the maximum min value
            t, x, y = heapq.heappop(q)
            if x == rl - 1 and y == cl - 1:
                return -t
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rl and 0 <= ny < cl and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    heapq.heappush(q, (max(t, -matrix[nx][ny]), nx, ny))
