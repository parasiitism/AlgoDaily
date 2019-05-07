# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: BFS + hashtable
    - BFS the tree level by level
    - use a hashtable to store [parent, currentnode]
    - after we have done the iterating one level, check if the x, y are on the same level and have diff parents

    Time    O(n)
    Space   O(n)
    12ms beats 100%
"""


class Solution(object):
    def isCousins(self, root, x, y):
        if root == None:
            return False
        # bfs starts with the root
        q = [(-1, root)]  # (parent, currentNode)
        while len(q) > 0:
            n = len(q)
            hs = {}
            # only iterate the nodes on the same layer
            for _ in range(n):
                # dequeue
                parent, node = q.pop(0)
                hs[node.val] = parent
                # enqueue if children are non-null
                if node.left != None:
                    q.append((node.val, node.left))
                if node.right != None:
                    q.append((node.val, node.right))
            # check if cousions
            if x in hs and y in hs:
                if hs[x] != hs[y]:
                    # yeah!!! nodes are on the same layer and have diff parents
                    return True
                else:
                    # description said that there would be no duplicate values, so it means no need to explore anymore
                    return False
        return False
