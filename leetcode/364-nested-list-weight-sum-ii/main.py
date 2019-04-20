# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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
    - recursively put the items into the appropriate array at index
    - reverse the 2D array by row
    - multiply the values with index and sum them up to the result

    Time    O(3n)
    Space   O(h)
    24 ms, faster than 44.37%
"""


class Solution(object):
    def __init__(self):
        self.arrays = []

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        # O(n)
        self.helper(nestedList, 0)
        # O(n)
        rArr = self.arrays[::-1]
        res = 0
        # O(n)
        for i in range(len(rArr)):
            arr = rArr[i]
            res += (i+1) * sum(arr)
        return res

    def helper(self, arr, level):
        for item in arr:
            if item.isInteger():
                x = item.getInteger()
                # create arrays if array length below index
                # e.g. self.arrays = [], level = 3
                # [] < 3
                # [ [] ] < 3
                # [ [], [] ] < 3
                # [ [], [], [] ] < 3
                # [ [], [], [], [] ] exit
                while len(self.arrays) <= level:
                    self.arrays.append([])
                # append the item into appropiate arr at index
                self.arrays[level].append(x)
            else:
                # recursion
                self.helper(item.getList(), level+1)


"""
    2nd approach: recursion + hashtable
    - recursively put the items into the appropriate array at index(key in hashtable)
    - find out the max depth that we can reach
    - multiply the values with index and sum them up to the result

    Time    O(2n)
    Space   O(h)
    24 ms, faster than 44.37%
"""


class Solution(object):

    def __init__(self):
        self.maxIdx = 0

    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        ht = {}
        # recursion
        self.helper(nestedList, 0, ht)
        # depth is max index + 1
        depth = self.maxIdx + 1
        res = 0
        # iterate the hashtable
        for key in ht:
            res += (depth - key) * ht[key]
        return res

    def helper(self, arr, level, ht):
        # find out the max index that we can reach
        self.maxIdx = max(self.maxIdx, level)

        for item in arr:
            if item.isInteger():
                x = item.getInteger()
                if level not in ht:
                    ht[level] = x
                else:
                    ht[level] += x
            else:
                self.helper(item.getList(), level + 1, ht)
