class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool


        232ms beats 54.85%
        24jan2019
        """
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False

        if s.val == t.val:
            if self.isIdentical(s, t) == True:
                return True

        left = self.isSubtree(s.left, t)
        right = self.isSubtree(s.right, t)
        return left or right

    def isIdentical(self, a, b):
        if a is None and b is None:
            return True
        elif a is None or b is None:
            return False
        mid = a.val == b.val
        left = self.isIdentical(a.left, b.left)
        right = self.isIdentical(a.right, b.right)
        return mid and left and right
