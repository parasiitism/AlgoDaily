from collections import *

"""
    1st: hashtable
    
    Time    O(N)
    Space   O(N)
    1653 ms, faster than 25.00%
"""


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        res = []
        for x in nums:
            if ctr[x] == 1 and x-1 not in ctr and x+1 not in ctr:
                res.append(x)
        return res
