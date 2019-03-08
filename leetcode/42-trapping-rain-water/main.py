class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ma = 0
        forward = []
        for h in height:
            forward.append(ma)
            ma = max(ma, h)

        ma = 0
        backward = []
        for i in range(len(height)-1, -1, -1):
            h = height[i]
            backward = [ma] + backward
            ma = max(ma, h)

        res = 0
        for i in range(len(forward)):
            f = forward[i]
            b = backward[i]
            m = min(f, b)
            if m > height[i]:
                res += m - height[i]
        return res


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
