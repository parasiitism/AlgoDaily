# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: inorder traversal + merge 2 lists

    Time    O(M+N)
    Space   O(M+N)
    388 ms, faster than 39.18%
"""


class Solution(object):
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.arr1, self.arr2 = [], []
        self.inorder(root1, self.arr1)
        self.inorder(root2, self.arr2)
        return self.merge2lists(self.arr1, self.arr2)

    def inorder(self, root: TreeNode, arr: List[int]):
        if root == None:
            return
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)

    def merge2lists(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        if i < len(arr1):
            res += arr1[i:]
        if j < len(arr2):
            res += arr2[j:]
        return res
