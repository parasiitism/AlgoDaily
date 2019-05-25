"""
    1st approach:
    - add a class for StackItem
    - for each push(), calculate the curMin and put it with the x in stack
    - for each pop(), pop the top item

    Time    O(n)
    Space   O(n)
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append(StackItem(x, x))
            return
        top = self.stack[-1]
        if x < top.minVal:
            self.stack.append(StackItem(x, x))
        else:
            self.stack.append(StackItem(x,  top.minVal))

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            return None
        return self.stack.pop().val

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1].val

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1].minVal


# for interview, OOD > tuple
class StackItem(object):
    def __init__(self, val, minVal):
        self.val = val
        self.minVal = minVal


"""
    2nd approach:
    - just use tuple instead of StackItem
    - for each push(), calculate the curMin and put it with the x in stack
    - for each pop(), pop the top item

    Time    O(n)
    Space   O(n)
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append((x, x))
            return
        lastMin = self.stack[-1][1]
        self.stack.append((x, min(x, lastMin)))

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            return None
        pop, lastMin = self.stack.pop()
        return pop

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
