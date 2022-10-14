"""
    Math: gcd

    Time    O(NlogM)
    Space   O(H)
    108 ms, faster than 100.00%
"""


class Solution:
    def minimumSplits(self, nums: List[int]) -> int:
        n = len(nums)
        gcd = nums[0]
        res = 1
        for i in range(1, n):
            x = nums[i]
            temp = self.findGcd(gcd, x)
            if temp > 1:
                gcd = temp
            else:
                res += 1
                gcd = x
        return res

    def findGcd(self, a, b):
        if b == 0:
            return a
        return self.findGcd(b, a % b)
