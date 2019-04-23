# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: bottom up recursion
    - if values are same and positions are correct, traverse down the trees
    - if values are same but positions are incorrect, flip them and traverse down
    - we dont necessarily need to flip the trees, we can just traverse them with swapped nodes

    Time    O(n)
    Space   O(h)
    24 ms, faster than 53.94%
"""


class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False

        # extract the values for comparision
        # -1 indicates the values of none node
        left1 = -1
        if root1.left != None:
            left1 = root1.left.val
        right1 = -1
        if root1.right != None:
            right1 = root1.right.val

        left2 = -1
        if root2.left != None:
            left2 = root2.left.val
        right2 = -1
        if root2.right != None:
            right2 = root2.right.val

        # if values are same and positions are correct, traverse down the trees
        if left1 == left2 and right1 == right2:
            x = self.flipEquiv(root1.left, root2.left)
            y = self.flipEquiv(root1.right, root2.right)
            return x and y

        # if values are same but positions are incorrect, flip them and traverse down
        if left1 == right2 and right1 == left2:
            x = self.flipEquiv(root1.left, root2.right)
            y = self.flipEquiv(root1.right, root2.left)
            return x and y

        return False
