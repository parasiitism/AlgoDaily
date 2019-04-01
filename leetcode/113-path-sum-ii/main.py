class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: recursive dfs
    
    Time  O(n)
    Space O(h)
    44 ms, faster than 62.78%
"""


class Solution(object):

    def __init__(self):
        self.res = []

    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.helper(root, 0, [], target)
        return self.res

    def helper(self, node, prefixSum, prePath, target):
        if node == None:
            return
        cur = prefixSum + node.val
        path = prePath + [node.val]
        if node.left == None and node.right == None and cur == target:
            self.res.append(path)
        self.helper(node.left, cur, path, target)
        self.helper(node.right, cur, path, target)


"""
    2nd approach: iterative dfs
    
    Time  O(n)
    Space O(h)
    44 ms, faster than 62.78% 
"""


class StackItem(object):
    def __init__(self, node, prefixSum=0, path=[]):
        self.node = node
        self.prefixSum = prefixSum
        self.path = path


class Solution(object):

    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        stack = []
        stack.append(StackItem(root))
        while len(stack) > 0:
            pop = stack.pop()
            node = pop.node
            cur = pop.prefixSum + node.val
            path = pop.path + [node.val]
            if node.left == None and node.right == None and cur == target:
                res.append(path)
            if node.left != None:
                stack.append(StackItem(node.left, cur, path))
            if node.right != None:
                stack.append(StackItem(node.right, cur, path))
        return res
