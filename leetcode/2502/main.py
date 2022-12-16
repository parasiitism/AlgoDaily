"""
    Array

    Time of allocate    O(N)
    Time of free        O(N)
"""


class Allocator:

    def __init__(self, n: int):
        self.n = n
        self.slots = n * [None]

    def allocate(self, size: int, mID: int) -> int:
        i = 0
        while i < self.n:
            j = i
            L = 0
            while j < self.n and self.slots[j] == None:
                L += 1
                if L == size:
                    self._fill(i, size, mID)
                    return i
                j += 1
            i = j + 1
        return -1

    def _fill(self, idx, size, mID):
        for i in range(size):
            self.slots[idx+i] = mID

    def free(self, mID: int) -> int:
        L = 0
        for i in range(self.n):
            if self.slots[i] == mID:
                self.slots[i] = None
                L += 1
        return L


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
