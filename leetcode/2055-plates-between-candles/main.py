"""
    1st: prefix sum, binary search

    Time    O(NlogN)
    Space   O(N)
    2836 ms, faster than 20.00%
"""


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pfs = 0
        candles = []
        for i in range(len(s)):
            c = s[i]
            if c == '*':
                pfs += 1
            else:
                candles.append((i, pfs))
        # print(candles)
        res = []
        for s, e in queries:
            i = self.bsearch(candles, s, 0)
            j = self.bsearch(candles, e, 1)
            if j > i:
                diff = candles[j][1] - candles[i][1]
                res.append(diff)
            else:
                res.append(0)
        return res

    def bsearch(self, nums, target, leftRight):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid][0]:
                right = mid - 1
            elif target > nums[mid][0]:
                left = mid + 1
            else:
                return mid
        if leftRight == 0:
            return left
        return right
