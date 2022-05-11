# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
    recursion

    Time    O(N)
    Space   O(H)
    70 ms, faster than 50.00%
"""


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node == None:
            return 0, 0

        left, left_cnt = self.dfs(node.left)
        right, right_cnt = self.dfs(node.right)

        x = node.val
        cnt = 1 + left_cnt + right_cnt
        avg = (x + left + right) // cnt

        if x == avg:
            self.res += 1
        return (x + left + right, cnt)
