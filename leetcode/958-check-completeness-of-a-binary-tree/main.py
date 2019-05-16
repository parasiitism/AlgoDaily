"""
    2nd approach:
	1. bfs and the queue finally should have all the leafs including null
	2. for a complete binary tree, there should not be any node after we met a null node in the final level

	e.g.1
				1
			2		3
		4 5	 6
	queue = [null, null, null, null, null, null, null]
	parent = 3		4	 4		5	 5		6	 6
	so it is complete

	e.g.2
				1
			2		3
		4 5	 		6
	queue = [null, 6, null, null, null, null]
	parent = 3	   3	4	4	   5	5

	Time	O(n)
	Space	O(h)
	0 ms, faster than 100.00%
"""


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        while q[0] != None:
            node = q.pop(0)
            q.append(node.left)
            q.append(node.right)
        while len(q) > 0 and q[0] == None:
            q.pop(0)
        return len(q) == 0
