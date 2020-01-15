# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st: bfs, level by level

    Time    O(N)
    Space   O(N)
    100 ms, faster than 49.46%
"""


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = [root]
        res = 0
        while len(q) > 0:
            n = len(q)
            total = 0
            for _ in range(n):
                head = q.pop(0)
                total += head.val
                if head.left != None:
                    q.append(head.left)
                if head.right != None:
                    q.append(head.right)
            res = total
        return res


"""
    2nd: recursive dfs
    - record the running maxLevel
    - update/accumulate sum for each level

    Time    O(N)
    Space   O(N)
    100 ms, faster than 49.46%
"""


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.maxLevel = 0
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, level):
        if root == None:
            return
        if level > self.maxLevel:
            self.res = root.val
            self.maxLevel = level
        elif level == self.maxLevel:
            self.res += root.val
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
