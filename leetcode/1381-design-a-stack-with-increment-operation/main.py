"""
    1st: array
    - straight-forward approach

    Time    O(k) per increment()
    Space   O(maxSize)
    124 ms, faster than 45.15%
"""


class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.arr = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.arr) == self.maxSize:
            return
        self.arr.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.arr) == 0:
            return -1
        return self.arr.pop()

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        start = max(len(self.arr) - k, 0)
        for i in range(min(k, len(self.arr))):
            self.arr[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

"""
    2nd: 
    - learned from others
    - use an additional array to record the increment value
    - inc[i] means for all elements from stack[0] to stack[i], we should plus inc[i] when we pop() from the stack
    - then inc[i-1] += inc[i], so that we will keep the increment value for the next pop()

    ref:
    - https://leetcode.com/problems/design-a-stack-with-increment-operation/discuss/539716/JavaC%2B%2BPython-Lazy-increment-O(1)

    Time    O(1) for all func
    Space   O(2N)
    80 ms, faster than 87.86%
"""


class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.arr = []
        self.inc = maxSize * [0]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.arr) == self.maxSize:
            return
        self.arr.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.arr) == 0:
            return -1
        i = len(self.arr) - 1
        if i > 0:
            self.inc[i-1] += self.inc[i]
        res = self.arr.pop() + self.inc[i]
        self.inc[i] = 0
        return res

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        last = min(k, len(self.arr)) - 1
        if last >= 0:
            self.inc[last] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
