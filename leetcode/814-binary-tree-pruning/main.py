# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: tree, recursion
    - recursively traverse the input tree, if the value sum of subtree is 0, return null

    Time    O(n)
    Space   O(n)
    16ms beats 80%
"""


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        val, node = self.dfs(root)
        return node

    def dfs(self, node):
        if node == None:
            return 0, None
        left_val, left = self.dfs(node.left)
        right_val, right = self.dfs(node.right)
        if left_val == 0:
            node.left = None
        if right_val == 0:
            node.right = None
        return left_val + node.val + right_val, node
