# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    1st approach: recursion

    on each node, 

    the max value should be amongst
    - current node val
    - left branch sum + current node val
    - right branch sum + current node val
    - left branch sum + current node val + right branch sum

    since we only count branches' sum but not the total nodes' sum from each sub tree
    , we should just return the max amongst
    - current node val
    - left branch sum + current node val
    - right branch sum + current node val

    Time    O(n)
    Space   O(h)
    92 ms, faster than 44.15%
"""


class Solution(object):

    def __init__(self):
        self.res = -sys.maxsize

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node == None:
            return 0

        mid = node.val
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        midLeft = left + mid
        midRight = mid + right
        midLeftRight = left + mid + right

        onlyBranches = max(mid, max(midLeft, midRight))

        # the max value should be amongst
        # - current node val
        # - left branch sum + current node val
        # - right branch sum + current node val
        # - left branch sum + current node val + right branch sum
        temp = max(onlyBranches, midLeftRight)
        self.res = max(self.res, temp)

        # return the max amongst
        # - current node val
        # - left branch sum + current node val
        # - right branch sum + current node val
        return onlyBranches
