"""
    1st:  brute force

    Time    ON(N^3)
    Space   O(1)
    1726 ms, faster than 16.67%
"""


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                d1 = nums[j] - nums[i]
                for k in range(j+1, n):
                    d2 = nums[k] - nums[j]
                    if d1 == d2 == diff:
                        res += 1
        return res


"""
    2nd: hashtable

    Time    ON(N)
    Space   O(N)
    41 ms, faster than 75.00%
"""


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set()
        res = 0
        for x in nums:
            if x - diff in seen and x - diff * 2 in seen:
                res += 1
            seen.add(x)
        return res
