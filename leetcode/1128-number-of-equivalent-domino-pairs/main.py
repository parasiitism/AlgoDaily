from collections import defaultdict

"""
    1st: hastable
    
    Time O(n)
    Space O(n)
    212 ms, faster than 64.26%
"""


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        res = 0
        ht = defaultdict(int)
        for a, b in dominoes:
            if (a, b) in ht:
                res += ht[(a, b)]
            ht[(a, b)] += 1
            if a != b:
                ht[(b, a)] += 1
        return res
