"""
    1st: bfs+hashtable?
    - store the parent of each node, each node can only has one parent
    - a valid tree can only has one node

    corner case: there is a cycle, and there is another tree
    4
    [1,2,0,-1]
    [-1,-1,-1,-1]
    

    Time    O(N)
    Space   O(N)
    288 ms, faster than 33.86%
"""


class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        parents = n * [-1]
        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]

            if left != -1:
                if parents[left] != -1:
                    return False
                parents[left] = i

            if right != -1:
                if parents[right] != -1:
                    return False
                parents[right] = i
        # check if more than one root
        root = None
        for i in range(n):
            if parents[i] == -1:
                if root:
                    return False
                root = i
            if leftChild[i] != -1 and rightChild[i] != -1 and leftChild[i] == rightChild[i]:
                return False
            if leftChild[i] != -1 and leftChild[i] == parents[i]:
                return False
            if rightChild[i] != -1 and rightChild[i] == parents[i]:
                return False
        # check if cycle
        hs = set()
        q = [root]
        while len(q) > 0:
            head = q.pop(0)
            if head in hs:
                return False
            hs.add(head)
            left = leftChild[head]
            right = rightChild[head]
            if left != -1:
                q.append(left)
            if right != -1:
                q.append(right)

        return len(hs) == n


"""
    2nd: same as above but DFS
    272 ms, faster than 49.00%
"""


class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        parents = n * [-1]
        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]

            if left != -1:
                if parents[left] != -1:
                    return False
                parents[left] = i

            if right != -1:
                if parents[right] != -1:
                    return False
                parents[right] = i
        # check if more than one root
        root = None
        for i in range(n):
            if parents[i] == -1:
                if root:
                    return False
                root = i
            if leftChild[i] != -1 and rightChild[i] != -1 and leftChild[i] == rightChild[i]:
                return False
            if leftChild[i] != -1 and leftChild[i] == parents[i]:
                return False
            if rightChild[i] != -1 and rightChild[i] == parents[i]:
                return False
        # check if cycle
        hs = set()
        stack = [root]
        while len(stack) > 0:
            head = stack.pop()
            if head in hs:
                return False
            hs.add(head)
            left = leftChild[head]
            right = rightChild[head]
            if left != -1:
                stack.append(left)
            if right != -1:
                stack.append(right)

        return len(hs) == n
