

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


class EncodeQueue(object):
    def __init__(self, node, is_first=False, parent=None):
        self.node = node
        self.is_first = is_first
        self.parent = parent


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
        result_root = None
        queue = []
        queue.append(EncodeQueue(root))
        while len(queue) > 0:
            size = len(queue)
            current = None
            # iterate the nodes on the same level
            for i in range(size):
                # add each node to an array
                temp = queue.pop(0)
                temp_node = TreeNode(temp.node.val)

                # construct the tree
                if result_root == None:
                    result_root = temp_node
                elif temp.is_first:
                    # 1st child
                    temp.parent.right = temp_node
                    current = temp_node
                else:
                    # sublings
                    current.left = temp_node
                    current = temp_node

                # add its children to the queue
                for j in range(len(temp.node.children)):
                    child = temp.node.children[j]
                    q_child = EncodeQueue(child, True if j ==
                                          0 else False, temp_node)
                    queue.append(q_child)

        return result_root

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.

        :type data: TreeNode
        :rtype: Node
        """


# test
def test_preorder(root):
    if root == None:
        return
    print(root.val)
    test_preorder(root.left)
    test_preorder(root.right)


def test_level_order(root):
    """
    :type root: Node
    :rtype: List[List[int]]
    """
    if root == None:
        return []
    result = []
    queue = []
    queue.append(root)
    while len(queue) > 0:
        size = len(queue)
        nodes_on_the_same_level = []
        # iterate the nodes on the same level
        for i in range(size):
                # add each node to an array
            temp = queue.pop(0)
            nodes_on_the_same_level.append(temp.val)
            # add its children to the queue
            if temp.left != None:
                queue.append(temp.left)
            if temp.right != None:
                queue.append(temp.right)
        result.append(nodes_on_the_same_level)
    print(result)
    return result


#       1
#   2   3   4
#      5 6    7
a = Node(1, [])
b = Node(2, [])
c = Node(3, [])
d = Node(4, [])
e = Node(5, [])
f = Node(6, [])
g = Node(7, [])

a.children = [b, c, d]
c.children = [e, f]
d.children = [g]

# Your Codec object will be instantiated and called as such:
codec = Codec()
# codec.decode(codec.encode(root))
t = codec.encode(a)
test_preorder(t)
test_level_order(t)
