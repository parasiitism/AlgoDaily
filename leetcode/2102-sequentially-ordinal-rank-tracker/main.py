from sortedcontainers import SortedList
from bisect import *

"""
    1st: binary search

    Time of add     O(logN) -> O(N)  binary search is O(logN) but insertion is O(N), it just happens to be fast in python
    Space           O(N)
    1372 ms, faster than 42.23%
"""


class SORTracker:

    def __init__(self):
        self.items = []
        self.idx = 0

    def add(self, name: str, score: int) -> None:
        insort(self.items, (-score, name))

    def get(self) -> str:
        res = self.items[self.idx][1]
        self.idx += 1
        return res


"""
    2nd: sorted list
    - actually this is a data structure which uses binary search

    Time of add     O(logN) -> O(N)  binary search is O(logN) but insertion is O(N), it just happens to be fast in python
    Space           O(N)
    1056 ms, faster than 80.62%
"""


class SORTracker:

    def __init__(self):
        self.items = SortedList()
        self.idx = 0

    def add(self, name: str, score: int) -> None:
        self.items.add((-score, name))

    def get(self) -> str:
        res = self.items[self.idx][1]
        self.idx += 1
        return res
