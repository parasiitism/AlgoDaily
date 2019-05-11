# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: iterative dfs 
    Time    O(n)
    Space   O(h)
    20 ms, faster than 99.45%
    11may2019
"""


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        stack1 = [root]
        stack2 = [root]
        while len(stack1) > 0 or len(stack2) > 0:
            if len(stack1) != len(stack2):
                return False
            pop1 = stack1.pop()
            pop2 = stack2.pop()
            if pop1 == None and pop2 == None:
                continue
            if pop1 == None or pop2 == None:
                return False
            if pop1.val != pop2.val:
                return False

            stack1.append(pop1.left)
            stack1.append(pop1.right)

            stack2.append(pop2.right)
            stack2.append(pop2.left)
        return True


"""
    2nd approach: recursive dfs

    Time    O(n)
    Space   O(h)
    20 ms, faster than 99.45%
    11may2019
"""


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, a, b):
        if a == None and b == None:
            return True
        if a == None or b == None:
            return False
        if a.val != b.val:
            return False
        left = self.dfs(a.left, b.right)
        right = self.dfs(a.right, b.left)
        return left and right
