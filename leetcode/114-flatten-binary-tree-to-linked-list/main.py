# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.

        1st approach: 
        - store the nodes' values
        - add the values back to the linked list

        Time    O(2n)
        Space   O(n)
        28 ms, faster than 71.08%
        """
        arr = []

        def preOrder(node):
            if node == None:
                return
            arr.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        cur = root
        for i in range(len(arr)):
            x = arr[i]
            cur.val = x
            cur.left = None
            if i+1 < len(arr):
                cur.right = TreeNode(-1)
            cur = cur.right
