import sys


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.amplitude = -sys.maxsize

    def treeAmplitude(self, root):
        self.dfs(root, sys.maxsize, -sys.maxsize)
        return self.amplitude

    def dfs(self, node, lowerB, upperB):
        if node == None:
            return
        a = min(node.val, lowerB)
        b = max(node.val, upperB)
        if node.left == None and node.right == None:
            if b - a > self.amplitude:
                self.amplitude = b-a
        self.dfs(node.left, a, b)
        self.dfs(node.right, a, b)


#       1
#    2     3
#  4 5    6
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

print(Solution().treeAmplitude(a))
