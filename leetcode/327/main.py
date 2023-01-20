from sortedcontainers import SortedList
from bisect import *

"""
    1st: sorted container
    - a python handy tool to make a mutable sorted array

    Time    O(NlogN) -> O(N^2) since SortedList.add() uses bisect.insort() which use array.insert() taking O(N) under the hood
    Space   O(N)
    Runtime 2247ms beats 96.14%
"""


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        sl = SortedList([0])
        res = 0
        pfs = 0
        for i in range(n):
            pfs += nums[i]
            # if lower is negative, pfs-lower must be >= pfs
            right = sl.bisect_right(pfs - lower)
            # if lower is positve, pfs-upper must be <= pfs
            left = sl.bisect_left(pfs - upper)
            # the range in between
            res += right - left
            sl.add(pfs)
        return res


"""
    2nd: Binary Indexed Tree + binary search
    - similar to 1st, but using a BIT to make a mutable sorted array
    - but the implementation is error-prone, i failed to find the right combination of +1, -1 for the binary search

    Time    O(NlogN)
    Space   O(N)
    Runtime 3440ms beats 70.17%
"""


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)

        pfs = 0
        pfss = [0]
        for i in range(n):
            pfs += nums[i]
            pfss.append(pfs)
        pfss = sorted(pfss)

        BIT = BinaryIndexedTree(len(pfss))
        BIT.update(bisect_left(pfss, 0), 1)  # the 0 in pfss
        res = 0
        pfs = 0
        for i in range(len(nums)):
            pfs += nums[i]
            right = BIT.getSum(bisect_right(pfss, pfs - lower) - 1)
            left = BIT.getSum(bisect_left(pfss, pfs - upper) - 1)
            res += right - left
            BIT.update(bisect_left(pfss, pfs), 1)
        return res


class BinaryIndexedTree(object):
    def __init__(self, n):
        self.fenwickTree = (n+1) * [0]

    def update(self, i, val):
        k = i + 1
        while k < len(self.fenwickTree):
            self.fenwickTree[k] += val
            k += k & -k

    def getSum(self, i):
        s = 0
        k = i + 1
        while k > 0:
            s += self.fenwickTree[k]
            k -= k & -k
        return s
