class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        !!! this method is known as topological sorting/ordering !!!

        1. create a list to save to children for each node
        2. for each node, put the children in
            e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
            children list = [[], [0], [3], [], [3], [2,4,1]]
        3. use a hashtable to store the visited node, 1=visiting, 2=visited
        4. use a stack to store the nodes which no longer has unvisited children
        5. the result is the stack in the reversed order

        Time    O(V+E)
        Space   O(V)
        36ms beats 98.29%
        """
        # prepare a list to save to children for each node
        graph = []
        for i in range(numCourses):
            graph.append([])
        # iterate though the edges and put them into the corresponding node in the graph
        for prereq in prerequisites:
            prev, cur = prereq[1], prereq[0]
            graph[prev].append(cur)
        # iterate all the vertexes
        seen = {}
        stack = []
        for i in range(numCourses):
            if i in seen:
                if seen[i] == 1:
                    return []
                elif seen[i] == 2:
                    continue
            if self.exploreVertex(graph, i, seen, stack) == False:
                return []
        # result is the stack in a reversed order
        res = []
        while len(stack) > 0:
            res.append(stack.pop())
        return res

    def exploreVertex(self, graph, curIdx, seen, stack):
        seen[curIdx] = 1
        children = graph[curIdx]
        for child in children:
            if child in seen:
                if seen[child] == 1:
                    return False
                elif seen[child] == 2:
                    continue
            if self.exploreVertex(graph, child, seen, stack) == False:
                return False
        seen[curIdx] = 2
        stack.append(curIdx)
        return True


print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2]]))

print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2], [5, 3]]))
