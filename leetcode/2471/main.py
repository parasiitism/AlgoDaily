# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    BFS + min swap to sort an array

    Time    O(NlogN)
    Space   O(N)
    3797 ms, faster than 11.11%
"""
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = [root]
        while len(q) > 0:
            n = len(q)
            level = []
            for i in range(n):
                node = q.pop(0)
                if node == None:
                    continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            res += self.count_swap(level)
        return res
        
    def count_swap(self, A):
        n = len(A)
        B = sorted(A)
        value2idx = {}
        # store index of elements in A
        for i in range(n):
            value2idx[A[i]] = i
        cnt = 0
        for i in range(n):
			# If element in A is out of position, we need to swap hence increase cnt
            if (A[i] != B[i]):
                cnt += 1
                j = A[i]
				# Replace it with element that should be at this "i" in A using B[i]
                A[i], A[value2idx[B[i]]] = A[value2idx[B[i]]], A[i]
				# Update the indexes for swaped elements in "value2idx"
                value2idx[j] = value2idx[B[i]]
                value2idx[B[i]] = i

        return cnt
