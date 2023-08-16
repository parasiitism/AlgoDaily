
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

"""
    1st: recursion
    - similar to lc236, 1644, 1650, 1676
    - find the root
    - do LCA

    Time    O(2N)
    Space   O(N)
    148 ms, faster than 100.00%
"""


class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        root = None
        cur = p
        while cur != None:
            root = cur
            cur = cur.parent

        return self.lca(root, p, q)

    def lca(self, node, p, q):
        if node == None or node == p or node == q:
            return node
        left = self.lca(node.left, p, q)
        right = self.lca(node.right, p, q)
        if left != None and right != None:
            return node
        if left != None:
            return left
        return right


"""
    2nd: iteration
    - find the common height
    - poping the nodes from P and Q until p === q

    Time    O(A+B)
    Space   O(1)
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        height_p = self.getHeight(p)
        height_q = self.getHeight(q)

        while height_p > height_q:
            p = p.parent
            height_p -= 1

        while height_p < height_q:
            q = q.parent
            height_q -= 1

        while p != q:
            p = p.parent
            q = q.parent

        return p

    def getHeight(self, node):
        h = 0
        cur = node
        while cur != None:
            h += 1
            cur = cur.parent
        return h
