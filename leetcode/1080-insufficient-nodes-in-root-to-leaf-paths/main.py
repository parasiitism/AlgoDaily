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
    104 ms, faster than 15.00%
"""


class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        return self.dfs(root, 0, limit)

    def dfs(self, node, total, limit):
        if node == None:
            return None
        # current sum
        total += node.val
        # check if we need to remove leaf
        if node.left == None and node.right == None:
            if total < limit:
                return None
            else:
                return node
        left = self.dfs(node.left, total, limit)
        right = self.dfs(node.right, total, limit)
        # if we removed a leaf from this nofe and it doesn't have other children, remove this node
        if left == None and right == None:
            return None
        # update this node children
        node.left = left
        node.right = right
        return node
