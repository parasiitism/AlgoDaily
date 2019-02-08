class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        1st approach: Topological Ordering in DFS

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
        connections = []
        for i in range(numCourses):
            connections.append([])
        # iterate though the edges and put them into the corresponding node in the graph
        for prereq in prerequisites:
            prev, cur = prereq[1], prereq[0]
            connections[prev].append(cur)
        # iterate all the vertexes
        seen = {}
        stack = []
        for i in range(numCourses):
            if i in seen:
                if seen[i] == 1:
                    return []
                elif seen[i] == 2:
                    continue
            if self.exploreVertex(connections, i, seen, stack) == False:
                return []
        # result is the stack in a reversed order
        res = []
        while len(stack) > 0:
            res.append(stack.pop())
        return res

    def exploreVertex(self, connections, curIdx, seen, stack):
        seen[curIdx] = 1
        children = connections[curIdx]
        for child in children:
            if child in seen:
                if seen[child] == 1:
                    return False
                elif seen[child] == 2:
                    continue
            if self.exploreVertex(connections, child, seen, stack) == False:
                return False
        seen[curIdx] = 2
        stack.append(curIdx)
        return True


print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2]]))

print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2], [5, 3]]))


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        2nd appraoch: Topological Ordering in BFS

        1. create a list to save to children for each node
        2. for each node, put the children in
            e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
            children list = [[], [0], [3], [], [3], [2,4,1]]
        3. use a hashtable to store the visited node, 1=visiting, 2=visited
        4. use a stack to store the nodes which no longer has unvisited children
        5. the result is the stack in the reversed order

        Time    O(V+E)
        Space   O(V)
        32ms beats 98.29%
        """
        # prepare a list to save to children for each node
        connections = []
        indegree = []
        for i in range(numCourses):
            connections.append([])
            indegree.append(0)
        # iterate though the edges and put them into the corresponding node in the connections
        for prereq in prerequisites:
            prev, cur = prereq[1], prereq[0]
            connections[prev].append(cur)
            indegree[cur] += 1

        # put the nodes which has no incoming edges
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        # a count to check if the graph has a cycle
        # if there is a cycle, there will be a node's indegree never becomes 0
        # it means it will not be push to the queue therefore the the cnt will be inconsistent with the numCourses
        cnt = 0
        while len(queue) > 0:
            head = queue.pop(0)
            res.append(head)
            cnt += 1
            children = connections[head]
            for child in children:
                # subtract 1 for all destinations which the current node points(prereq) to
                indegree[child] -= 1
                # if indegree of that child is 0, out it to the queue
                if indegree[child] == 0:
                    queue.append(child)

        if cnt == numCourses:
            return res
        return []


print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2]]))

print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2], [5, 3]]))
