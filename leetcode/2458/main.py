# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
    - recursion
    - learned from others

    ref:
    - https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/discuss/2757990/Python-3-Explanation-with-pictures-DFS

    Time    O(N)
    Space   O(N)
    3916 ms, faster than 9.06%
"""


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        cached = {}

        @cache
        def get_height(node):
            if node == None:
                return 0
            left = get_height(node.left)
            right = get_height(node.right)
            return max(left, right) + 1

        def dfs(node, depth, max_height):
            if node == None:
                return
            # if we remove this node, the subtree will be removed, we stop here. The res = its cousins'
            cached[node.val] = max_height
            # possibly when we remove left child, we will need to compute the height thru right child
            dfs(node.left, depth + 1, max(max_height, depth + get_height(node.right)))
            # vice-versa
            dfs(node.right, depth + 1, max(max_height, depth + get_height(node.left)))
        dfs(root, 0, 0)

        res = []
        for q in queries:
            res.append(cached[q])
        return res
