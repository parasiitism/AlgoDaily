# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
    1st approach: recursion

    Time    O(n)
    Space   O(h)
    84 ms, faster than 29.99%
"""


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nums = []

        def _dfs(arr):
            for x in arr:
                if x.isInteger():
                    self.nums.append(x.getInteger())
                else:
                    _dfs(x.getList())
        _dfs(nestedList)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.nums.pop(0)
        return -1

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.nums) > 0


print("-----")

"""
    2nd approach: stack

    Time    O(n)
    Space   O(h)
    64 ms, faster than 98.75%
"""


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        for i in range(len(nestedList)-1, -1, -1):
            item = nestedList[i]
            self.stack.append(item)

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.stack) > 0:
            top = self.stack[-1]
            if top.isInteger():
                return True
            else:
                pop = self.stack.pop()
                for i in range(len(pop.getList())-1, -1, -1):
                    item = pop.getList()[i]
                    self.stack.append(item)
        return False


"""
    but actually, in a real interview, u will be given an array of int or arr, instead of leetcode's NestedInteger

    e.g. a = [[[1,2],3],4,[5,6]]

    in the beginning
    stack = [a]

    when we do hasnext(), we unfold the top item until we get to an integer
    stack = [
        [[1,2],3],          <- top
        4,
        [5,6]
    ]

    stack = [
        [1,2],              <- top
        3,
        4,
        [5,6]
    ]

    stack = [
        1,                  <- top, done unfolding
        2,
        3,
        4,
        [5,6],
    ]

    Time    O(n)
    Space   O(n)
"""


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = [nestedList]

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


ni = NestedIterator([[[1, 2], 3], 4, [5, 6]])
print(ni.next())
print(ni.next())
print(ni.next())
print(ni.next())
print(ni.next())
print(ni.next())
