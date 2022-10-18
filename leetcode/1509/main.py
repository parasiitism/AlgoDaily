"""
    Moving averge with gorwing window
    
    learned from others
    - https://leetcode.com/problems/minimize-maximum-of-array/discuss/2706521/JavaC%2B%2BPython-Prefix-Sum-Average-O(n)

    Time    O(N)
    Space   O(1)
    1939 ms, faster than 60.00%
"""


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pfs = 0
        res = 0
        for i in range(len(nums)):
            x = nums[i]
            pfs += x
            res = max(res, math.ceil(pfs/(i+1)))
        return res
