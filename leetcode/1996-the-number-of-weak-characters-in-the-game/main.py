
from collections import *
"""
    1st: hashtable + sort
    - sort the characters
    - group the characters by attack level
    - iterate from right
        - for every the maxDefense level we have, count the number of characters in this group having smaller defense level
        - update the defense level
    - in this way, we can make sure that the result represent the distinct set of characters

    Time    O(NlogN)
    Space   O(N)
    2404 ms, faster than 100.00%
"""


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        n = len(properties)
        res = 0
        ht = defaultdict(list)
        max_d = -1

        for a, d in properties:
            ht[a] += [d]

        keys = list(ht.keys())
        keys.sort(key=lambda x: -x)

        for key in keys:
            for d in ht[key]:
                if d < max_d:
                    res += 1
            for d in ht[key]:
                max_d = max(max_d, d)

        return res
