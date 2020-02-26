# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st: recursion
    1. first calculate the sum of all nodes' value
    2. for every subtree, calculate the product by using subtreeSum * (total-subtreeSum), update the global result if necessary

    Time    O(2N)
    Space   O(N)
    400 ms, faster than 66.46%
"""


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, self.findTotal(root))
        return self.res % (10**9 + 7)

    def findTotal(self, node: TreeNode) -> int:
        if node == None:
            return 0
        return node.val + self.findTotal(node.left) + self.findTotal(node.right)

    def dfs(self, node: TreeNode, total: int) -> int:
        if node == None:
            return 0
        subtreeSum = node.val + \
            self.dfs(node.left, total) + self.dfs(node.right, total)
        self.res = max(self.res, subtreeSum*(total - subtreeSum))
        return subtreeSum
