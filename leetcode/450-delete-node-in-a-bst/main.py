# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        suggested solution: recursion

        Time		O(h) height of tree
        Space		O(h) recursion
        372 ms, faster than 94.59%
        21feb2019 updated
        """
        if root == None:
            return None
        if root.val == key:
            if root.left == None and root.right == None:
                return None
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            suc = self.findSucc(root)
            root.val = suc.val
            root.right = self.deleteNode(root.right, suc.val)
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def findSucc(self, node):
        suc = node.right
        while suc.left != None:
            suc = suc.left
        return suc
