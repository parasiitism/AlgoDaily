"""
    math

    Time    O(N^2) worst
    Space   O(1)
    962 ms, faster than 71.43%
"""
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            lcm = nums[i]
            for j in range(i, n):
                y = nums[j]
                lcm = lcm * y // math.gcd(lcm, y)
                if lcm == k:
                    res += 1
                elif lcm > k:
                    break
        return res