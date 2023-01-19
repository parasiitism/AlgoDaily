"""
    1st: sorted container
    - sorted container is a trick in python

    Time    O(N^2) -> O(N^2) SortedList.add = array insort which takes O(N) times worst
    Space   O(N)
"""
from sortedcontainers import SortedList


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sl = SortedList()
        res = 0
        for x in instructions:
            left = sl.bisect_left(x)
            right = sl.bisect_right(x)
            res += min(left, len(sl) - right)
            res %= 10**9 + 7
            sl.add(x)
        return res


"""
    2nd: Binary Indexed Tree
    - index of BIT(instructions[i]): count

    Time    O(N log10**5)
    Space   O(10**5)
"""


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        BIT = BinaryIndexedTree(10**5)
        res = 0
        for i in range(len(instructions)):
            x = instructions[i]
            left = BIT.getSum(x-1)
            right = BIT.getSum(x)
            res += min(left, i - right)
            res %= 10**9 + 7
            BIT.update(x, 1)
        return res


class BinaryIndexedTree(object):
    def __init__(self, n):
        self.fenwickTree = (n+1) * [0]

    def update(self, i, val):
        k = i
        while k < len(self.fenwickTree):
            self.fenwickTree[k] += val
            k += k & -k

    def getSum(self, i):
        s = 0
        k = i
        while k > 0:
            s += self.fenwickTree[k]
            k -= k & -k
        return s
