import sys
"""
    3rd approach: dynamic programming, kadan's algorithm
    - for each item, store the max either itself or extend the previous sum with itself
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

a = [4, 1, -5, 6, -3, 2]
print(Solution().maxSubArray(a))

a = [7, -3, -10, 4, 2, 8, -2, 4, -5, -6]
print(Solution().maxSubArray(a))

a = [-10, 2, 3, -2, 0, 5, -15]
print(Solution().maxSubArray(a))

print("-----")

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
            # we use >= instead of > because we want to include the head if the prevsum == 0
            if prevSum+num >= num:
                prevSum += num
                prevSumArr.append(num)
            else:
                prevSum = num
                prevSumArr = [num]
            # update global result and result array
            # we use >= instead of > because we want to include the head if the prevsum == 0
            if prevSum >= res:
                res = prevSum
                resArr = prevSumArr[:]
        return res, resArr


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(a))

a = [4, 1, -5, 6, -3, 2]
print(Solution().maxSubArray(a))

a = [7, -3, -10, 4, 2, 8, -2, 4, -5, -6]
print(Solution().maxSubArray(a))

a = [-10, 2, 3, -2, 0, 5, -15]
print(Solution().maxSubArray(a))
