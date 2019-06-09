"""
    1st approach
	- if not overlap, result = area A + area B
	- else, result = area A + area B - overlapping area
	use the method in leetcode 836 to determind if the rects overlap
	Time	O(1)
    Space   O(1)
    56 ms, faster than 47.77%
"""


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        if self.isRectangleOverlap(A, B, C, D, E, F, G, H) == False:
            return self.areaOf(A, B, C, D) + self.areaOf(E, F, G, H)
        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        return self.areaOf(A, B, C, D) + self.areaOf(E, F, G, H) - self.areaOf(x1, y1, x2, y2)

    def isRectangleOverlap(self, A, B, C, D, E, F, G, H):
        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        if x1 < x2 and y1 < y2:
            return True
        return False

    def areaOf(self, x1, y1, x2, y2):
        return (x2-x1)*(y2-y1)
