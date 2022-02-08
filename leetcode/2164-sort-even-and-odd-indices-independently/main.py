"""
    1st: sort

    Time    O(NlogN)
    Space   O(N)
    91 ms, faster than 37.50%
"""


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odds = []
        evens = []
        for i in range(n):
            if i % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        odds.sort(key=lambda x: -x)
        evens.sort()
        res = []
        while len(evens) > 0 or len(odds) > 0:
            if len(evens) > 0:
                res.append(evens.pop(0))
            if len(odds) > 0:
                res.append(odds.pop(0))
        return res
