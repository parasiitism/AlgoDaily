# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: recursion

    Time    O(n)
    Space   O(h)
    48 ms, faster than 52.08%
"""


class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        if root == None:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node == None:
            return (0, 0)
        left_total, left_count = self.dfs(node.left)
        right_total, right_count = self.dfs(node.right)
        total = node.val + left_total + right_total
        count = 1 + left_count + right_count
        avg = total/float(count)
        self.res = max(self.res, avg)
        return total, count
