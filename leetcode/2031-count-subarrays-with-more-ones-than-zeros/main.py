from collections import *
"""
    1st: hashtable
    - transform zeros to -1 in nums
    - construct prefixSum along the iteration, and count the occurence of every prefixSum
    - observation: prefixSum > 0 means an array has 1s more than 0s
    - since there are only -1 and 1
        - if x == -1, the diff between counter[pfs-1] and counter[pfs] is the number of subarray which 1s more than 0s
        - if x == 1, we don't care about the curent number of prefixSum
    
    e.g.    [ 0,  1,  1,  0,  1]
    
    Iterations:
    -1: Counter({0: 1, -1: 1})
        pfs = -1
        diff = 0
    1:  Counter({0: 2, -1: 1})
        pfs = 0
        diff = 1
    1:  Counter({0: 2, -1: 1, 1: 1})
        pfs = 1
        diff = 3
    -1: Counter({0: 3, -1: 1, 1: 1})
        pfs = 0
        diff = 1
    1:  Counter({0: 3, 1: 2, -1: 1})
        pfs = 1
        diff = 4
    
    Sum all the diffs = 9

    Time    O(N)
    Space   O(N)
    1028 ms, faster than 100.00%
"""


class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        posNegOnes = [-1 if x == 0 else 1 for x in nums]
        counter = Counter()
        counter[0] = 1
        res, pfs, diff = 0, 0, 0
        for x in posNegOnes:
            pfs += x
            if x == -1:
                diff -= counter[pfs]
            else:
                diff += counter[pfs-1]
            counter[pfs] += 1
            res += diff
            res %= 10**9 + 7
        return res
