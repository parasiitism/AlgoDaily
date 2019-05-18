"""
    questions to ask:
    - will we have empty arrays? yes
    - all are numbers? yes
"""

"""
    naive approach: put all of the numbers into a single array

    Time  O(n) when construct
    Space O(n)
    104 ms, faster than 17.66%
"""


class Vector2D(object):

    def __init__(self, v):
        self.nums = []
        for arr in v:
            for num in arr:
                self.nums.append(num)

    def next(self):
        return self.nums.pop(0)

    def hasNext(self):
        return len(self.nums) > 0


"""
    1st approach: stack
    
    e.g. a = [[[1,2],3],4,[5,6]]

    in the beginning
    stack = [a]

    when we do hasnext(), we unfold the top item until we get to an integer
    stack = [
        [5,6],
        4,
        [[1,2],3],          <- top
    ]

    stack = [
        [5,6],
        4,
        3,
        [1,2],              <- top
    ]

    stack = [
        [5,6],
        4,
        3,
        2,
        1,                  <- top, done unfolding
    ]

    Time    O(n)
    Space   O(n)
    80 ms, faster than 50.56%
"""


class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.stack = [v]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.stack) > 0:
            top = self.stack[-1]
            if isinstance(top, int):
                return True
            else:
                pop = self.stack.pop()
                for i in range(len(pop)-1, -1, -1):
                    self.stack.append(pop[i])
        return False


"""
    2nd approach: queue <- similar to the stack one
    
    e.g. a = [[[1,2],3],4,[5,6]]

    in the beginning
    stack = [a]

    when we do hasnext(), we unfold the top item until we get to an integer
    queue = [
        [[1,2],3],          <- head
        4,
        [5,6]
    ]

    queue = [
        [1,2],              <- head
        3,
        4,
        [5,6]
    ]

    queue = [
        1,                  <- head, done unfolding
        2,
        3,
        4,
        [5,6],
    ]

    Time    O(n)
    Space   O(n)
    84 ms, faster than 39.28%
"""


class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.queue = [v]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        return self.queue.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.queue) > 0:
            head = self.queue[0]
            if isinstance(head, int):
                return True
            else:
                pop = self.queue.pop(0)
                temp = []
                for i in range(len(pop)):
                    temp.append(pop[i])
                self.queue = temp + self.queue
        return False
