# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: recursive dfs

    Time    O(n)
    Space   O(h)
    28 ms, faster than 99.78%
"""


class Solution(object):

    def __init__(self):
        self.res = 0

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, preSum):
        if node == None:
            return
        curSum = preSum*2 + node.val
        if node.left == None and node.right == None:
            self.res += curSum
            return
        self.dfs(node.left, curSum)
        self.dfs(node.right, curSum)


"""
    2nd approach: iterative dfs

    Time    O(n)
    Space   O(h)
    28 ms, faster than 99.78%
"""


class Solution(object):

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        res = 0
        stack = [(root, 0)]
        while len(stack) > 0:
            node, preSum = stack.pop()
            curSum = preSum*2 + node.val
            if node.left == None and node.right == None:
                res += curSum
            if node.left != None:
                stack.append((node.left, curSum))
            if node.right != None:
                stack.append((node.right, curSum))
        return res
