from collections import *

"""
    1st: hashtable + sort
    - count the frequency of every number
    - for every number, find its pair, and remove it from the hashtbale
    - dont forget to sort the array so that we can start with small numbers

    Time    O(N + NlogN + N)
    Space   O(N)
    1416 ms, faster than 20.00%
"""


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1:
            return []
        counter = Counter(changed)
        changed.sort()
        res = []
        for i in range(n):
            x = changed[i]
            if counter[x] == 0:
                continue
            dub = x * 2
            if counter[dub] > 0:
                counter[dub] -= 1
                counter[x] -= 1
                res.append(x)
            else:
                return []
        return res
