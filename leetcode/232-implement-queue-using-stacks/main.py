"""
    classic approach: 2 stacks
    
    Time    O(n)
    Space   O(n)
    20 ms, faster than 61.17%
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mainS = []
        self.minorS = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while len(self.mainS) > 0:
            self.minorS.append(self.mainS.pop())
        self.mainS.append(x)
        while len(self.minorS) > 0:
            self.mainS.append(self.minorS.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.mainS.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.mainS[-1]  # rmb: peek is to peek the top(last) element in the stack

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.mainS) == 0
