"""
    1st approach: sliding window

    Time    O(1) next()
    Space   O(k) k: size since we need to store the sliding window
    56 ms, faster than 70.34%
"""


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.arr = []
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.arr) > 0 and len(self.arr) == self.size:
            left = self.arr.pop(0)
            self.sum -= left
        self.sum += val
        self.arr.append(val)
        return self.sum/float(len(self.arr))
