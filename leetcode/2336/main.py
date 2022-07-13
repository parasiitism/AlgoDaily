from heapq import *

"""
    hashtable
    - test set is small, so this is a hack

    Time    O(N)
    Space   O(N)
    249 ms, faster than 60.00%
"""


class SmallestInfiniteSet:

    def __init__(self):
        self.hs = set([i for i in range(1, 1001)])
        self.minheap = [i for i in range(1, 1001)]

    def popSmallest(self) -> int:
        if len(self.minheap) > 0:
            popped = heappop(self.minheap)
            self.hs.remove(popped)
            return popped
        return -1

    def addBack(self, num: int) -> None:
        if num in self.hs:
            return
        self.hs.add(num)
        heappush(self.minheap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
