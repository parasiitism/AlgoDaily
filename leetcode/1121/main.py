"""
    math
    - learned from others

    For example 2: A = [5,6,6,7,8]
    we have two 6, so we have to split A into at least two subsequence.
    We want K = 3 numbers in each subsequence, so we need at least K * 2 = 6 numbers.
    But we have only A.length = 5 numbers.

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        ht = Counter(nums)
        most_freq = max(ht.values())
        return len(nums) >= k * most_freq
