from heapq import *

"""
    1st: maxheap

    Time    O(D)
    Space   O(3)
    65 ms, faster than 8.33%
"""


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount = list(filter(lambda x: x > 0, amount))
        maxheap = [-x for x in amount]
        heapify(maxheap)
        res = 0
        while len(maxheap) > 0:
            if len(maxheap) >= 2:
                a = heappop(maxheap)
                b = heappop(maxheap)
                res += 1
                a += 1
                b += 1
                if a != 0:
                    heappush(maxheap, a)
                if b != 0:
                    heappush(maxheap, b)
            elif len(maxheap) == 1:
                a = heappop(maxheap)
                res += 1
                a += 1
                if a != 0:
                    heappush(maxheap, a)
        return res


"""
    2nd: math

    Time    O(1)
    Space   O(1)
    63 ms, faster than 8.33%
"""


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), math.ceil(sum(amount)/2))
