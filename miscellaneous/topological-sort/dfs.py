class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # prepare a list to save to children for each node
        connections = []
        for i in range(numCourses):
            connections.append([])
        # iterate though the edges and put them into the corresponding node in the connections
        for prereq in prerequisites:
            pre, cur = prereq[0], prereq[1]
            connections[pre].append(cur)
        # iterate all the vertices
        seen = set()
        stack = []
        for i in range(numCourses):
            if i in seen:
                continue
            self.exploreVertex(connections, i, seen, stack)
        # result is the stack in a reversed order
        res = []
        while len(stack) > 0:
            res.append(stack.pop())
        return res

    def exploreVertex(self, connections, curIdx, seen, stack):
        seen.add(curIdx)
        children = connections[curIdx]
        for child in children:
            if child in seen:
                continue
            self.exploreVertex(connections, child, seen, stack)
        stack.append(curIdx)


print(Solution().findOrder(
    6, [[4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]]))
