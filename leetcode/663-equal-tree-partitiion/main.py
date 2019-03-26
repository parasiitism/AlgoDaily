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


class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        2nd approach: dfs + hashset, learned from others
        - for each node, calculate its children sum
        - calculate the total sum as well
        - dfs again to check if total - cur == cur

        compare to the 1st approach:
        - actually we dont need to care if there are duplicate sum values,
        because if there are, lets say 2 same values , it means that we can cut the tree in 2 ways

        ref:
        - https://leetcode.com/problems/equal-tree-partition/discuss/106727/javac-simple-solution-with-only-one-hashmap

        corner cases:
        - [0,null,0]
        - [0,-1,1]

        76 ms, faster than 45.64%
        """
        if root == None:
            return False
        m = set()
        # we should not add total to the hashset
        # otherwise we are not partitioning the tree
        total = root.val + \
            self.calSum(root.left, m) + self.calSum(root.right, m)
        return total % 2 == 0 and total / 2 in m

    def calSum(self, node, m):
        if node == None:
            return 0
        left = self.calSum(node.left, m)
        right = self.calSum(node.right, m)
        curSum = left + node.val + right
        m.add(curSum)
        return curSum
