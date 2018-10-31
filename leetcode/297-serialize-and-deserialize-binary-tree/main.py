# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            for i in range(len(queue)):
                head = queue.pop(0)
                if head != None:
                    result.append(head.val)
                    if head.left != None:
                        queue.append(head.left)
                    else:
                        queue.append(None)
                    if head.right != None:
                        queue.append(head.right)
                    else:
                        queue.append(None)
                else:
                    result.append(None)
        # remove tailing nulls
        for i in range(len(result)):
            idx = len(result) - 1
            if result[idx] is None:
                result.pop()
        # to string
        temp = ','.join(str(e) if e is not None else 'null' for e in result)
        return '['+temp+']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


#       1
#    2      3
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
# a.left = b
a.right = c

# Your Codec object will be instantiated and called as such:
codec = Codec()
# codec.deserialize(codec.serialize(root))
print(codec.serialize(a))
