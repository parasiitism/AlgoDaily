# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: graph
    1. transform the tree into a graph
    2. count the number of nodes connecting to the parent, left and right of the input x
    3. compare the number of connected nodes and return the result

    Time    O(2n)
    Space   O(n)
    24 ms, faster than 29.51%
"""


class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.graph = {}
        self.dfs(root, None)
        parent, left, right = self.graph[x]
        a = self.countNodes(parent, x)
        b = self.countNodes(left, x)
        c = self.countNodes(right, x)
        return a > b + c + 1 or b > a + c + 1 or c > a + b + 1

    def dfs(self, node, parent):
        if node == None:
            return
        self.graph[node.val] = [parent, None, None]
        if node.left != None:
            self.graph[node.val][1] = node.left.val
            self.dfs(node.left, node.val)
        if node.right != None:
            self.graph[node.val][2] = node.right.val
            self.dfs(node.right, node.val)

    def countNodes(self, start, excluding):
        if start == None:
            return 0
        count = 0
        seen = set([excluding])
        q = [start]
        while len(q) > 0:
            head = q.pop(0)
            if head in seen:
                continue
            seen.add(head)
            count += 1
            cands = self.graph[head]
            for cand in cands:
                if cand != None:
                    q.append(cand)
        return count
