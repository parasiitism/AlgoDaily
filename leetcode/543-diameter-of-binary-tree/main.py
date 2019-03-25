# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int

        1st approach: dfs in recursion
        - for each node, compare the depths of left and right subtree
        - and compare and assign the result
        - in each node, just return the max depth of either left or right subtree 

        Time  O(n)
        Space O(h)
        52 ms, faster than 20.92%
        """
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if node == None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.result = max(self.result, left + right)
        return max(left, right) + 1
