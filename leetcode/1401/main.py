"""
    Binary search

    Time    O(2Rlog2R)
    Space   O(1)
"""


class Solution:
    def checkOverlap(self, r: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        for y in range(yCenter - r, yCenter + r + 1):
            left_x = self.bsearch_left(
                xCenter - r, xCenter, xCenter, yCenter, y, r)
            right_x = self.bsearch_right(
                xCenter, xCenter + r + 1, xCenter, yCenter, y, r) - 1
            if y1 <= y <= y2:
                if x1 <= right_x and x2 >= left_x:
                    return True
        return False

    def bsearch_left(self, left, right, xCenter, yCenter, y, r):
        while left < right:
            mid = (left + right) // 2
            if (mid - xCenter)**2 + (y - yCenter)**2 <= r**2:
                right = mid
            else:
                left = mid + 1
        return left

    def bsearch_right(self, left, right, xCenter, yCenter, y, r):
        while left < right:
            mid = (left + right) // 2
            if (mid - xCenter)**2 + (y - yCenter)**2 > r**2:
                right = mid
            else:
                left = mid + 1
        return left
