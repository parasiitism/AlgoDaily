import json
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# my 1st approach
# bfs, iterative
# it is what leetcode does
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
        arr = json.loads(data)
        if len(arr) == 0:
            return None
        root = TreeNode(arr[0])
        queue = []
        queue.append(root)
        i = 1
        while len(queue) > 0:
            n = len(queue)
            for j in range(n):
                head = queue.pop(0)
                if i+2*j < len(arr) and arr[i+2*j] is not None:
                    left = TreeNode(arr[i+2*j])
                    head.left = left
                    queue.append(left)
                if i+2*j+1 < len(arr) and arr[i+2*j+1] is not None:
                    right = TreeNode(arr[i+2*j+1])
                    head.right = right
                    queue.append(right)
            i += 2*n
        return root


# for checking
def test_level_order(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    result = []
    if not root:
        return result
    queue = []
    queue.append(root)
    while len(queue) > 0:
        level = []
        level_node_count = len(queue)
        for idx in range(0, level_node_count):
            node = queue.pop(0)
            level.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        result.append(level)
    print(result)
    return result


#       1
#    2      3
#         4   5
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
c.right = e

# Your Codec object will be instantiated and called as such:
codec = Codec()
haha = codec.serialize(a)
print(haha)
node = codec.deserialize(haha)
test_level_order(node)
