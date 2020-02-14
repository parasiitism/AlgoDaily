import sys
"""
    Floyd Warshall Algorithm
    - Find the All Pairs Shortest Paths
    - the basic idea is to see if there is a middle node k can connect node i and node j
    - and then update the distance[i][j] if distance[i][k] + distance[k][j] < distance[i][j]

    ref:
    - https://www.youtube.com/watch?v=4OQeCuLYj-4
    - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/discuss/490312/JavaC%2B%2BPython-Easy-Floyd-Algorithm
    - http://alrightchiu.github.io/SecondRound/all-pairs-shortest-pathfloyd-warshall-algorithm.html

    btw, its good to see look at the comparison table in
    - ./compare1.png
    - ./compare2.png

    Time    O(N^3)
    Space   O(N^2)
"""


class Solution(object):
    def floyd(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # construct the 2D matrix
        dis = [n * [sys.maxsize] for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        # see if node middle(k) can connect node i and node j
        # and update the cost if its smaller
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        # the 2d table contains all the shortest/cheapest paths from any node i to any node j
        return dis
