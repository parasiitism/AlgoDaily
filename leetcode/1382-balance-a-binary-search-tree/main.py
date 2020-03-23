# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: inorder + binary search
    - convert the tree to a sorted array using an in-order traversal
    - construct a new balanced tree from the sorted array recursively

    Time    O(2N)
    Space   O(N)
    392 ms, faster than 17.25% 
"""


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        self.inorder(root)
        return self.buildBST(self.arr)

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        self.arr.append(node.val)
        self.inorder(node.right)

    def buildBST(self, nums):
        if len(nums) == 0:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.buildBST(nums[:mid])
        node.right = self.buildBST(nums[mid+1:])
        return node
