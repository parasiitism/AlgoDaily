"""
    1st: optimizeed brute force with hashtable
    
    Time    O(RCRC) worst
    Space   O(RCRC)
    7532 ms, faster than 29.20%
"""


class Solution(object):
    def minimizeTheDifference(self, mat, target):
        hs = {0}
        for row in mat:
            _hs = set()
            for x in set(row):  # the crux
                for cand in hs:
                    _hs.add(x + cand)
            hs = _hs
        closest = 2**32
        for cand in hs:
            if abs(cand - target) < abs(closest - target):
                closest = cand
        return abs(closest - target)
