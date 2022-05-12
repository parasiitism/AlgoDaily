from collections import *

"""
    hashtable + sort

    Time    O(Nlog26)
    Space   O(26)
    78 ms, faster than 100.00%
"""


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        ctr = Counter(s)
        keysCounts = []
        for k in ctr:
            keysCounts.append([k, ctr[k]])
        keysCounts.sort(key=lambda x: -x[1])
        pressCountMapping = {}
        for i in range(len(keysCounts)):
            key, _ = keysCounts[i]
            if i < 9:
                pressCountMapping[key] = 1
            elif i < 18:
                pressCountMapping[key] = 2
            else:
                pressCountMapping[key] = 3
        res = 0
        for c in s:
            res += pressCountMapping[c]
        return res
