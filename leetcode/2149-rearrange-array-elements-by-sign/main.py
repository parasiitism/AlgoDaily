"""
    1st: array

    Time    O(N)
    Space   O(N)
    8172 ms, faster than 20.00%
"""


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positives = []
        negatives = []
        for x in nums:
            if x >= 0:
                positives.append(x)
            else:
                negatives.append(x)
        res = []
        for i in range(n):
            if i % 2 == 0:
                res.append(positives.pop(0))
            else:
                res.append(negatives.pop(0))
        return res
