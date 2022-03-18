"""
    1st: binary search

    Time    O(NlogN)
    Space   O(N)
    141 ms, faster than 60.00%
"""


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        keyIndices = []
        for i in range(n):
            if nums[i] == key:
                keyIndices.append(i)
        res = []
        for i in range(n):
            L, R = self.bsearch(keyIndices, i)
            if 0 <= L < len(keyIndices) and abs(keyIndices[L] - i) <= k:
                res.append(i)
            elif 0 <= R < len(keyIndices) and abs(i - keyIndices[R]) <= k:
                res.append(i)
        return res

    def bsearch(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid, mid
        return right, left
