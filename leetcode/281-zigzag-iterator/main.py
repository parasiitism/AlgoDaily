class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]

        leetcode doesn't support golang submission for this question, i did it in python
        Time    O(k) number of input arraies, in this case is 2
        Space   O(n)
        48ms beats 61.11%
        2feb2019
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


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
