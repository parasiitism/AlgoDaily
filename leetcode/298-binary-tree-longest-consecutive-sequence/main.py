# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: recursive dfs

    Time    O(n)
    Space   O(n)
    616 ms, faster than 5.08%
"""


class Solution(object):

    def __init__(self):
        self.res = 1

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.dfs(root, -sys.maxsize, [])
        return self.res

    def dfs(self, node, prev, path):
        if node == None:
            return
        newPath = []
        if prev+1 == node.val:
            newPath = path[:]
            newPath.append(node.val)
            if len(newPath) > self.res:
                self.res = len(newPath)
        else:
            newPath.append(node.val)
        self.dfs(node.left, node.val, newPath)
        self.dfs(node.right, node.val, newPath)
