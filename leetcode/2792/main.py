# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
    recursion + sort
    - since K <= 10, we don't really need to care about the time that it takes in every recursion

    Time    O(N*KlogK)
    Space   O(H+K)
"""


class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0

        def dfs(node):
            if node == None:
                return []
            left = dfs(node.left)
            right = dfs(node.right)
            A = sorted(left + right)
            A = A[:k]
            if len(A) == k and A[-1] < node.val:
                self.res += 1
            return A + [node.val]

        dfs(root)

        return self.res
