"""
    1st math
    
    Time    O(N)
    Space   O(N) the result
    1872 ms, faster than 100.00%
"""


class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(len(queries)):
            t, idx = queries[i]
            r = t % (2 * n)
            if r < n and idx < n - r:
                res.append(nums[idx + r])
            elif r > n and idx < r - n:
                res.append(nums[idx])
            else:
                res.append(-1)
        return res
