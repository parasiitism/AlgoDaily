"""
    combine
    - leetcode 700: Search in BST
    - leetcode 701: Insert in BST
    - leetcode 450: Delete in BST
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST(object):

    def __init__(self):
        self.root = None

    def searchBST(self, val: int) -> TreeNode:
        cur = self.root
        while cur:
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                cur = cur.right
            else:
                return cur
        return None

    def insertIntoBST(self, val: int) -> TreeNode:
        if self.root == None:
            return TreeNode(val)
        cur = self.root
        while cur:
            if val < cur.val:
                if cur.left == None:
                    cur.left = TreeNode(val)
                    break
                else:
                    cur = cur.left
            elif val > cur.val:
                if cur.right == None:
                    cur.right = TreeNode(val)
                    break
                else:
                    cur = cur.right
            else:
                break
        return cur

    def deleteNode(self, key):
        self.root = self._deleteNode(self.root, key)

    def _deleteNode(self, root, key):
        if root == None:
            return None
        if key < root.val:
            root.left = self._deleteNode(root.left, key)
        elif key > root.val:
            root.right = self._deleteNode(root.right, key)
        elif root.val == key:
            if root.left == None and root.right == None:
                return None
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            suc = self._findLeftMost(root.right)
            root.val, suc.val = suc.val, root.val
            root.right = self._deleteNode(root.right, key)
            return root
        return root

    def _findLeftMost(self, node):
        suc = node
        while suc.left != None:
            suc = suc.left
        return suc
