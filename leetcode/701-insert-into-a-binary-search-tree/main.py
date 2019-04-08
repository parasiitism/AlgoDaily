# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode

        1st approach: iterative search the direction we are going to go down and insert the target into the right position

        104 ms, faster than 63.72%
        """
        if root == None:
            return TreeNode(val)
        cur = root
        while True:
            if cur.val < val:
                if cur.right != None:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
            else:
                if cur.left != None:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
        return root


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode

        2nd approach: recursive search the direction we are going to go down and insert the target into the right position

        104 ms, faster than 63.72%
        """
        if root == None:
            return TreeNode(val)
        self.recursion(root, val)
        return root

    def recursion(self, cur, val):
        if cur.val < val:
            if cur.right != None:
                self.recursion(cur.right, val)
            else:
                cur.right = TreeNode(val)
            return
        if cur.left != None:
            self.recursion(cur.left, val)
        else:
            cur.left = TreeNode(val)
