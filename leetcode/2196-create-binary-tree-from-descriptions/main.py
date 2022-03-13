# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    1st: graph
    - build a graph
    - use the graph to build the binary tree

    Time    O(N)
    Space   O(N)
    2436 ms, faster than 53.85%
"""


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        g = defaultdict(dict)
        children = set()
        for p, c, isLeft in descriptions:
            if isLeft:
                g[p][0] = c
            else:
                g[p][1] = c
            children.add(c)
        rootKey = None
        for key in g:
            if key not in children:
                rootKey = key
                break
        if rootKey == None:
            return None

        def dfs(key):
            node = TreeNode(key)
            if 0 in g[key]:
                node.left = dfs(g[key][0])
            if 1 in g[key]:
                node.right = dfs(g[key][1])
            return node

        root = dfs(rootKey)

        return root
