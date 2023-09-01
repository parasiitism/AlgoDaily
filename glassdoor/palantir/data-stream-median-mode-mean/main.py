from heapq import *
from collections import *


class MedianModeMean:

    def __init__(self):
        self.maxheap = []  # for the left hand side
        self.minheap = []  # for the right hand side, the bigger one
        self.ctr = Counter()
        self.max_appeared = (None, 0)  # (num, freq)
        self.total = 0

    def addNum(self, num: int) -> None:
        # mode
        self.ctr[num] += 1
        if self.ctr[num] > self.max_appeared[1]:
            self.max_appeared = (num, self.ctr[num])
        # avg
        self.total += num
        # median
        if len(self.maxheap) == len(self.minheap):
            heappush(self.maxheap, -num)
            max_from_left = -heappop(self.maxheap)
            heappush(self.minheap, max_from_left)
        else:
            heappush(self.minheap, num)
            min_from_right = heappop(self.minheap)
            heappush(self.maxheap, -min_from_right)

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            left = -self.maxheap[0]
            right = self.minheap[0]
            return (left + right) / 2.0
        else:
            return self.minheap[0]

    def findMode(self):
        return self.max_appeared[0]

    def findMean(self):
        n = len(self.maxheap) + len(self.minheap)
        return self.total / n
