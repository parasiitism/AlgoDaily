# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: inorder traversal
    - inorder traverse the tree
    - the node at k is the result

    Time    O(k)
    Space   O(h)
    48 ms, faster than 64.80%
"""


class Solution(object):

    def __init__(self):
        self.res = -1
        self.count = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.dfs(root, k)
        return self.res

    def dfs(self, node, k):
        if node == None:
            return
        self.dfs(node.left, k)
        self.count += 1
        if self.count == k:
            self.res = node.val
        self.dfs(node.right, k)
