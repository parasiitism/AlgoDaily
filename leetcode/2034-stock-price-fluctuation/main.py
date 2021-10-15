from heapq import *

"""
    1st: 2 heaps + hashtable
    - keep a hashmap of every timestamp to a stock price
    - when we have an update, heappush to both heaps
    - if the price from the heap doesn't match the price its timestamp, keep popping from the heap
    - keep in mind that, it is possible that a heap would maintain some outdated prices even after popping, 
        but it doesn't matter, cos we just want the min or the max
    
    Time of update()    O(logN)
    Time of current()   O(1)
    Time of maximum()   O(1) -> O(N) it depends on the update freq
    Time of minimum()   O(1) -> O(N)
    784 ms, faster than 83.33%
"""


class StockPrice:

    def __init__(self):
        self.timestamps = {}  # {timestamp: price}
        self.latestTimestamp = 0
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timestamps[timestamp] = price
        self.latestTimestamp = max(self.latestTimestamp, timestamp)

        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamps[self.latestTimestamp]

    def maximum(self) -> int:
        while -self.maxHeap[0][0] != self.timestamps[self.maxHeap[0][1]]:
            heappop(self.maxHeap)
        return -self.maxHeap[0][0]

    def minimum(self) -> int:
        while self.minHeap[0][0] != self.timestamps[self.minHeap[0][1]]:
            heappop(self.minHeap)
        return self.minHeap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
