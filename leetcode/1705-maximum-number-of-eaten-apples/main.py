from heapq import *

"""
    1st: brute-force with minheap

    Time    O(ADlogAD)
    Space   O(AD)
    LTE because A*D can be huge
"""
from heapq import *


class Solution(object):
    def eatenApples(self, apples, days):
        n = len(apples)
        res = 0
        minheap = []
        for i in range(n):
            a = apples[i]
            r = days[i]
            for _ in range(a):
                heappush(minheap, i+r)
            while len(minheap) > 0 and minheap[0] <= i:
                heappop(minheap)
            if len(minheap) > 0:
                heappop(minheap)
                res += 1
        i = n
        while len(minheap) > 0:
            while len(minheap) > 0 and minheap[0] <= i:
                heappop(minheap)
            if len(minheap) > 0:
                heappop(minheap)
                res += 1
            i += 1
        return res


"""
    2nd: minheap, optimized with count

    Time    O(AlogA)
    Space   O(A)
    652 ms, faster than 86.08%
"""


class Solution(object):
    def eatenApples(self, apples, days):
        n = len(apples)
        res = 0
        minheap = []
        for i in range(n):
            a = apples[i]
            r = days[i]
            heappush(minheap, [i+r, a])
            while len(minheap) > 0 and minheap[0][0] <= i:
                heappop(minheap)
            if len(minheap) > 0:
                minheap[0][1] -= 1
                if minheap[0][1] == 0:
                    heappop(minheap)
                res += 1
        i = n
        while len(minheap) > 0:
            toRoot, count = minheap[0]
            diff = toRoot - i
            if diff <= count:
                i += diff
                heappop(minheap)
                res += diff
            else:
                i += count
                heappop(minheap)
                res += count
        return res
