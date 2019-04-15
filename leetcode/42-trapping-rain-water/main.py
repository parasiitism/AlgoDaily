"""
    1st approach:
    - calculate max from the front
    - calculate max from the end
    - the min(forward[i], backward[i]) - height[i] is the volumn of the trapping water on that cell

    Time    O(3n)
    Space   O(3n)
    76 ms, faster than 13.97%
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxH = 0
        forward = []
        for h in height:
            forward.append(maxH)
            maxH = max(maxH, h)

        maxH = 0
        backward = []
        for i in range(len(height)-1, -1, -1):
            backward.insert(0, maxH)
            maxH = max(maxH, height[i])

        res = 0
        for i in range(len(forward)):
            f = forward[i]
            b = backward[i]
            m = min(f, b)
            if m > height[i]:
                res += m - height[i]
        return res


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
