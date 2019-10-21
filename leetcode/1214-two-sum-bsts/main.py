# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: recursive dfs
    - traverse all the nodes in tree1 and tree2 and store them in 2 arrays
    - use a hashtable to do 2sum

    Time    O(2A+2B)
    Space   O(A+B)
    84 ms, faster than 46.15%
"""


class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        arr1, arr2 = [], []
        self.dfs(root1, arr1)
        self.dfs(root2, arr2)
        hs = set(arr1)
        for x in arr2:
            if target - x in hs:
                return True
        return False

    def dfs(self, node, arr):
        if node == None:
            return
        arr.append(node.val)
        self.dfs(node.left, arr)
        self.dfs(node.right, arr)


"""
    2nd: iterative dfs
    - traverse the nodes in tree1, and put the nodes into a hashset
    - traverse the nodes in tree2 to see if there is a counterpart

    Time    O(A+B)
    Space   O(A+B)
    64 ms, faster than 84.27%
"""


class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        if root1 == None or root2 == None:
            return False
        hs = set()
        stack = [root1]
        while len(stack) > 0:
            pop = stack.pop()
            hs.add(pop.val)
            if pop.left != None:
                stack.append(pop.left)
            if pop.right != None:
                stack.append(pop.right)

        stack = [root2]
        while len(stack) > 0:
            pop = stack.pop()
            if target - pop.val in hs:
                return True
            if pop.left != None:
                stack.append(pop.left)
            if pop.right != None:
                stack.append(pop.right)
        return False
