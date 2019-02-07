class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # prepare a list to save to children for each node
        graph = []
        for i in range(numCourses):
            graph.append([])
        # iterate though the edges and put them into the corresponding node in the graph
        for prereq in prerequisites:
            pre, cur = prereq[0], prereq[1]
            graph[pre].append(cur)
        # iterate all the vertexes
        seen = set()
        stack = []
        for i in range(numCourses):
            if i in seen:
                continue
            self.exploreVertex(graph, i, seen, stack)
        # result is the stack in a reversed order
        res = []
        while len(stack) > 0:
            res.append(stack.pop())
        return res

    def exploreVertex(self, graph, curIdx, seen, stack):
        seen.add(curIdx)
        children = graph[curIdx]
        for child in children:
            if child in seen:
                continue
            self.exploreVertex(graph, child, seen, stack)
        stack.append(curIdx)


print(Solution().findOrder(
    6, [[4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]]))
