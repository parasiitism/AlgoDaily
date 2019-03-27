import heapq

"""
    questions to ask:
    - how big is the N, e.g. many seats? 10^9 
    - will the input leave an unocuppied seat? no for now
    - if there are more than 1 option, which should i choose?
        n = 5, seat = [1,0,1,0,1] <= choose the first 0
    - so if i remove the end or the front and more than 1 options?
        n = 4, seat = [1,0,1,0] <= choose the first 0 as always
"""


"""
    1st approach:
    - store the occupied positions in an array
    - for every seat(), check the end, the middle, and the front to find out the left most "seatable" option
    - for every leave(), binary search the target and remove

    Time of seat    O(n)
    Time of leave   O(logn) binary search
    Space           O(n) worst case if all seats are occupied
    424 ms, faster than 12.06%
"""


class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.arr = []
        self.n = N

    def seat(self):
        """
        :rtype: int
        """
        if len(self.arr) == 0:
            self.arr.append(0)
            return 0
        if len(self.arr) == 1 and self.arr[0] == 0:
            self.arr.append(self.n-1)
            return self.n-1

        targetIdx = None
        targetDiff = 0

        # find in the end
        if self.arr[-1] != self.n-1:
            diff = self.n-self.arr[-1]-1
            if diff >= targetDiff:
                targetDiff = diff
                targetIdx = len(self.arr)-1

        # find in the middle
        for i in range(len(self.arr)-2, -1, -1):
            diff = int((self.arr[i+1]-self.arr[i])/2)
            if diff >= targetDiff:
                targetDiff = diff
                targetIdx = i

        # find in the front
        if self.arr[0] != 0:
            diff = self.arr[0]
            if diff >= targetDiff:
                self.arr = [0]+self.arr
                return 0

        # insert the person in the right position
        place = self.arr[targetIdx] + targetDiff
        self.arr = self.arr[:targetIdx+1] + [place] + self.arr[targetIdx+1:]
        return place

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        i = self.bsearch(p)
        self.arr = self.arr[:i] + self.arr[i+1:]

    def bsearch(self, target):
        arr = self.arr
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = int((left + right)/2)
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


e = ExamRoom(10)
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
e.leave(4)
print(e.seat())
e.leave(9)
print(e.seat())

print("----------------")

e = ExamRoom(6)
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
e.leave(1)
e.leave(2)
e.leave(4)
e.leave(5)
print(e.seat())

print("----------------")

e = ExamRoom(10)
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
e.leave(1)
e.leave(2)
e.leave(0)
e.leave(9)
print(e.seat())

print("----------------")

e = ExamRoom(5)
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
e.leave(0)
e.leave(1)
e.leave(3)
e.leave(4)
print(e.seat())

print("----------------")

e = ExamRoom(4)
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
e.leave(1)
e.leave(3)
print(e.seat())

print("============================")

"""
    2nd approach:
    - use a max heap to store the distance(interval) btw the seats
    - in the beginning, we can just use save [-1, N] to start
    - for every seat()
        - pop the max diff
        - use the diff to calculate the middle position
        - split the interval into 2 intervals and add back to the max heap
        since python haepq use 2nd item as a tie-breaker, e.g [2, 1, data], [2, 2, data] pop the first one,
        we can simply save the item in the format of [diff, leftIdx, rightIdx] to handle the tie situation
    - for every leave()
        - find and remove the items where end and start at index p
        - merge the items since we remove the middle one and add back one interval
        - heapify again to make sure that the heapq is legit

    Time of seat    O(3logn) 1 pop + 2 heap push
    Time of leave   O(n) heapify
    Space           O(n) worst case if all seats are occupied
    96 ms, faster than 73.82%
"""


class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.pq = []
        heapq.heappush(self.pq, (-N, -1, N))
        self.n = N

    # a helper for us to calculate the distance btw x and y
    def _calDist(self, x, y):   # length of the interval (x, y)
        if x == -1:  # note here we negate the value to make it maxheap
            return -y
        elif y == self.n:
            # e.g. 10-4-1=5, there are 5 seats btw 4 and the end
            return -(self.n - x - 1)
        else:
            return -int((y-x)/2)

    def seat(self):
        """
        :rtype: int

        O(logn) 1 heap pop + 2 heap push
        """
        # pop the intervals which has the max interval
        diff, left, right = heapq.heappop(self.pq)
        # calculate the seat position
        seat = None
        if left == -1:
            seat = 0
        elif right == self.n:
            seat = self.n-1
        else:
            seat = int((right + left)/2)
        # split the interval into 2 intervals and add back to the max heap
        heapq.heappush(self.pq, (self._calDist(left, seat), left, seat))
        heapq.heappush(self.pq, (self._calDist(seat, right), seat, right))
        return seat

    def leave(self, p):
        """
        :type p: int
        :rtype: void

        O(n) heapify
        """
        # find the items where end and start at index p
        itemLeft = None
        itemRight = None
        for interval in self.pq:
            if interval[1] == p:
                itemRight = interval
            if interval[2] == p:
                itemLeft = interval
            if itemLeft != None and itemRight != None:
                break
        # remove the items
        self.pq.remove(itemLeft)
        self.pq.remove(itemRight)
        # merge the items since we remove the middle one and add back one interval
        dis = self._calDist(itemLeft[1], itemRight[2])
        self.pq.append((dis, itemLeft[1], itemRight[2]))
        # and re-heapify the intervals again O(n)
        heapq.heapify(self.pq)


e = ExamRoom(10)
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
e.leave(4)
print(e.seat())
e.leave(9)
print(e.seat())

print("----------------")

e = ExamRoom(6)
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
e.leave(1)
e.leave(2)
e.leave(4)
e.leave(5)
print(e.seat())

print("----------------")

e = ExamRoom(10)
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
e.leave(1)
e.leave(2)
e.leave(0)
e.leave(9)
print(e.seat())

print("----------------")

e = ExamRoom(5)
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
e.leave(0)
e.leave(1)
e.leave(3)
e.leave(4)
print(e.seat())

print("----------------")

e = ExamRoom(4)
print(e.seat())
print(e.seat())
print(e.seat())
print(e.seat())
e.leave(1)
e.leave(3)
print(e.seat())

print("----------------")

"""
0
9
4
2
5
9
----------------
0
5
2
1
3
4
5
----------------
0
9
4
2
6
1
0
----------------
0
4
2
1
3
0
----------------
0
3
1
2
1
"""
