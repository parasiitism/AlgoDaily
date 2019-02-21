# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        suggested solution 1: recursion
        case 1: 0 child: remove the current node from its parent
        case 2: 1 child: replace the current node with its child
        case 3: 2 children: replace the current node with its in-order successor child, left most child in its right subtree

        ref: https://www.youtube.com/watch?v=tT9-aCWD1Ag

        Time		O(h) height of tree
        Space		O(h) recursion
        56 ms, faster than 99.87%
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
            suc = self.findMinFromRight(root)
            root.val = suc.val
            root.right = self.deleteNode(root.right, suc.val)
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def findMinFromRight(self, node):
        suc = node.right
        while suc.left != None:
            suc = suc.left
        return suc


class Solution(object):
    def deleteNode(self, root, key):
        """
        suggested solution 2: recursion
        case 1: 0 child: remove the current node from its parent
        case 2: 1 child: replace the current node with its child
        case 3: 2 children: replace the current node with its in-order pedecessor child, right most child in its left subtree

        ref: https://www.youtube.com/watch?v=tT9-aCWD1Ag

        Time		O(h) height of tree
        Space		O(h) recursion
        56 ms, faster than 99.87%
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
            pre = self.findMaxFromLeft(root)
            root.val = pre.val
            root.left = self.deleteNode(root.left, pre.val)
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def findMaxFromLeft(self, node):
        pre = node.left
        while pre.right != None:
            pre = pre.right
        return pre
