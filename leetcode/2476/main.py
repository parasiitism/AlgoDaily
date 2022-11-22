# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: Binary Search Tree traversal

    Time    O(QlogN)
    Space   O(H)
    
    LTE: Since the BST might not be balanced, the potential time complexity can be O(N).
"""


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        res = []
        for q in queries:
            x = self.smallerEqual(root, q)
            y = self.largerEqual(root, q)
            if x == -2**32:
                x = -1
            if y == 2**32:
                y = -1
            res.append((x, y))
        return res

    def smallerEqual(self, node, target):
        cur = node
        maxSmaller = -2**32
        while cur != None:
            if target < cur.val:
                cur = cur.left
            elif target > cur.val:
                maxSmaller = cur.val
                cur = cur.right
            else:
                return cur.val
        return maxSmaller

    def largerEqual(self, node, target):
        cur = node
        minLarger = 2**32
        while cur != None:
            if target < cur.val:
                minLarger = cur.val
                cur = cur.left
            elif target > cur.val:
                cur = cur.right
            else:
                return cur.val
        return minLarger


"""
    2nd: binary search

    Time    O(QlogN)
    Space   O(H)
    2033 ms, faster than 100.00%
"""


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        sorted_arr = []

        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            sorted_arr.append(node.val)
            inorder(node.right)
        inorder(root)
        n = len(sorted_arr)
        res = []
        for q in queries:
            i = self.bsearch_left(sorted_arr, q)
            j = self.bsearch_right(sorted_arr, q)
            x, y = -1, -1
            if 0 <= i < n:
                x = sorted_arr[i]
            if 0 <= j < n:
                y = sorted_arr[j]
            res.append([x, y])
        return res

    def bsearch_left(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        # to find number that <= target
        return right

    def bsearch_right(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        # to find number that >= target
        return left
