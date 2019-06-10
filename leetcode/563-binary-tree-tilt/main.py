# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: recursive dfs

    Time    O(n)
    Space   O(h)
    52 ms, faster than 73.41%
"""


class Solution(object):

    def __init__(self):
        self.res = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, res = self.dfs(root)
        self.res += res
        return self.res

    def dfs(self, node):
        if node == None:
            return 0, 0
        left, t1 = self.dfs(node.left)
        right, t2 = self.dfs(node.right)
        self.res += t1 + t2
        return node.val + left + right, abs(left-right)
