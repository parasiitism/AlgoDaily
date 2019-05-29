"""
    2nd approach: same logic + followup: print the result array

    Time    O(n)
    Space   O(n)
    48 ms, faster than 62.45%
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res = 0
        prev = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > prev:
                prev = nums[i]
                count += 1
            else:
                if count > res:
                    res = count
                prev = nums[i]
                count = 1
        if count > res:
            res = count
        return res


"""
    2nd approach: same logic + followup: print the result array

    Time    O(n)
    Space   O(n)
    60 ms, faster than 57.69%
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res = []
        cur = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > cur[-1]:
                cur.append(nums[i])
            else:
                if len(cur) > len(res):
                    res = cur
                cur = [nums[i]]
        if len(cur) > len(res):
            res = cur
        return res
