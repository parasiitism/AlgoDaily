import sys

"""
    1st approach: brute force

    Time    O(n^2)
    Space   O(1)
    TLE
"""


class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        res = -sys.maxsize
        B = A + A
        for i in range(len(A)):
            cur = 0
            for j in range(i, i+len(A)):
                cur += B[j]
                res = max(res, cur)
        return res


"""
    2nd approach: kadane's variant, learned from others
    - there are 2 cases:
        1. the maxSumSubarray is in the middle
        2. we can form maxSumSubarray by subtracting the minSumSubarray in the middle
    - see ./idea.png

    corner case: If all numbers are negative, the sum will be zero. In this case, just return maxSum

    ref:
    - https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass

    Time    O(n)
    Space   O(1)
    472 ms, faster than 83.82% 
"""


class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        # kadane for max sum subarray
        maxSum = -sys.maxsize
        curMaxSum = -sys.maxsize
        # kadane for min sum subarray
        minSum = sys.maxsize
        curMinSum = sys.maxsize
        # iterate
        for num in nums:
            # min
            curMinSum = min(curMinSum+num, num)
            minSum = min(minSum, curMinSum)
            # max
            curMaxSum = max(curMaxSum+num, num)
            maxSum = max(maxSum, curMaxSum)
        # substract the min sum subarray in the middle
        total = sum(nums)
        noMiddle = total - minSum
        # corner case: if all numbers are negative, the sum will be zero
        # in this case, just return maxSum
        if noMiddle == 0:
            return maxSum
        return max(maxSum, noMiddle)


s = Solution()

a = [1, -2, 3, -2]
print(s.maxSubarraySumCircular(a))

a = [5, -3, 5]
print(s.maxSubarraySumCircular(a))

a = [3, -1, 2, -1]
print(s.maxSubarraySumCircular(a))

a = [3, -2, 2, -3]
print(s.maxSubarraySumCircular(a))

a = [-2, -3, -1]
print(s.maxSubarraySumCircular(a))
