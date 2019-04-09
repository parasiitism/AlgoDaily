# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: dfs + hashtable
    - count the sum recursively from bottom
    - count the occurence using a hashtable
    - find out the nodes with max count and aggregate them

    Time  O(n)
    Space O(n)
    48 ms, faster than 53.27% 
"""


class Solution(object):

    def __init__(self):
        self.ht = {}

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        total = self.helper(root)
        maxCount = 0
        res = []
        for key in self.ht:
            if self.ht[key] > maxCount:
                res = [key]
                maxCount = self.ht[key]
            elif self.ht[key] == maxCount:
                res.append(key)
        return res

    def helper(self, node):
        if node == None:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        count = left + node.val + right
        if count in self.ht:
            self.ht[count] += 1
        else:
            self.ht[count] = 1
        return count
