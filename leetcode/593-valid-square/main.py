"""
    1st: math
    - 4 smaller distances should be equal (sides)
    - 2 larger distances should be equal too (diagonals)

    Time    O(1)
    Space   O(1)
    16 ms, faster than 89.06%
"""


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        res = []
        points = [p1, p2, p3, p4]
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                temp = self.getLength2(points[i], points[j])
                res.append(temp)
        res = sorted(res)
        return res[0] == res[1] == res[2] == res[3] and res[3] < res[4] and res[4] == res[5]

    def getLength2(self, a, b):
        return (a[0] - b[0])**2 + (a[1] - b[1])**2


s = Solution()

a, b, c, d = [0, 0], [1, 1], [1, 0], [0, 1]
print(s.validSquare(a, b, c, d))

a, b, c, d = [1134, -2539], [492, -1255], [-792, -1897], [-150, -3181]
print(s.validSquare(a, b, c, d))

a, b, c, d = [0, 0], [0, 0], [0, 0], [0, 0]
print(s.validSquare(a, b, c, d))
