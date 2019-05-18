"""
    1st approach: 2 pointers
    
    Time    O(k) number of input arraies, in this case is 2
    Space   O(n)
    48ms beats 61.11%
    2feb2019
"""


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.cnt = len(v1)+len(v2)
        self.combo = [v1, v2]
        self.i = 0
        self.numberOfPop = 0

    def next(self):
        """
        :rtype: int
        """
        while True:
            idx = self.i % 2
            if len(self.combo[idx]) > 0:
                temp = self.combo[idx].pop(0)
                self.i += 1
                self.numberOfPop += 1
                return temp
            self.i += 1

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.numberOfPop < self.cnt


"""
    2nd approach: pop and rotate
    - this is much easier to solve the followup question: v1, v2, v3, v4...,vn

    Time    O(k)
    Space   O(n)
    52 ms, faster than 44.48%
    18may2019
"""


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = []
        if len(v1) > 0:
            self.vectors.append(v1)
        if len(v2) > 0:
            self.vectors.append(v2)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext() == False:
            return -1
        topVector = self.vectors.pop(0)
        p = topVector.pop(0)
        # after pop, put the popped items back but to the end
        if len(topVector) > 0:
            self.vectors.append(topVector)
        return p

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.vectors) > 0 and len(self.vectors[0]) > 0
