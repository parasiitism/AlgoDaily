"""
    1st: kadane's algorithm
    - on top of to lc53
    - for every number, there are only 2 possibilities, + or -
        so we can create 2 arrays
    - and then run a kadane's algo
    - caution: since the description says we can only start from +, we need to change the kadane's a bit for odd indices

    Time    O(4N)
    Space   O(2N)
    1064 ms, faster than 100.00%
"""


class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        A = []
        B = []
        for i in range(n):
            if i % 2 == 0:
                A.append(nums[i])
                B.append(-nums[i])
            else:
                A.append(-nums[i])
                B.append(nums[i])
        x = self.kadane(A)
        y = self.kadane(B[1:])
        return max(x, y)

    def kadane(self, nums):
        cur = -(2**32)
        res = -(2**32)
        for i in range(len(nums)):
            if i % 2 == 0:
                cur = max(cur + nums[i], nums[i])
            else:
                cur += nums[i]
            res = max(res, cur)
        return res
