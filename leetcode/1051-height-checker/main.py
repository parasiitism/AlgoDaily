"""
    1st approach: sort

    Time    O(n)
    Space   O(n)
    16 ms, faster than 95.04%
"""


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        sortedNums = sorted(heights)
        for i in range(len(heights)):
            if sortedNums[i] != heights[i]:
                res += 1
        return res
