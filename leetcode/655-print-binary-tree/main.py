# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: recursive DFS
    - depth first search to find the height
    - the heights are 1, 3, 7, 15,....which is n = 2**m-1
    - create an array for results
    - put each node into a correct cell by calculation

    e.g. these are the cell posistion in a tree with height = 4
            7
        3,      11
      1, 5,    9, 13
    0,2,4,6,8,10,12,14

    Time    O(2n)
    Space   O(n)
    24 ms, faster than 41.56%
"""


class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        n = self.findDepth(root)
        w = 2**n-1
        res = []
        for _ in range(n):
            res.append(w*[''])
        self.f(root, 0, w-1, 0, res)
        return res

    def findDepth(self, node):
        if node == None:
            return 0
        left = self.findDepth(node.left)
        right = self.findDepth(node.right)
        return max(left, right) + 1

    def f(self, node, start, end, i, res):
        if node == None:
            return
        mid = (start + end)//2
        res[i][mid] = str(node.val)
        self.f(node.left, start, mid-1, i+1, res)
        self.f(node.right, mid+1, end, i+1, res)


"""
    2nd: iterative DFS
    - depth first search to find the height
    - the heights are 1, 3, 7, 15,....which is n = 2**m-1
    - create an array for results
    - put each node into a correct cell by calculation

    e.g. these are the cell posistion in a tree with height = 4
            7
        3,      11
      1, 5,    9, 13
    0,2,4,6,8,10,12,14

    Time    O(2n)
    Space   O(n)
    20 ms, faster than 73.75%
"""


class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        stack = [(root, 1)]
        n = 0
        while len(stack) > 0:
            pop, h = stack.pop()
            n = max(n, h)
            if pop.left != None:
                stack.append((pop.left, h+1))
            if pop.right != None:
                stack.append((pop.right, h+1))

        w = 2**n-1
        res = []
        for i in range(n):
            res.append(w*[''])

        # node, start, end, level
        stack = [(root, 0, w-1, 0)]
        while len(stack) > 0:
            pop, start, end, i = stack.pop()
            mid = (start + end)//2
            res[i][mid] = str(pop.val)
            if pop.left != None:
                stack.append((pop.left, start, mid-1, i+1))
            if pop.right != None:
                stack.append((pop.right, mid+1, end, i+1))

        return res
