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

    Time of seat    O(n)
    Time of leave   O(n)
    Space           O(n) worst case if all seats are occupied
    436 ms, faster than 10.88%
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
        i = 0
        while i < len(self.arr):
            if self.arr[i] == p:
                self.arr = self.arr[:i] + self.arr[i+1:]
                break
            i += 1


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
