class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        1st approach: brute force
        - for each bar, calculate the height from the current index to the index 0

        Time	O(n^2)
        Space	O(1)
        TLE
        """
        res = 0
        for i in range(len(heights)):
            maxheight = sys.maxsize
            cnt = 1
            for j in range(i, -1, -1):
                maxheight = min(maxheight, heights[j])
                temp = maxheight * cnt
                res = max(res, temp)
                cnt += 1
        return res
