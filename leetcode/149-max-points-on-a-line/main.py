from collections import *

"""
    1st: brute force with math + hashtable
    - for every point, find the slope to any other points
    - use gcd find the integers for m = dy/dx to represent the slope to avoid the precesion problem

    Time    O(N^2 log(max(A,B))
    Space   O(N^2)
    77 ms, faster than 30.05%
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        res = 0
        for i in range(n):
            ht = defaultdict(int)  # [slope = (x, y)] : count
            redundant = 0
            seenMost = 0  # the seen-most ht[slope]
            for j in range(i+1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                # 2 points are the same
                if dx == 0 and dy == 0:
                    redundant += 1
                    continue
                gcd = self.getGcd(dx, dy)
                dx //= gcd
                dy //= gcd
                slope = (dx, dy)
                ht[slope] += 1
                seenMost = max(seenMost, ht[slope])
            # 3 things: the seen-most ht[slope]+ redundant + current point
            res = max(res, seenMost + redundant + 1)
        return res

    def getGcd(self, a, b):
        if b == 0:
            return a
        return self.getGcd(b, a % b)
