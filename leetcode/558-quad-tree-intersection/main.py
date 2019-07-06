"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

"""
1st approach: recursive dfs
- my intuitive approach is just to dfs the trees BUT we need to consider 2 corner cases:
	- e.g.2 a false leaf BUT its counterpart is a QTree
	- e.g.3 all children have the same values
- actually i am not sure what 'val' should i return if it is not a leaf, therefore i put None and leetcode ACCEPTED lol


e.g. 1
A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       | F | F |  |       |       |
|   T   |   T   |  |   T   +---+---+  |   T   |   T   |
|       |       |  |       | T | T |  |       |       |
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |       |       |
|   F   |   F   |  |   T   |   F   |  |   T   |   F   |
|       |       |  |       |       |  |       |       |
+-------+-------+  +-------+-------+  +-------+-------+

e.g.2
A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       | F | F |  |       | F | F |
|   T   |   F   |  |   T   +---+---+  |   T   |---+---+ 
|       |       |  |       | T | T |  |       | T | T |
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |       |       |
|   F   |   F   |  |   T   |   F   |  |   T   |   F   |
|       |       |  |       |       |  |       |       |
+-------+-------+  +-------+-------+  +-------+-------+

e.g.3
A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |               |
|   T   |   T   |  |   T   |   T   |  |               |
|       |       |  |       |       |  |               |
+-------+-------+  +-------+---+---+  +       T       |
|       |       |  |       |       |  |               |
|   F   |   T   |  |   T   |   T   |  |               |
|       |       |  |       |       |  |               |
+-------+-------+  +-------+-------+  +-------+-------+

Time    O(n) we just need to visit all nodes at most once
Space   O(h) depend one the depth of the trees
220 ms, faster than 97.22%
"""


class Solution(object):
    def intersect(self, t1, t2):
        if t1.isLeaf and t2.isLeaf:
            return Node(t1.val or t2.val, True, None, None, None, None)
        elif t1.isLeaf:
            if t1.val == True:
                # e.g.1
                return Node(True, True, None, None, None, None)
            else:
                # e.g.2
                return t2
        elif t2.isLeaf:
            if t2.val == True:
                # e.g.1
                return Node(True, True, None, None, None, None)
            else:
                # e.g.2
                return t1
        else:
            a = self.intersect(t1.topLeft, t2.topLeft)
            b = self.intersect(t1.topRight, t2.topRight)
            c = self.intersect(t1.bottomLeft, t2.bottomLeft)
            d = self.intersect(t1.bottomRight, t2.bottomRight)
            # if all children have the same value, merge them into one node
            if a.isLeaf and b.isLeaf and c.isLeaf and d.isLeaf:
                total = a.val + b.val + c.val + d.val
                if total == 4:
                    return Node(True, True, None, None, None, None)
                elif total == 0:
                    return Node(False, True, None, None, None, None)
            # else, keep 4 children
            return Node(None, False, a, b, c, d)

    def dfs(self, t):
        if t == None:
            return False
        if t.isLeaf:
            return t.val
        return self.dfs(t.topLeft) or\
            self.dfs(t.topRight) or\
            self.dfs(t.bottomLeft) or\
            self.dfs(t.bottomRight)
