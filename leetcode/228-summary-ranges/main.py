"""
    1st approach: intervals
    - if the last interval ends at cur-1, we extend the last interval
    - else we create a new interval and append it to the intervals array

    Time    O(2n)
    Space   O(n)
    20 ms, faster than 65.41%
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        first = nums[0]
        intvs = [[first, first]]
        for i in range(1, len(nums)):
            num = nums[i]
            if num == intvs[-1][1]+1:
                intvs[-1][1] = num
            else:
                x = [num, num]
                intvs.append(x)
        res = []
        for a, b in intvs:
            if a == b:
                res.append(str(a))
            else:
                res.append(str(a)+'->'+str(b))
        return res
