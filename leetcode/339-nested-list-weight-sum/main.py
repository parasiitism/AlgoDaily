"""
    1st approach: recursive dfs

    Time  O(n)
    Space O(h)
    12 ms, faster than 99.88%
"""


class Solution(object):

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.dfs(nestedList, 1)

    def dfs(self, arr, depth):
        res = 0
        for x in arr:
            if x.isInteger():
                res += depth * x.getInteger()
            else:
                res += self.dfs(x.getList(), depth+1)
        return res


"""
    1st approach: iterative dfs

    Time  O(n)
    Space O(h)
    20 ms, faster than 83.54%
"""


class Solution(object):

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        result = 0
        stack = []
        stack.append((nestedList, 1))
        while len(stack) > 0:
            arr, depth = stack.pop()
            for x in arr:
                if x.isInteger():
                    result += depth * x.getInteger()
                else:
                    stack.append((x.getList(), depth + 1))
        return result
