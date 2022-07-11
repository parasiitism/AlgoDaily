# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    recursion

    Time    O(N)
    Space   O(H)
    82 ms, faster than 60.00%
"""


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        if left == None and right == None:
            return root.val == 1
        op = root.val
        if op == 2:
            return self.evaluateTree(left) or self.evaluateTree(right)
        return self.evaluateTree(left) and self.evaluateTree(right)
