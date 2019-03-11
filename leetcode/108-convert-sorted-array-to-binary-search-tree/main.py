# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    revise:
    0. to create a balence tree, u must sort the array first
    1. sort the array
    2. build the tree recursively in the way of binary search
"""


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        nums = sorted(nums)
        return self.buildBST(nums, 0, len(nums)-1)

    def buildBST(self, nums, left, right):
        if left > right:
            return None
        mean = (left + right) / 2
        node = TreeNode(nums[mean])
        node.left = self.buildBST(nums, left, mean - 1)
        node.right = self.buildBST(nums, mean + 1, right)
        return node
