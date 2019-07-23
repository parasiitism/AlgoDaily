# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    learned from others: math
    
    ref:
    - https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal
    - idea.png

    Time    O(n)
    Space   O(n)
    24 ms, faster than 81.56%
"""


class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node == None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.res += abs(left) + abs(right)
        return node.val + left + right - 1
