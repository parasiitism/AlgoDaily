"""
    prefix sum + binary search
    - for subsequences, we can just sort
    - to maximize the length of a subsequence we can start from the smallest numbers

    Time    O(NlogN + QlogN)
    Space   O(N)
    191 ms, faster than 20.00%
"""


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pfs = 0
        pfss = []
        for i in range(len(nums)):
            pfs += nums[i]
            pfss.append(pfs)
        res = []
        for target in queries:
            idx = self.upperBsearch(pfss, target)
            res.append(idx)
        return res

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
