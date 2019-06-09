import math

"""
    1st approach: brute-force math

    a, b, c are length of the sides
    p = (a + b + c)/2.0
    area = sqrt(p * (p-a) * (p-b) * (p-c))

    Time    O(n^3)
    Space   O(1)
    352 ms, faster than 12.45%
"""


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    area = self.calArea(points[i], points[j], points[k])
                    res = max(res, area)
        return res

    def calArea(self, A, B, C):
        a = self.calSide(A, B)
        b = self.calSide(B, C)
        c = self.calSide(C, A)
        p = (a + b + c)/2.0
        # if the triangle is invalid, e.g. not a + b > c, this part will be less than 0
        if p * (p-a) * (p-b) * (p-c) < 0:
            return 0
        return math.sqrt(p * (p-a) * (p-b) * (p-c))

    def calSide(self, A, B):
        x1, y1 = A[0], A[1]
        x2, y2 = B[0], B[1]
        return math.sqrt((x1 - x2)**2 + (y1 - y2) ** 2)


a = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
print(Solution().largestTriangleArea(a))


a = [[-35, 19], [40, 19], [27, -20], [35, -3], [44, 20],
     [22, -21], [35, 33], [-19, 42], [11, 47], [11, 37]]
print(Solution().largestTriangleArea(a))
