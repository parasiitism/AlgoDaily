from bisect import *

"""
    1st: binary search + math
    - my first thought was using intervals, but it was too complicated to implement correctly
    
    learned from others:
    - put opens and closes to an array <- so ideally, there will be an even number of nums
    - addRange
        - lower-bound binary search the start
            - if resultIdx == even:
                it means there are legit pairs on the left, so we should insert an open at resultIdx
            - else:
                it means that the start is already inside a pair(range), we don't need to do anything
        - upper-bound binary search the end
            - if resultIdx == even:
                it means there are legit pairs on the left, so we should insert a close at resultIdx
            - else:
                it means that the start is already inside a pair(range), we don't need to do anything
    - removeRange
        - lower-bound binary search the start
            - if resultIdx == odd:
                it means that the start is inside a pair, we should remove the range on the right hand side
            - else:
                it means that the end is aleady outside a pair(range), we don't need to do anything
        - upper-bound binary search the end
            - if resultIdx == odd:
                it means that the end is inside a pair, we should remove the range on the left hand side
            - else:
                it means that the end is aleady outside a pair(range), we don't need to do anything
    - queryRange
        - use lower-bound binary search the start AND upper-bound binary search the end
            - if the result indices point to the same index AND the index is a start point(odd), it means the range is legit

    ref:
    - https://leetcode.com/problems/range-module/discuss/244194/Python-solution-using-bisect_left-bisect_right-with-explanation

    Time of addRange        O(N) because slicing takes O(O) which > binary search O(logN)
    Time of removeRange     O(N) because slicing takes O(O) which > binary search O(logN)
    Time of queryRange      O(logN)
    372 ms, faster than 69.44% 
"""


class RangeModule(object):

    def __init__(self):
        self.openCloses = []

    def addRange(self, left, right):
        s = bisect_left(self.openCloses, left)
        e = bisect_right(self.openCloses, right)

        sub = []
        if s % 2 == 0:
            sub.append(left)
        if e % 2 == 0:
            sub.append(right)

        self.openCloses = self.openCloses[:s] + sub + self.openCloses[e:]
        # or self.openCloses[s:e] = sub

    def removeRange(self, left, right):
        s = bisect_left(self.openCloses, left)
        e = bisect_right(self.openCloses, right)

        sub = []
        if s % 2 == 1:
            sub.append(left)
        if e % 2 == 1:
            sub.append(right)

        self.openCloses = self.openCloses[:s] + sub + self.openCloses[e:]
        # or self.openCloses[s:e] = sub

    def queryRange(self, left, right):
        s = bisect_right(self.openCloses, left)
        e = bisect_left(self.openCloses, right)

        return s == e and s % 2 == 1


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
