# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st: recursion, 1-pass
    1. first calculate the sum of all nodes' value
    2. for every subtree, calculate the product by using subtreeSum * (total-subtreeSum), update the global result if necessary

    Time    O(2N)
    Space   O(N)
    318 ms, faster than 76.88%
"""


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        self.candidates = []
        total = self.dfs(root)
        res = 0
        for c in self.candidates:
            res = max(res, c * (total - c))
        return res % (10**9 + 7)

    def dfs(self, node: TreeNode) -> int:
        if node == None:
            return 0
        subtreeSum = node.val + self.dfs(node.left) + self.dfs(node.right)
        self.candidates.append(subtreeSum)
        return subtreeSum
