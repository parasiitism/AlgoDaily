"""
    Implementation of a Min Heap
    - https://www.youtube.com/watch?v=LhhRbRXhB40
    - https://www.youtube.com/watch?v=W81Qzuz4qH0
"""


class Heap(object):
    def __init__(self):
        self.nums = []

    def heapify(self, arr):
        for o in arr:
            self.heapPush(o)

    # shift down the current min if the new value is small : O(logN)
    def heapPush(self, target):
        self.nums.append(target)
        curIdx = len(self.nums) - 1
        # print("heapPush", curIdx)
        while True:
            parentIdx = (curIdx - 1) / 2
            if parentIdx >= 0 and self.nums[parentIdx] > self.nums[curIdx]:
                self.nums[parentIdx], self.nums[curIdx] = self.nums[curIdx], self.nums[parentIdx]
                curIdx = parentIdx
            else:
                break

    # shift up with min value if any:  O(logN)
    def heapPop(self):
        pop = self.nums[0]
        p = self.nums.pop()
        if len(self.nums) == 0:
            return pop
        self.nums[0] = p
        cur = 0
        while cur < len(self.nums):
            left = 2*cur+1
            right = 2*cur+2
            # if 2 children
            if left < len(self.nums) and right < len(self.nums):
                if self.nums[cur] < self.nums[left] and self.nums[cur] < self.nums[right]:
                    break
                elif self.nums[left] < self.nums[right]:
                    self.nums[cur], self.nums[left] = self.nums[left], self.nums[cur]
                    cur = left
                else:
                    self.nums[cur], self.nums[right] = self.nums[right], self.nums[cur]
                    cur = right
            # if 1 child
            elif left < len(self.nums):
                if self.nums[left] < self.nums[cur]:
                    self.nums[cur], self.nums[left] = self.nums[left], self.nums[cur]
                    cur = left
                break
            # if no child, do nothing
            else:
                break
        return pop


h = Heap()

# test insert()
h.heapPush(8)
h.heapPush(9)
h.heapPush(6)
h.heapPush(7)
h.heapPush(4)
h.heapPush(3)
h.heapPush(5)
print(h.nums)
while len(h.nums) > 0:
    print(h.heapPop())

print("------------------------------------------------")

# test insert() with duplicate values
h = Heap()
h.heapPush(8)
h.heapPush(8)
h.heapPush(6)
h.heapPush(4)
h.heapPush(4)
h.heapPush(3)
h.heapPush(5)
while len(h.nums) > 0:
    print(h.heapPop())

print("------------------------------------------------")

# test heapify()
h = Heap()
h.heapify([6, 4, 2, 8, 9, 5, 7, 3])
print(h.nums)

# test heapify() with duplicate
h = Heap()
h.heapify([6, 4, 2, 8, 9, 5, 7, 4])
print(h.nums)

# test heapify() with duplicate
h = Heap()
h.heapify([6, 4, 2, 8, 9, 5, 7, 3])
top = h.heapPop()
print(top, h.nums)

"""
    Heap Sort
"""


def heapSort(nums):
    res = []
    h = Heap()
    h.heapify(nums)
    for i in range(len(nums)):
        p = h.heapPop()
        res.append(p)
    return res


nums = [12, 3, 1, 2, 4, 6, 3, 2, 4, 6, 3, 37, 37, 5, 5, 7, 77, 33, 4, 45]
print(heapSort(nums))
