# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


"""
    1st approach: bfs

    Time    O(n)
    Space   O(2w)
    56 ms, faster than 82.66%
"""


class Solution:
    # @param root, a tree link node
    # @return TreeLinkNode
    def connect(self, root):
        if root == None:
            return
        queue = [root]
        while len(queue) > 0:
            cnt = len(queue)
            prev = None
            for i in range(cnt):
                head = queue.pop(0)
                # here is the crux
                head.next = prev
                prev = head
                # add items into queue
                if head.right != None:
                    queue.append(head.right)
                if head.left != None:
                    queue.append(head.left)
    return root


#     5
#   3   6
# 2  4
# 1
a = TreeLinkNode(5)
b = TreeLinkNode(3)
c = TreeLinkNode(6)
d = TreeLinkNode(2)
e = TreeLinkNode(4)
f = TreeLinkNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = f

ans = Solution().connect(a)
