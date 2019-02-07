class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        1st approach:
        1. create a list to save to children for each node
        2. for each node, put the children in
            e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
            children list = [[], [0], [3], [], [3], [2,4,1]]
        3. dfs each node to see if there is a cycle
        4. return true if no cycle
        - TLE
        """
        graph = []
        for i in range(numCourses):
            graph.append([])

        for prereq in prerequisites:
            pre, cur = prereq[0], prereq[1]
            graph[pre].append(cur)

        for i in range(len(graph)):
            if self.dfs(graph, i, {}) == False:
                return False

        return True

    def dfs(self, graph, curIdx, seen):

        if curIdx in seen:
            return False
        newSeen = {curIdx}.union(seen)

        children = graph[curIdx]
        for child in children:
            if self.dfs(graph, child, newSeen) == False:
                return False

        return True


# a = {'a', 'b'}
# b = {'c'}.union(a)
# c = {}
# print(a)
# print(b)
# print('c' in a)
# print('c' in b)

print(Solution().canFinish(2, [[1, 0]]))
print(Solution().canFinish(2, [[0, 1], [1, 0]]))
print(Solution().canFinish(
    6, [[4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]]))
print(Solution().canFinish(
    6, [[4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3], [3, 5]]))


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        2nd approach:
        !!! actually i was almost there !!!
        !!! this method is known as topological sorting/ordering !!!
        1. create a list to save to children for each node
        2. for each node, put the children in
            e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
            children list = [[], [0], [3], [], [3], [2,4,1]]
        3. dfs each node to see if there is a cycle
        4. return true if no cycle

        32ms beats 94.33%
        """

        # prepare a list to save to children for each node
        graph = []
        for i in range(numCourses):
            graph.append([])
        # iterate though the edges and put them into the corresponding node in the graph
        for prereq in prerequisites:
            pre, cur = prereq[0], prereq[1]
            graph[pre].append(cur)
        # iterate though the nodes and see if there is a cycle
        seen = {}
        for i in range(len(graph)):
            if self.dfs(graph, i, seen) == False:
                return False

        return True

    def dfs(self, graph, curIdx, seen):
        if curIdx in seen:
            if seen[curIdx] == 2:
                # if seen[curIdx] == 2, it meas this node has been visited and no cycle is detected
                return True
            elif seen[curIdx] == 1:
                # if seen[curIdx] == 1, it meas this node is being visiting and here is a cycle
                return False
        # mark the curidx as 'visiting'
        seen[curIdx] = 1

        children = graph[curIdx]
        for child in children:
            if self.dfs(graph, child, seen) == False:
                return False
        # mark the curidx as 'visited'
        seen[curIdx] = 2
        return True


print('-----')
print(Solution().canFinish(2, [[1, 0]]))
print(Solution().canFinish(2, [[0, 1], [1, 0]]))
print(Solution().canFinish(
    6, [[4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]]))
print(Solution().canFinish(
    6, [[4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3], [3, 5]]))
