# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def print_tree(key, arr):
#     res = []
#     for node in arr:
#         res.append(node.val)
#     print(key, res)

"""
    BFS
    - very annoying implementation

    Time    O(N)
    Space   O(N)
    4147 ms, faster than 24.34%
"""


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [(root, 0)]
        odd_row_parents = []
        odd_row_nodes = []

        def f():
            children = [node.val for node in odd_row_nodes]
            # print_tree('f', odd_row_parents)
            # print(children)
            while len(odd_row_parents) > 0:
                p = odd_row_parents.pop(0)
                right = children.pop()
                left = children.pop()
                p.left.val = right
                p.right.val = left
            # print(odd_row_parents)
            # print(children)

        while len(q) > 0:
            n = len(q)
            _odd_row_parents = []
            for _ in range(n):
                node, level = q.pop(0)
                if level % 2 == 1:
                    odd_row_nodes.append(node)
                else:
                    _odd_row_parents.append(node)

                if node.left != None:
                    q.append((node.left, level+1))
                if node.right != None:
                    q.append((node.right, level+1))
            # print_tree('after for', _odd_row_parents)
            if len(odd_row_parents) > 0 and len(odd_row_nodes) > 0:
                f()
                odd_row_nodes = []
            odd_row_parents = _odd_row_parents
        # print(len(odd_row_parents), len(odd_row_nodes))
        if len(odd_row_parents) > 0 and len(odd_row_nodes) > 0:
            f()
        return root
