import math

"""
    ref:
    - https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=525149
    - https://christianhill.co.uk/blog/overlapping-circles/
    - https://scipython.com/book/chapter-8-scipy/problems/p84/overlapping-circles/
    - https://dev.to/bacchu/area-of-intersecting-circles--36l0
"""


class Solution(object):
    def computeArea(self, x1, y1, r1, x2, y2, r2):
        """
        :type x1: int   <= center x of circle1
        :type y1: int   <= center y of circle1
        :type r1: int   <= radius of circle1
        :type x2: int   <= center x of circle2
        :type y2: int   <= center y of circle2
        :type r2: int   <= radius of circle2

        :rtype: float <= area
        """
        centerDist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return self.computeAreaBetween(r1, r2, centerDist)

    def computeAreaBetween(self, r1, r2, dist):
        # checking
        if dist >= abs(r1 + r2):
            # they dont overlap at all
            return 0
        elif dist <= abs(r1-r2):
            # a circle inside another circle
            rMin = min(r1, r2)
            return math.pi * rMin ** 2

        r1Square = r1 ** 2
        r2Square = r2 ** 2
        distSquare = dist ** 2

        # cos(A) = (b^2 + c^2 - a^2) / 2bc
        cos1 = (r1Square + distSquare - r2Square) / (2.0 * r1 * dist)
        cos2 = (r2Square + distSquare - r1Square) / (2.0 * r2 * dist)

        # get the theta
        theta1 = math.acos(cos1)
        theta2 = math.acos(cos2)

        # sum 2 areas of the circle's segment cut off by the chord intersection
        # area of one side = theta * b^2 - 0.5 * b^2 * sine(2 * theta)
        area1 = (theta2 * r2Square) - (0.5 * r2Square * math.sin(2.0*theta2))
        area2 = (theta1 * r1Square) - (0.5 * r1Square * math.sin(2.0*theta1))

        return area1 + area2


# normal cases
print("--- normal cases ---")
print(Solution().computeArea(0, 0, 3, 5, 0, 3))
print(Solution().computeArea(0, 0, 3, 5, 0, 4))
# same as
print(Solution().computeAreaBetween(3, 3, 5))
print(Solution().computeAreaBetween(3, 4, 5))

# one circle is inside another one
print("--- one circle is inside another one ---")
print(Solution().computeArea(0, 0, 10, 5, 0, 2))

# touch at one point
print("--- touch at one point ---")
print(Solution().computeArea(0, 0, 3, 6, 0, 3))

# dont overlap at all
print("--- dont overlap at all ---")
print(Solution().computeArea(0, 0, 3, 10, 0, 3))
