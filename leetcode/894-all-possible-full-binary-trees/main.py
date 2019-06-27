# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: recursion, learned from others
    - numbers must be odd
    - if we have A nodes on my left, then we should have N-A-1 nodes on my right
    - the base case of the recursion is when n == 1, we just return 1 node

    ref:
    - https:// https://www.youtube.com/watch?v=noVVstnQvyY

    TIme    O(2^n)
    Space   O(2^n)
    220 ms, faster than 35.13%
"""


class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        ans = []
        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N - i - 1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ans.append(root)
        return ans
