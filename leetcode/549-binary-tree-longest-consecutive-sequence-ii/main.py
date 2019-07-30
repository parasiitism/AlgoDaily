# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: recursion
    - for each node, we can calculate the longest increment count and the longest decremnt count
        - if node.child.val - 1 == node.val: incremnet + 1
        - if node.child.val + 1 == node.val: decremnet + 1
    - by returning the (incremnet count, decremnet count) in a recursion, we can accumlate the counts if we can make a sequence with the current node

    Time    O(n)
    Space   O(h) at most O(n)
    44 ms, faster than 66.10%
"""


class Solution(object):

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node == None:
            return 0, 0
        inc, dec = 1, 1
        if node.left != None:
            x, y = self.dfs(node.left)
            if node.val == node.left.val - 1:
                inc = x + 1
            elif node.val == node.left.val + 1:
                dec = y + 1
        if node.right != None:
            x, y = self.dfs(node.right)
            if node.val == node.right.val - 1:
                inc = max(inc, x + 1)
            elif node.val == node.right.val + 1:
                dec = max(dec, y + 1)
        self.res = max(self.res, inc+dec-1)
        return inc, dec
