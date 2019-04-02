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
