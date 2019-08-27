# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st aproach:
	1. find the max
	2. set the node with max value
	3. set the node.left with nums[:i] and node.right with nums[i+1:] recursively
    
	Time	O(n^2)
	Space	O(h)
	192 ms, faster than 34.59%
"""


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        maxIdx = 0
        maxNum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
                maxIdx = i
        node = TreeNode(maxNum)
        node.left = self.constructMaximumBinaryTree(nums[:maxIdx])
        node.right = self.constructMaximumBinaryTree(nums[maxIdx+1:])
        return node
