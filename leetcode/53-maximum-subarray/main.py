import sys
"""
    3rd approach: dynamic programming, kadan's algorithm
    - for each item, store the max among itself, or extend the previous sum with itself
      e.g. dp[i] chooses between dp[i-1]+nums[i] and nums[i]
    - the result is the largest dp[i]
    - optimize the 2nd approach by using store one variable for dp array cos for each item
    we just need to compare with previous item result

    Time	O(n)
    Space	O(1)
    56 ms, faster than 37.09% 

    ref:
    - https://www.youtube.com/watch?v=2MmGzdiKR9Y
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -sys.maxsize
        prevSum = -sys.maxsize
        for num in nums:
            prevSum = max(prevSum+num, num)
            res = max(res, prevSum)
        return res


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(a))

"""
    follow up: print the subarray with the max sum
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -sys.maxsize
        resArr = []
        prevSum = -sys.maxsize
        prevSumArr = []
        for num in nums:
            # update current sum and array
            if prevSum+num >= num:
                prevSum += num
                prevSumArr.append(num)
            else:
                prevSum = num
                prevSumArr = [num]
            # update global result and result array
            if prevSum >= res:
                res = prevSum
                resArr = prevSumArr[:]
        return res, resArr


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(a))
