from heapq import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = [root]
        minheap = []
        while len(q) > 0:
            n = len(q)
            level_sum = 0
            for i in range(n):
                node = q.pop(0)
                level_sum += node.val
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            heappush(minheap, level_sum)
            if len(minheap) > k:
                heappop(minheap)
        if len(minheap) < k:
            return -1
        return minheap[0]