# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: convert the tree to a graph + bfs + hashtable
    - construct a adjacent list of a node like [node, parent, left, right]
    - put the adjacent list with node.val as the key
    - bfs through the edges to find out the shortest path
    - use a hashset to avoid redundant visiting
    
    Time    O(N+E)
    Space   O(N)
    44 ms, faster than 67.40%
"""


class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None or k < 1 or k > 1000:
            return -1
        # iterative dfs the tree
        # to construct [node, parent, left, right]
        m = {}
        stack = [(root, -1)]
        while len(stack) > 0:
            node, parent = stack.pop()
            if node.left == None and node.right == None:
                m[node.val] = [node.val, parent, -1, -1]
            elif node.left == None:
                m[node.val] = [node.val, parent, -1, node.right.val]
            elif node.right == None:
                m[node.val] = [node.val, parent, node.left.val, -1]
            else:
                m[node.val] = [node.val, parent, node.left.val, node.right.val]

            if node.left != None:
                stack.append((node.left, node.val))
            if node.right != None:
                stack.append((node.right, node.val))
        # bfs through the edges start from the node with value of k
        q = []
        q.append(m[k])
        # avoid redundant calculation
        seen = set()
        while len(q) > 0:
            cur, parent, left, right = q.pop(0)
            if cur in seen:
                continue
            seen.add(cur)
            if left == -1 and right == -1:
                return cur
            if parent != -1:
                q.append(m[parent])
            if left != -1:
                q.append(m[left])
            if right != -1:
                q.append(m[right])
        # actually we wont reach here LOL
        return -1
