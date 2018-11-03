import json


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


# my naive solution:
# json
# result = {
#     'value': root.val,
#     'children': []
# }
# it beats 42.49%, not that bad
class Codec:

    def serialize(self, root):
        if root is None:
            return

        def helper(node):
            if node is None:
                return
            result = {
                'value': node.val,
                'children': []
            }
            for child in node.children:
                result['children'].append(helper(child))
            return result

        final_dic = helper(root)
        return json.dumps(final_dic)

    def deserialize(self, data):
        if data == None or len(data) == 0:
            return None
        dictt = json.loads(data)

        def helper(node):
            if node == None:
                return None
            root = Node(node['value'], [])
            for child in node['children']:
                root.children.append(helper(child))
            return root

        return helper(dictt)


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
            temp = queue[0]
            queue = queue[1:]
            nodes_on_the_same_level.append(temp.val)
            # add its children to the queue
            for j in range(len(temp.children)):
                if temp.children[j] != None:
                    queue.append(temp.children[j])
        result.append(nodes_on_the_same_level)
    print(result)
    return result


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
test_level_order(d)
