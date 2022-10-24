"""
    brute force

    Time    O(N^2)
    Space   O(1)
    437 ms, faster than 100.00% 
"""


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            x = nums[i]
            for j in range(i, n):
                x = math.gcd(x, nums[j])
                if x == k:
                    res += 1
                elif x < k:  # optimization
                    break
        return res
