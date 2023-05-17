"""
    breadth first search

    Time    O(N)
    Space   O(W)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [(root, None)]
        while len(q) > 0:
            n = len(q)
            total = 0
            ht = Counter()
            nodes_parents = q[:n]
            for i in range(n):
                node, parent = nodes_parents[i]
                total += node.val
                ht[parent] += node.val
            for i in range(n):
                node, parent = q.pop(0)
                node.val = total - ht[parent]
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
        return root
