"""
    1st: math

    Time    O(N + log(X))
    Space   O(1)
    56 ms, faster than 27.27%
"""


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        return self.gcd(smallest, largest)

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
