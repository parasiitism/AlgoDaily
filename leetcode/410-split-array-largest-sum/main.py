from typing import List
import sys

"""
    1st: dynamic programming, recursion + hashtable
    - similar to lc813, 1043, 1335

    LTE 
    26 / 27 test cases passed.
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        return self.dfs(nums, m, {})

    def dfs(self, nums, m, ht):
        if m == 1:
            return sum(nums)
        n = len(nums)
        key = (n, m)
        if key in ht:
            return ht[key]

        pfs = 0
        res = sys.maxsize
        for i in range(len(nums) - 1):
            pfs += nums[i]
            temp = self.dfs(nums[i+1:], m - 1, ht)
            cur = max(pfs, temp)
            res = min(res, cur)
        ht[key] = res
        return res


"""
    2nd: 
    optimization 1: using an index to indicate the start instead of doing array slicing

    LTE
"""


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        return self.dfs(nums, 0, k, {})

    def dfs(self, nums, start, k, cache):
        if k == 1:
            return sum(nums[start:])
        key = (start, k)
        if key in cache:
            return cache[key]
        pfs = 0
        res = 2**32
        for i in range(start, len(nums)):
            pfs += nums[i]
            sfs = self.dfs(nums, i+1, k - 1, cache)
            cur = max(pfs, sfs)
            res = min(res, cur)
        cache[key] = res
        return res


"""
    2nd:
    - similar to lc813, 1043, 1335
    - optimize 1st approach with suffix sum and use start index instead of array slicing

    Time    O(M * N^2)
    Space   O(MN)
    7508 ms, faster than 5.66%
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        suffixSums = len(nums) * [0]
        sfs = 0
        for i in range(len(nums)-1, -1, -1):
            sfs += nums[i]
            suffixSums[i] = sfs

        return self.dfs(nums, 0, m, {}, suffixSums)

    def dfs(self, nums, start, m, ht, suffixSums):
        if m == 1:
            return suffixSums[start]
        key = (start, m)
        if key in ht:
            return ht[key]

        pfs = 0
        res = sys.maxsize
        for i in range(start, len(nums) - 1):
            pfs += nums[i]
            sfs = self.dfs(nums, i+1, m - 1, ht, suffixSums)
            cur = max(pfs, sfs)
            res = min(res, cur)
        ht[key] = res
        return res


"""
    3rd: bottom up iteration
    - similar to lc813, 1043, 1335
    - tbh, it is hard to transform the recursive approach into this approach....

    ref:
    - https://www.youtube.com/watch?v=Cpy4T_rVuPk

    Time    O(M * N^2)
    Space   O(MN)
    5856 ms, faster than 18.00%
"""


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)

        preffixSums = (n+1) * [0]
        for i in range(n):
            preffixSums[i+1] = preffixSums[i] + nums[i]

        dp = []
        for i in range(n + 1):
            dp.append((m + 1) * [sys.maxsize])

        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(i):
                    cur = max(dp[k][j-1], preffixSums[i] - preffixSums[k])
                    dp[i][j] = min(dp[i][j], cur)

        return dp[-1][-1]


"""
    4th: binary search
    - the best approach for this problem, easier to implement and best in time complexity
    - the idea is to binary-search the subarray sum, (inversely proportional)
        the smaller the subsarray sum, the more number of subarrays
        the bigger the subsarray sum, the fewer number of subarrays

    Time    O(NlogS)
    Space   O(1)
"""


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = 2**32
        while left < right:
            mid = (left + right) // 2
            # not intuitive for this condition, but the idea is mid is too big to leads to a small number of pieces,
            # we need to have smaller mid, so we search on the left
            if self.countSubarray(nums, mid) <= k:
                right = mid
            else:
                left = mid + 1
        return left

    def countSubarray(self, nums, suggestion):
        cur_sum = 0
        split_cnt = 0
        for x in nums:
            if cur_sum + x <= suggestion:
                cur_sum += x
            else:
                cur_sum = x
                split_cnt += 1
        return split_cnt + 1
