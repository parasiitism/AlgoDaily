# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: recursion

    Time    O(N)
    Space   O(N)
    824 ms, faster than 100.00%
"""


class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node == None:
            return 0
        x = node.val
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if x == left + right:
            self.res += 1
        return x + left + right
