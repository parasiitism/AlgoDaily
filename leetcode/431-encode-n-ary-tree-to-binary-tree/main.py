

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # The left child of each node in the binary tree is the next sibling of the node in the N-ary tree.
    # The right child of each node in the binary tree is the first child of the node in the N-ary tree.
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.

        :type root: Node
        :rtype: TreeNode
        """
        if root == None:
            return []
        result = None
        current = None
        queue = []
        queue.append(root)
        while len(queue) > 0:
            size = len(queue)
            # iterate the nodes on the same level
            for i in range(size):
                # add each node to an array
                temp = queue.pop(0)

                # add its children to the queue
                for j in range(len(temp.children)):
                    if temp.children[j] != None:
                        queue.append(temp.children[j])

        return result

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.

        :type data: TreeNode
        :rtype: Node
        """


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
