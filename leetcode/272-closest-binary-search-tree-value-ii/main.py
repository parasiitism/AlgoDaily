import heapq

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.pq = []

    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.dfs(root, target)
        res = []
        for i in range(k):
            res.append(heapq.heappop(self.pq))
        return res

    def dfs(self, node, target):
        if node == None:
            return
        heapq.heappush(pq, (abs(target-node.val), node.val))
        self.dfs(node.left, target)
        self.dfs(node.right, target)
