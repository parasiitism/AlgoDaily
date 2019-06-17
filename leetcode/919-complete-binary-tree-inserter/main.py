# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    1st approach: BFS
    - when init, we put the single-child or no-children nodes into a queue
    - when insert, assign the new node to the left or right of the first node in the queue
    - pop the first node if it contains 2 children

    Time of init()      O(n)
    Time of insert()    O(1)
    Time of insert()    O(1)
    Space               O(n)
    44 ms, faster than 95.45%
"""


class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.q = []
        q = [root]
        while len(q) > 0:
            pop = q.pop(0)
            if (pop.left == None and pop.right == None)\
                    or (pop.right == None):
                self.q.append(pop)
            if pop.left != None:
                q.append(pop.left)
            if pop.right != None:
                q.append(pop.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        first = self.q[0]
        parent = first
        if first.left == None:
            first.left = node
            self.q.append(node)
        elif first.right == None:
            first.right = node
            self.q.append(node)

        if first.left != None and first.right != None:
            self.q.pop(0)
        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
