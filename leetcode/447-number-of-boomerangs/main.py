"""
    1st approach: hashtable
    - for each point, calculate the distance between other points and count the points with the same distance
    - iterate through the hashtable, for each point with the same distance, we have n-1 points to pair with
    
    e.g.
         1
         |
    0____|____2
         |
         |
         3

    edges are
    01
    02
    03
    10
    12
    13
    20
    21
    23
    30
    31
    total = 4x(4-1) = 12
    
    TIme    O(n^2)
    Space   O(n)
    632 ms, faster than 83.17%
"""


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        # for each point, calculate the distance between other points
        for i in range(len(points)):
            ht = {}
            x1, y1 = points[i]
            for j in range(len(points)):
                if i == j:
                    continue
                x2, y2 = points[j]
                d = (x1-x2)**2 + (y1-y2)**2
                # count the points with the same distance
                if d not in ht:
                    ht[d] = 1
                else:
                    ht[d] += 1
            # for each point with the same distance, we have n-1 points to pair with
            for key in ht:
                num = ht[key]
                count += num*(num-1)
        return count


# 2
a = [[0, 0], [1, 0], [2, 0]]
print(Solution().numberOfBoomerangs(a))

# 4
a = [[0, 0], [1, 0], [2, 0], [3, 0]]
print(Solution().numberOfBoomerangs(a))

# 12
a = [[0, 0], [1, 0], [2, 0], [2, 0]]
print(Solution().numberOfBoomerangs(a))

# 20
a = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
print(Solution().numberOfBoomerangs(a))
