class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


# suggested solution:
# attach the number of children as a helper in string such that
# we dont need to deal with any parentheses
class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        result = []

        def dfs(node):
            if node == None:
                return
            result.append(str(node.val))
            result.append(str(len(node.children)))
            for child in node.children:
                dfs(child)
        dfs(root)
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == None or len(data) == 0:
            return None
        arr = data.split(',')

        def dfs():
            if len(arr) == 0:
                return
            root = Node(int(arr.pop(0)), [])
            children_count = int(arr.pop(0))
            for i in range(children_count):
                root.children.append(dfs())
            return root

        return dfs()


#       1
#   2   3   4
# 5
a = Node(1, [])
b = Node(2, [])
c = Node(3, [])
d = Node(4, [])
e = Node(5, [])
a.children = [b, c, d]
b.children = [e]

codec = Codec()
s = codec.serialize(a)
print(s)
d = codec.deserialize(s)
print(d)
