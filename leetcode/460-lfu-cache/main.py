import heapq


class Heap(object):

    def __init__(self):
        self._heap = []

    def push(self, priority, item):
        heapq.heappush(self._heap, (priority, item))

    def update(self):
        heapq.heapreplace(self._heap, (10, "which size?"))

    def pop(self):
        item = heapq.heappop(self._heap)[1]  # (prio, item)[1] == item
        return item

    def printHeap(self):
        print(self._heap)


h = Heap()
# add some nonsense:
h.push(10, "I'm a large one")
h.push(20, "Actually I'm larger")
h.push(5, "size is not everything")
h.push(0, "which size?")
h.printHeap()
h.update()
h.printHeap()
