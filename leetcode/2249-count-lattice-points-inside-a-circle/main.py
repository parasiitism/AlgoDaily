"""
    hashtable

    Time    O(N * R^2)
    Space   O(N * R^2)
    9782 ms, faster than 33.33%
"""


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        lattices = set()
        for x, y, r in circles:
            for i in range(x-r, x+r+1):
                for j in range(y-r, y+r+1):
                    dd = (i - x)**2 + (j - y)**2
                    if dd <= r*r:
                        lattices.add((i, j))
        return len(lattices)
