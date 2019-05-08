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
        if root == None:
            return []
        # m is the hashtable to store the adjacent list of a node. e.g. val1 : [parent, left, right]
        m = {}
        self.dfs(root, -1, m)
        # in case target is not in the tree
        if target.val not in m:
            return []
        # avoid revisting
        res = []
        seen = set()
        # bfs
        q = [(target.val, 0)]
        while len(q) > 0:
            head, steps = q.pop(0)
            # avoid revisting
            if head in seen:
                continue
            seen.add(head)
            # if steps == k
            if steps == K and head > -1:
                res.append(head)
            elif steps < K:
                # get the adjacent list and traverse
                if head in m:
                    children = m[head]
                    for child in children:
                        q.append((child, steps+1))
        return res
        
    def dfs(self, node, parent, m):
        """
        dfs through the tree to construct a adjacent list for each node
        {
            val1 : [parent1, left1, right1],
            val2 : [parent2, left2, right2],
            ....
        }
        """
        if node == None:
            return
        arr = [parent, -1, -1]
        if node.left != None:
            arr[1] = node.left.val
            self.dfs(node.left, node.val, m)
        if node.right != None:
            arr[2] = node.right.val
            self.dfs(node.right, node.val, m)
        m[node.val] = arr