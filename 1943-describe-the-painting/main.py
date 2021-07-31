from collections import *

"""
    1st: line sweeping
    
    e.g. [[1,4,5],[4,7,7],[1,7,9]]

    hashtable: 
    1: 5 + 9
    4: -5 + 7
    7: -7 -9
    
    prefix sum of sorted keys
    1: 14
    4: 14 - 5 + 7 = 16
    7: 16 - 7 - 9 = 0

    result:
    [[1, 4, 14], [4, 7, 16]]

    Time    O(N + NlogN)
    Space   O(N)
    1644 ms, faster than 33.81%
"""


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        N = len(segments)
        ht = Counter()
        for i in range(N):
            s, e, c = segments[i]
            ht[s] += c
            ht[e] -= c
        tuples = []
        for key in ht:
            tuples.append((key, ht[key]))
        tuples.sort()
        pfs = 0
        res = []
        for i in range(len(tuples)-1):
            s, c = tuples[i]
            e, _ = tuples[i+1]
            pfs += c
            if pfs > 0:
                res.append((s, e, pfs))
        return res
