from bisect import *
from collections import *

"""
    1st: hashtable + binary search

    Time of init()      O(N)
    Time of query()     O(logN)
    Space               O(N)
    1508 ms, faster than 100.00%
"""


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.ht = defaultdict(list)
        n = len(arr)
        for i in range(n):
            x = arr[i]
            self.ht[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        indices = self.ht[value]
        s = bisect_left(indices, left)
        e = bisect_right(indices, right)
        return e - s
