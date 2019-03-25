# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    questions to ask:
    - negative numbers?
"""


class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        1st approach: dfs + hashtable
        - for each node, calculate its children sum
        - calculate the total sum as well
        - dfs again to check if total - cur == cur

        corner cases:
        - [0,null,0]
        - [0,-1,1]

        88 ms, faster than 21.48%
        """
        m = {}
        total = self.calSum(root, m)

        stack = [root]
        while len(stack) > 0:
            pop = stack.pop()

            # check if total is in the map
            # important: we can only remove edge(not root)
            if pop != root and total == 2*m[pop]:
                return True

            if pop.left != None:
                stack.append(pop.left)
            if pop.right != None:
                stack.append(pop.right)
        return False

    def calSum(self, node, m):
        if node == None:
            return 0
        left = self.calSum(node.left, m)
        right = self.calSum(node.right, m)
        curSum = left + node.val + right
        m[node] = curSum
        return curSum
