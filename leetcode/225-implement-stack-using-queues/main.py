"""
    classic approach: 2 queues
    
    Time    O(n)
    Space   O(n)
    20 ms, faster than 62.85%
"""


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mainQ = []
        self.minorQ = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        while len(self.mainQ) > 0:
            self.minorQ.append(self.mainQ.pop(0))
        self.mainQ.append(x)
        while len(self.minorQ) > 0:
            self.mainQ.append(self.minorQ.pop(0))

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.mainQ.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.mainQ[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.mainQ) == 0
