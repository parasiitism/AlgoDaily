"""
    1st: greedy
    - don't deletion, just append
    - at EOD, make sure the constructed array is with an even length

    Time    O(N)
    Space   O(N)
    1304 ms, faster than 66.67%
"""


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res = []
        for x in nums:
            if len(res) % 2 == 0 or x != res[-1]:
                res.append(x)
        if len(res) % 2 != 0:
            res.pop()
        return len(nums) - len(res)
