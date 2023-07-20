class MinHeap(object):

    def __init__(self):
        self.A = []

    def heapPush(self, x):
        self.A.append(x)
        self._shiftUp(len(self.A) - 1)

    def heapPop(self):
        n = len(self.A)
        self.A[0], self.A[n-1] = self.A[n-1], self.A[0]
        min_node = self.A.pop()
        self._shiftDown(0)
        return min_node

    def _shiftUp(self, idx):
        parent = (idx - 1) // 2
        if parent >= 0 and self.A[idx] < self.A[parent]:
            self.A[idx], self.A[parent] = self.A[parent], self.A[idx]
            self._shiftUp(parent)

    def _shiftDown(self, idx):
        children = [idx*2+1, idx*2+2]
        smallest_idx = idx
        for i in children:
            if i < len(self.A) and self.A[i] < self.A[smallest_idx]:
                smallest_idx = i
        if smallest_idx != idx:
            self.A[idx], self.A[smallest_idx] = self.A[smallest_idx], self.A[idx]
            self._shiftDown(smallest_idx)

    def heapify(self, arr):
        # O(nlogn) version
        # for o in arr:
        #     self.heapPush(o)

        # O(n) version
        # bottom-up
        # shift down from bottom to top such that we minimize the number of shift operations
        # n/2 + n/8 + n/16.... = O(n)
        self.A = arr
        n = len(self.A)
        for i in range(n//2, -1, -1):
            self._shiftDown(i)


h = MinHeap()

print("--- insert() ---")
h.heapPush(8)
h.heapPush(9)
h.heapPush(6)
h.heapPush(7)
h.heapPush(4)
h.heapPush(3)
h.heapPush(5)
print(h.A)
while len(h.A) > 0:
    print(h.heapPop())

print("--- insert() with duplicate values ----")
h = MinHeap()
h.heapPush(8)
h.heapPush(8)
h.heapPush(6)
h.heapPush(4)
h.heapPush(4)
h.heapPush(3)
h.heapPush(5)
while len(h.A) > 0:
    print(h.heapPop())

print("--- heapify() --- ")
h = MinHeap()
h.heapify([6, 4, 2, 8, 9, 5, 7, 3])
res = []
while len(h.A) > 0:
    res.append(h.heapPop())
print(res)

print("--- heapify() with duplicates --- ")
h = MinHeap()
h.heapify([6, 4, 2, 8, 9, 5, 7, 4])
res = []
while len(h.A) > 0:
    res.append(h.heapPop())
print(res)


print("--- HeapSort --- ")


def heapSort(nums):
    res = []
    h = MinHeap()
    h.heapify(nums)
    n = len(nums)
    for _ in range(n):
        p = h.heapPop()
        res.append(p)
    return res


nums = [12, 3, 1, 2, 4, 6, 3, 2, 4, 6, 3, 37, 37, 5, 5, 7, 77, 33, 4, 45]
print(heapSort(nums))
