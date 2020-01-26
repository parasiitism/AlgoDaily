# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: recursion
    1. postorder recursion down to the leaves
    2. if the leaves == target, return None
    3. construct the tree by recursion

    Time    O(N)
    Space   O(H)
    60 ms, faster than 24.88% 
"""


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root == None:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.val == target and root.left == None and root.right == None:
            return None
        return root
