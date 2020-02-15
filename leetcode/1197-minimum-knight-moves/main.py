"""
    1st: brute force BFS
    Time    O(8^N)
    Space   O(8^N)
    LTE
"""


class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dirs = [(1, 2), (2, 1), (2, -1), (1, -2),
                (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        q = [(0, 0, 0)]
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i == x and j == y:
                return steps
            for di, dj in dirs:
                nextI = i + di
                nextJ = j + dj
                q.append((nextI, nextJ, steps + 1))

        return 0


s = Solution()
print(s.minKnightMoves(0, 1))  # 3
print(s.minKnightMoves(2, 1))  # 1
print(s.minKnightMoves(5, 5))  # 4
print(s.minKnightMoves(7, 7))  # 6


"""
    2nd: BFS + hashtable
    - do the same thing as 1st approach
    - use a hashtable to avoid redundant calculation

    Time    <<< O(8^N)
    Space   <<< O(8^N)
    7576 ms, faster than 5.04%
"""


class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dirs = [(1, 2), (2, 1), (2, -1), (1, -2),
                (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        q = [(0, 0, 0)]
        hs = set()
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i == x and j == y:
                return steps
            for di, dj in dirs:
                nextI = i + di
                nextJ = j + dj
                if (nextI, nextJ) in hs:
                    continue
                hs.add((nextI, nextJ))
                q.append((nextI, nextJ, steps + 1))
        return 0
