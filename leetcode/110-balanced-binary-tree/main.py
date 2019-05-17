# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: recursion
    - for each node, if depths from left and right diff > 1, it is unbalanced

    Time    O(n)
    Space   O(n)
    40 ms, faster than 96.57%
"""


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root) != -1

    def dfs(self, node):
        if node == None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left-right) > 1:
            return -1
        return max(left, right) + 1
