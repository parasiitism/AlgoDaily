"""
    1st: Binary Indexed Tree but using brute-force space
    - there might be negative numbers we need to make them positive, 
    so i just add a random offset which big enough to cover the constraints

    Time    O(Nlog100001)
    Space   O(100001)
    Runtime 2149 ms beats 71.8%
"""


from sortedcontainers import SortedList
import bisect


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


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        BIT = BinaryIndexedTree(100001)
        res = 0
        for i in range(n):
            a, b = nums1[i], nums2[i]
            c = a - b
            res += BIT.getSum(20001 + c + diff)
            BIT.update(20001 + c, 1)
        return res


"""
    2nd: binary search
    - everytime we see a new number, we binary search the run sorted list to see if we had seen it before and get the index
    - put the new number to the sorted list

    Time    O(NlogN) -> O(N^2) the worst Time of insort() is O(N)
    Space   O(N)
    Runtime 1210 ms beats 98.95%
"""


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        diffs = []
        res = 0
        for i in range(n):
            a, b = nums1[i], nums2[i]
            d = a - b
            res += bisect.bisect_right(diffs, d + diff)
            bisect.insort(diffs, d)
        return res


"""
    3r: binary search with SortList
    - the logic is the same as 2nd

    Time    O(NlogN) -> O(N^2) the worst Time of insort() is O(N)
    Space   O(N)
    Runtime 1353ms beats 85.72%
"""


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        sl = SortedList()
        res = 0
        for i in range(n):
            a, b = nums1[i], nums2[i]
            d = a - b
            res += sl.bisect_right(d + diff)
            sl.add(d)
        return res
