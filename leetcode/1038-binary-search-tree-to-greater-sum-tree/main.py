# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: recursive (reversed) inorder traversal

    Time    O(n)
    Space   O(h)
    12 ms, faster than 96.98% 
"""


class Solution(object):

    def __init__(self):
        self.prefixSum = 0

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inorder(root)
        return root

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.right)
        self.prefixSum += node.val
        node.val = self.prefixSum
        self.inorder(node.left)


"""
    2nd approach: iterative (reversed) inorder traversal

    Time    O(n)
    Space   O(h)
    12 ms, faster than 96.98% 
"""


class Solution(object):

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        prefixSum = 0
        stack = []
        cur = root
        while cur != None or len(stack) > 0:
            # all the way down to the right most leaf
            while cur != None:
                stack.append(cur)
                cur = cur.right
            # pop the item from the stack
            node = stack.pop()
            # do something on the popped node
            prefixSum += node.val
            node.val = prefixSum
            cur = node.left
        return root
