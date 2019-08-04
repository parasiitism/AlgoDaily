# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: bottom-up recursion
    - sum up the count when a node.val == left/right.val, update the result if necessary
    - each recursion only returns either the left or the right longest univalue count

    Time    O(n)
    Space   O(h) -> O(n)
    492 ms, faster than 11.81%
"""


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res - 1

    def dfs(self, node):
        if node == None:
            return 1
        total = 1

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        leftCount = 0
        rightCount = 0
        if node.left != None and node.val == node.left.val:
            leftCount = left

        if node.right != None and node.val == node.right.val:
            rightCount = right

        total2 = total + leftCount + rightCount
        self.res = max(self.res, total2)

        return max(total+leftCount, total+rightCount)
