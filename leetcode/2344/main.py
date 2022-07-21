"""
    math
    1. find the GCD of numsDivide
    2. sort the nums
    3. find the index of the first gcd in sorted nums

    Time    O(NlogD)
    Space   O(1)
    1075 ms, faster than 22.22%
"""


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd = numsDivide[0]
        for x in numsDivide:
            gcd = self.findGcd(x, gcd)
        nums.sort()
        for i in range(len(nums)):
            x = nums[i]
            if gcd % x == 0:
                return i
        return -1

    def findGcd(self, a, b):
        if b == 0:
            return a
        return self.findGcd(b, a % b)
