import sys
from collections import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: BFS
    - on each level, sum up all the node.val and update the temporary result if necessary

    Time    O(N)
    Space   O(N)
    364 ms, faster than 49.43%
"""


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        maxLevel = 0
        maxTotal = -sys.maxsize
        q = [root]
        cur = 0
        while len(q) > 0:
            n = len(q)
            total = 0
            cur += 1
            for i in range(n):
                head = q.pop(0)
                total += head.val
                if head.left != None:
                    q.append(head.left)
                if head.right != None:
                    q.append(head.right)
            if total > maxTotal:
                maxTotal = total
                maxLevel = cur
        return maxLevel


"""
    2nd: iterative DFS + hastable
    - on each level, sum up all the node.val and update the temporary result if necessary
    - use a hashtable to store the sum each level

    Time    O(N)
    Space   O(N)
    388 ms, faster than 27.14% 
"""


class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        counts = defaultdict(int)
        stack = [(root, 1)]
        while len(stack) > 0:
            node, level = stack.pop()
            counts[level] += node.val
            if node.left != None:
                stack.append((node.left, level + 1))
            if node.right != None:
                stack.append((node.right, level + 1))
        maxLevel = 0
        maxTotal = -sys.maxsize
        for key in counts:
            if counts[key] > maxTotal:
                maxTotal = counts[key]
                maxLevel = key
        return maxLevel
