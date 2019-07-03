# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: recursive dfs
    - sorted list is the inorder traversal of the BST
    - use suffixSum to calculate the target values
    - update the nodes' value with the suffixSums

    Time    O(3n)
    Space   O(n)
    72 ms, faster than 32.67%
"""


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        arr = []

        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        suffixMap = {}
        suffixSum = 0
        for i in range(len(arr)-1, -1, -1):
            suffixSum += arr[i]
            suffixMap[arr[i]] = suffixSum

        def addSuffixSum(node):
            if node == None:
                return
            node.val = suffixMap[node.val]
            addSuffixSum(node.left)
            addSuffixSum(node.right)
        addSuffixSum(root)
        return root


"""
    2nd approach: recursive dfs
    - sorted list is the inorder traversal of the BST
    - use suffixSum to calculate the target values
    - update the nodes' value with the suffixSums

    Time    O(2n)
    Space   O(n)
    88 ms, faster than 30.81%
"""


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        # reverse inorder + suffix sum
        suffixMap = {}
        suffixSum = 0

        def revInorder(node):
            nonlocal suffixSum
            if node == None:
                return
            revInorder(node.right)
            # suffix sum
            temp = suffixSum + node.val
            suffixMap[node.val] = temp
            suffixSum = temp
            revInorder(node.left)
        revInorder(root)

        # traverse again to update the values
        def addSuffixSum(node):
            if node == None:
                return
            node.val = suffixMap[node.val]
            addSuffixSum(node.left)
            addSuffixSum(node.right)
        addSuffixSum(root)
        return root
