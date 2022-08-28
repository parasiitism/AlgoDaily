# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
    - transform tree into a graph
    - find the longest distance

    Time    O(N)
    Space   O(N)
    1986 ms, faster than 25.00%
"""


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = {}

        def dfs(node, parent):
            arr = [None, None, None]
            if parent != None:
                arr[0] = parent.val
            if node.left != None:
                arr[1] = node.left.val
                dfs(node.left, node)
            if node.right != None:
                arr[2] = node.right.val
                dfs(node.right, node)
            g[node.val] = arr
        dfs(root, None)

        res = 0
        q = [(start, 0)]
        seen = set()
        while len(q) > 0:
            node, steps = q.pop(0)
            if node in seen:
                continue
            seen.add(node)
            res = max(res, steps)
            if node not in g:
                continue
            for nb in g[node]:
                if nb != None:
                    q.append((nb, steps + 1))

        return res
