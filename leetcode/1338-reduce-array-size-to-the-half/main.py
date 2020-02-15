from typing import List
from collections import Counter

"""
    1st: hashtable + sort
    1. count the occurence of each number
    2. sort the occurences
    3. subtract the occurences one by one to get the result

    Time    O(N + NlogN)
    Space   O(N)
    636 ms, faster than 72.36%
"""


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        ht = Counter(arr)
        occurences = []
        for key in ht:
            occurences.append(ht[key])
        occurences = sorted(occurences, reverse=True)
        cur = 0
        for i in range(len(occurences)):
            cur += occurences[i]
            if cur >= n//2:
                return i + 1
        return 0
