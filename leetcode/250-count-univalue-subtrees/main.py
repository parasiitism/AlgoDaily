# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.res = 0

    def countUnivalSubtrees(self, root):
        """
            1st approach: bottom up recusrion
            Time    O(n)
            Space   O(h)
            32 ms, faster than 16.86% 
        """
        if root == None:
            return 0
        self.dfs(root, None)
        return self.res

    def dfs(self, node, parentVal):
        if node == None:
            return parentVal
        left = self.dfs(node.left, node.val)
        right = self.dfs(node.right, node.val)
        if node.val == left and node.val == right and left != None and right != None:
            self.res += 1
            return node.val
        return None
