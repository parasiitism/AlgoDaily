from itertools import *

"""
    1st: lexicographical permutation algorithm
    - leetcode 31

    Time    O(NM)
    Space   O(N)
    57 ms, faster than 100.00%
"""


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n_str = str(n)
        cands = [1, 22, 122, 333, 1333, 4444, 14444, 22333,
                 55555, 122333, 155555, 224444, 666666, 1224444]
        res = 1224444
        for cand in cands:
            s = str(cand)
            if len(s) < len(n_str):
                continue
            if cand > n:
                res = min(res, cand)
                continue
            nums = [int(c) for c in s]
            while True:
                self.nextPermutation(nums)
                _s = ''.join([str(x) for x in nums])
                _res = int(_s)
                if _res > n:
                    res = min(res, _res)
                    break
                if _s == s:
                    break
        return res

    # reuse leetcode31
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 1
        while i - 1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            self.reverse(nums, 0, n-1)
            return

        pivot = i - 1

        j = n - 1
        while j - 1 >= 0 and nums[j] <= nums[pivot]:
            j -= 1

        nums[pivot], nums[j] = nums[j], nums[pivot]

        self.reverse(nums, i, n-1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
