# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        res = []
        q = []
        q.append(root)
        cnt = 0
        while len(q) > 0:
            n = len(q)
            temp = []
            for i in range(n):
                head = q.pop(0)
                if cnt % 2 == 0:
                    temp.append(head.val)
                else:
                    temp.insert(0, head.val)
                if head.left != None:
                    q.append(head.left)
                if head.right != None:
                    q.append(head.right)
            res.append(temp)
            cnt += 1
        return res
