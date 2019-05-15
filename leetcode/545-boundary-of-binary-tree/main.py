# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: preorder + inorder + postorder

    Time    O(3n)
    Space   O(n)
    36 ms, faster than 96.63%
"""


class Solution(object):

    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(node):
            if node == None:
                return
            if node.left == None and node.right == None:
                return
            boundary.append(node.val)
            if node.left:
                preorder(node.left)
            else:
                preorder(node.right)

        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            if node != root and node.left == None and node.right == None:
                boundary.append(node.val)
            inorder(node.right)

        def postorder(node):
            if node == None:
                return
            if node.left == None and node.right == None:
                return
            if node.right:
                postorder(node.right)
            else:
                postorder(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        preorder(root.left)
        inorder(root)
        postorder(root.right)
        return boundary
