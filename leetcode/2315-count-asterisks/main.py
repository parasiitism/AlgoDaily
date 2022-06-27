from collections import *

"""
    hashtable
    
    Time   O(N)
    Space   O(N)
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        words = s.split('|')
        res = 0
        for i in range(len(words)):
            if i % 2 == 0:
                ctr = Counter(words[i])
                res += ctr['*']
        return res
