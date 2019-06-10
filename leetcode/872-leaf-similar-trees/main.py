# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: recursive dfs
    
    Time    O(n)
    Space   O(n) the string
    16 ms, faster than 96.43%
"""


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.a = ""

        def dfsA(node):
            if node == None:
                return
            if node.left == None and node.right == None:
                self.a += str(node.val) + ','
            dfsA(node.left)
            dfsA(node.right)
        dfsA(root1)

        self.b = ""

        def dfsB(node):
            if node == None:
                return
            if node.left == None and node.right == None:
                self.b += str(node.val) + ','
            dfsB(node.left)
            dfsB(node.right)
        dfsB(root2)
        return self.a == self.b


"""
    2nd approach: iterative dfs
    
    Time    O(n)
    Space   O(n) the string
    16 ms, faster than 96.43%
"""


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        a = ""
        stackA = [root1]
        while len(stackA) > 0:
            pop = stackA.pop()
            if pop.left == None and pop.right == None:
                a += str(pop.val) + ','
            if pop.right != None:
                stackA.append(pop.right)
            if pop.left != None:
                stackA.append(pop.left)

        b = ""
        stackB = [root2]
        while len(stackB) > 0:
            pop = stackB.pop()
            if pop.left == None and pop.right == None:
                b += str(pop.val) + ','
            if pop.right != None:
                stackB.append(pop.right)
            if pop.left != None:
                stackB.append(pop.left)
        return a == b
