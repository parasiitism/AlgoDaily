# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st: reuse lc654
    - construct the array with inorder traversal
    - append the input value
    - construct the tree using the way we did for lc654
        1. find the max
        2. set the node with max value
        3. set the node.left with nums[:i] and node.right with nums[i+1:] recursively
    
    Time    O(N+N^2)
    Space   O(N)
    24 ms, faster than 28.96%
"""


class Solution(object):

    def __init__(self):
        self.nums = []

    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.inorder(root)
        self.nums.append(val)
        return self.constructMaximumBinaryTree(self.nums)

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        self.nums.append(root.val)
        self.inorder(root.right)

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


"""
    2nd: recursion
    
    there are 2 cases
    - if val > root, use val as root and put the old root as the left child of new root
    - else, recursively do the same thing on the right child(becos the val will be added on the right of the array)
    
    Time    O(N)
    Space   O(h)
    16 ms, faster than 82.62%
"""


class Solution(object):

    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None or val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        root.right = self.insertIntoMaxTree(root.right, val)
