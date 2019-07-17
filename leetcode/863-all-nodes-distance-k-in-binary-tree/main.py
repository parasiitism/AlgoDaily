"""
    In short, just transform the tree into a graph and do bfs or dfs.

    e.g.
    {
        val1 : [parent1, left1, right1],
        val2 : [parent2, left2, right2],
        ....
    }

    Time O(N)
    Space O(N)
    24 ms, faster than 97.55%
"""


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        connections = {}

        def dfs(node, parent):
            if node == None:
                return
            arr = [parent, -1, -1]
            if node.left != None:
                arr[1] = node.left.val
                dfs(node.left, node.val)
            if node.right != None:
                arr[2] = node.right.val
                dfs(node.right, node.val)
            connections[node.val] = arr
        dfs(root, -1)

        q = [(target.val, 0)]
        seen = set()
        res = []
        while len(q) > 0:
            node, steps = q.pop(0)
            if node in seen:
                continue
            seen.add(node)
            if node == -1:
                continue
            if steps == K:
                res.append(node)
                continue
            children = connections[node]
            for child in children:
                q.append((child, steps + 1))
        return res
