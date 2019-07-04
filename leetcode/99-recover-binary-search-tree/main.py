# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: inorder+sort
	- actually the inorder traversal of a BST is suppoed to be a sorted list of a valid
	1. so we can just get the inorder list
	2. clone the list and sort it, then compare with the inorder list we get from the inroder traversal to get that 2 nodes
	3. traverse again the tree, coorect that 2 nodes

	Time	O(nlogn+2n)
	Space	O(n)
	72 ms, faster than 14.96%
"""


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        arr = []

        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)

        sortedArr = sorted(arr)

        m = {}
        for i in range(len(arr)):
            if arr[i] != sortedArr[i]:
                m[arr[i]] = sortedArr[i]

        def correct(node):
            if node == None:
                return
            correct(node.left)
            if node.val in m:
                node.val = m[node.val]
            correct(node.right)
        correct(root)
