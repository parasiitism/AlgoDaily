"""
    1st: binary search
    - use Longest Mono-Increasing/Non-decreasing Subsequence

    Time    O(NlogN)
    Space   O(N)
    1220 ms, faster than 47.82%
"""


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        total = 0
        for i in range(k):
            nums = arr[i::k]
            r = self.LMIS(nums)
            total += len(nums) - r
        return total

    def LMIS(self, nums):
        n = len(nums)
        sub = []
        for i in range(n):
            x = nums[i]
            if len(sub) == 0 or x >= sub[-1]:
                sub.append(x)
            else:
                j = self.upperBsearch(sub, x)
                sub[j] = x
        return len(sub)

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right
