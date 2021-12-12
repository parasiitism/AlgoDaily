"""
    1st: sort
    - sort by values
    - select the first K items
    - sort by index

    Time    O(NlogN)
    Space   O(N)
    52 ms, faster than 100.00%
"""


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        A = []
        for i in range(len(nums)):
            A.append((nums[i], i))
        A.sort(key=lambda x: -x[0])
        B = A[:k]
        B.sort(key=lambda x: x[1])
        return [B[i][0] for i in range(len(B))]
