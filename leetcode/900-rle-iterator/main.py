"""
    1st: queue

    Time    O(n)
    Space   O(n)
    32ms beats 15%
"""


class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.q = []
        self.total = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        # add items to queue
        while n > self.total:
            if len(self.A) < 2:
                self.q = []
                return -1
            count = self.A[0]
            value = self.A[1]
            self.q.append([count, value])
            self.total += count
            self.A = self.A[2:]
        # print(n, self.q)
        # remove items from queue
        res = -1
        while len(self.q) > 0 and n > self.q[0][0]:
            pop = self.q.pop(0)
            n -= pop[0]
            self.total -= pop[0]
            if n == 0:
                return pop[1]
        # subtract count
        if len(self.q) == 0:
            return -1
        self.q[0][0] = self.q[0][0] - n
        self.total -= n
        res = self.q[0][1]
        # print('calvin', res)
        if self.q[0][0] < 0:
            self.q.pop(0)
            return -1
        return res


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
