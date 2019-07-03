"""
    classic approach: 2 stacks
    
    Time    O(n)
    Space   O(n)
    16 ms, faster than 81.57%
"""


class MyQueue(object):

    def __init__(self):
        self.mainS = []
        self.minorS = []

    def push(self, x):
        while len(self.mainS) > 0:
            self.minorS.append(self.mainS.pop())
        self.mainS.append(x)
        while len(self.minorS) > 0:
            self.mainS.append(self.minorS.pop())

    def pop(self):
        return self.mainS.pop()

    def peek(self):
        temp = self.mainS.pop()
        self.mainS.append(temp)
        return temp  # rmb: peek is to peek the top(last) element in the stack

    def empty(self):
        return len(self.mainS) == 0


"""
    actually why just do it with an array
    
    Time    O(n)
    Space   O(n)
    12 ms, faster than 93.00%
"""


class MyQueue(object):

    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        return self.arr.pop(0)

    def peek(self):
        return self.arr[0]

    def empty(self):
        return len(self.arr) == 0
