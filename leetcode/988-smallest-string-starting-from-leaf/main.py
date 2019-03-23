import sys
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.res = 8500*"z"

    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str

        1st approach: recursive dfs

        Time    O(n)
        Space   O(h)
        44ms beats 21.32%
        """
        if root == None:
            return ""
        self.dfs(root, "")
        return self.res

    def dfs(self, node, path):
        if node == None:
            return
        chrs = "abcdefghijklmnopqrstuvwxyz"
        cur = chrs[node.val]
        if node.left == None and node.right == None:
            self.res = min(self.res, cur+path)
        self.dfs(node.left, cur+path)
        self.dfs(node.right, cur+path)


class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str

        1st approach: recursive dfs

        Time    O(n)
        Space   O(h)
        40 ms, faster than 26.88% 
        """
        if root == None:
            return ""
        res = 8500*"z"
        chrs = "abcdefghijklmnopqrstuvwxyz"
        stack = [(root, "")]
        while len(stack) > 0:
            node, path = stack.pop()
            cur = chrs[node.val]
            if node.left == None and node.right == None:
                res = min(res, cur+path)
            if node.left != None:
                stack.append((node.left, cur+path))
            if node.right != None:
                stack.append((node.right, cur+path))
        return res
