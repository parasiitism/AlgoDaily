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


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
