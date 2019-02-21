"""
  leetcode doesnt support go
"""


class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution(object):
    def inorderSuccessor(self, node):
        """
        Actually i dont know why it doesn't work
        1. if the node has right child, it means its successor is its leftmsot child in its right subtree
        2. if the node doesn't have children, look for its lowest ancestor which value is larger than its

        Time    O(logn)
        Space   O(h)
        348 ms, faster than 93.59% 
        """
        # find successor in its subtree
        if node.right != None:
            node = node.right
            while node.left:
                node = node.left
            return node
        # find successor from its ancestors
        parent = node.parent
        while parent != None and node.val > parent.val:
            parent = parent.parent
        if parent == None or parent.val < node.val:
            return None
        return parent


class Solution(object):
    def inorderSuccessor(self, node):
        """
        suggested solution
        """
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        while node.parent and node.parent.val < node.val:
            node = node.parent
        return node.parent
