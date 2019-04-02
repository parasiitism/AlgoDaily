# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: bfs + hashtable

    this is a very weird question, the nodes on the same level(level order) are asked to be sorted

    Time    O(n)
    Space   O(n)
    28 ms, faster than 44.80%
"""


class Solution(object):

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        ht = {}
        # // left most col
        leftMostCol = 0

        q = []
        q.append((root, 0, 0))
        while len(q) > 0:
            n = len(q)
            for i in range(n):
                node, col, row = q.pop(0)
                if col not in ht:
                    ht[col] = [(node.val, row)]
                else:
                    ht[col].append((node.val, row))
                if col < leftMostCol:
                    leftMostCol = col
                if node.left != None:
                    q.append((node.left, col-1, row+1))
                if node.right != None:
                    q.append((node.right, col+1, row+1))

        # comparoter sort.Slice
        # sort by colLevel, order numerically if tie
        def compare(a, b):
            if a[1] < b[1]:
                return -1
            elif a[1] > b[1]:
                return 1
            else:
                return a[0]-b[0]

        res = []
        while leftMostCol in ht:
            temp = ht[leftMostCol]
            temp = sorted(temp, cmp=compare)
            trim = []
            for x in temp:
                trim.append(x[0])
            res.append(trim)
            leftMostCol += 1
        return res
