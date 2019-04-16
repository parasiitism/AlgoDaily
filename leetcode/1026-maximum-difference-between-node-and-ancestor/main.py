# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: recursion
    - in each recursive function
        1. return the min and max node.val from the subtree
        2. compare the current node.val with the min and max which are from the return of subtrees

    Time    O(n)
    Space   O(h) h: height of the binary tree, worst case is O(n)
    36 ms, faster than 58.02%
"""


class Solution(object):

    def __init__(self):
        self.res = 0

    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node == None:
            return (10001, -1)

        mid = node.val
        leftMin, leftMax = self.dfs(node.left)
        rightMin, rightMax = self.dfs(node.right)

        a, b, c, d = 0, 0, 0, 0
        if leftMin != 10001 and leftMax != -1:
            a = abs(mid - leftMin)
            b = abs(mid - leftMax)

        if rightMin != 10001 and rightMax != -1:
            c = abs(mid - rightMin)
            d = abs(mid - rightMax)

        self.res = max(self.res, max(a, max(b, max(c, d))))

        left = min(mid, min(leftMin, rightMin))
        right = max(mid, max(leftMax, rightMax))
        return (left, right)
