from collections import *

"""
    1st: hashtable
    - counter the frequency of every number at even indices and odd indices
    - sort the frequencies, the result must be n - odds[-1][0] - evens[-1][0]

    Time    O(NlogN)
    Space   O(N)
    2008 ms, faster than 50.00%
"""


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        even_dict = Counter()
        odd_dict = Counter()

        for i in range(len(nums)):
            if i % 2 == 0:
                even_dict[nums[i]] += 1
            else:
                odd_dict[nums[i]] += 1

        odds = sorted(((v, k) for k, v in odd_dict.items()))
        evens = sorted(((v, k) for k, v in even_dict.items()))

        # if no repeat, then just choose the high freq
        if odds[-1][1] != evens[-1][1]:
            return n - odds[-1][0] - evens[-1][0]

        # if a key is frequent in at both even and odd indices,
        # then we have 2 scenarios to choose either
        cand0 = n - odds[-1][0] - (evens[-2][0] if len(evens) > 1 else 0)
        cand1 = n - evens[-1][0] - (odds[-2][0] if len(odds) > 1 else 0)

        return min(cand0, cand1)
