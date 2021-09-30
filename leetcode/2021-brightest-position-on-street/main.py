from collections import *

"""
    1st: line sweep + sort

    Time    O(NlogN) N = start+end of every light
    Space   O(N)
    1188 ms, faster than 100.00% 
"""


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        brightness = Counter()
        points = set()
        for p, r in lights:
            s = p-r
            e = p+r+1
            brightness[s] += 1
            brightness[e] -= 1
            points.add(s)
            points.add(e)
        keys = sorted(list(points))
        pfs = 0
        res = -(2**32)
        best = 0
        for p in keys:
            pfs += brightness[p]
            if pfs > best:
                best = pfs
                res = p
        return res
