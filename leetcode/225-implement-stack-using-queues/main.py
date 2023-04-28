"""
    1st: classic approach - 2 queues
    
    Time    O(n)
    Space   O(n)
    20 ms, faster than 62.85%
"""


class MyStack(object):

    def __init__(self):
        self.mainQ = []
        self.minorQ = []

    def push(self, x):
        while len(self.mainQ) > 0:
            self.minorQ.append(self.mainQ.pop(0))
        self.mainQ.append(x)
        while len(self.minorQ) > 0:
            self.mainQ.append(self.minorQ.pop(0))

    def pop(self):
        return self.mainQ.pop(0)

    def top(self):
        return self.mainQ[0]

    def empty(self):
        return len(self.mainQ) == 0


"""
    2nd: classic approach - 1 queue
    
    Time    O(n)
    Space   O(n)
    20 ms, faster than 62.85%
"""


class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        n = len(self.q)
        self.q.append(x)
        for i in range(n):
            self.q.append(self.q.pop(0))

    def pop(self) -> int:
        return self.q.pop(0)

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
