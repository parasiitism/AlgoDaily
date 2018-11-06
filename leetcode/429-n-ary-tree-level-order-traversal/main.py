class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
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
        return result


#       1
#   2   3   4
#  5 6
# 7
a = Node(1, [])
b = Node(2, [])
c = Node(3, [])
d = Node(4, [])
e = Node(5, [])
f = Node(6, [])
g = Node(7, [])

a.children = [b, c, d]
b.children = [e, f]
e.children = [g]

ans = Solution().levelOrder(a)
print("ans=", ans)
