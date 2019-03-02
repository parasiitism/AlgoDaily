class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]] e.g. [[to1, from1], [to2, from2],...]
        :rtype: List[int]

        2nd appraoch: Topological Ordering in BFS

        1. create a list to save to children for each node
        2. for each node, put the children in
            e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
            children list = [[], [0], [3], [], [3], [2,4,1]]
        3. count the indegree for each node(indegree = the number of incoming edges)
        4. put the nodes with 0 indegree into a queue
        5. if the queue is not empty, append the dequeued node to the result and in the same time decrement it's children's indegree
        6  after decrement, if there are nodes which has 0 indegree, put them into the queue
        7. do 6) and 7) until the queue becomes empty
        8. need a 'cnt' to check if there is a cycle(for detail: see comment)

        Time    O(V+E)
        Space   O(V)
        32ms beats 100%
        """
        # prepare a list to save to children for each node
        connections = []
        indegrees = []
        for i in range(numCourses):
            connections.append([])
            indegrees.append(0)
        # iterate though the edges and put them into the corresponding node in the connections
        for prereq in prerequisites:
            prev, cur = prereq[1], prereq[0]
            connections[prev].append(cur)
            indegrees[cur] += 1

        # put the nodes which has no incoming edges
        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        # a count to check if the graph has a cycle
        # if there is a cycle, there will be a node's indegree never becomes 0
        # it means it will not be push to the queue therefore the the cnt will be inconsistent with the numCourses
        cnt = 0
        res = []
        while len(queue) > 0:
            head = queue.pop(0)
            res.append(head)
            cnt += 1
            children = connections[head]
            for child in children:
                # subtract 1 for all destinations which the current node points(prereq) to
                indegrees[child] -= 1
                # if indegree of that child is 0, out it to the queue
                if indegrees[child] == 0:
                    queue.append(child)

        if cnt == numCourses:
            return res
        return []


print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2]]))

print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2], [5, 3]]))


# node values are not limited to numbers
# 1->5 works
# a->b works too
class Solution(object):
    def findOrder(self, prerequisites):
        """
        :type prerequisites: List[List[int/string]] e.g. [[to1, from1], [to2, from2],...]
        :rtype: List[int/string]
        """
        # get all the nodes
        nodesSet = set()
        for src, dest in prerequisites:
            nodesSet.add(src)
            nodesSet.add(dest)
        nodes = list(nodesSet)
        # init all the indegrees
        indegrees = {}
        for node in nodes:
            indegrees[node] = 0
        # get all the connections/adjacents list
        connections = {}
        for src, dest in prerequisites:
            # construct adjacent list
            if src not in connections:
                connections[src] = [dest]
            else:
                connections[src].append(dest)
            # add indegree for each node
            indegrees[dest] += 1
        # get the nodes with 0 indegree
        queue = []
        for key in indegrees:
            if indegrees[key] == 0:
                queue.append(key)
        # dequeue node from the queue and put it into the result
        res = []
        while len(queue) > 0:
            dq = queue.pop(0)
            res.append(dq)
            if dq in connections:
                children = connections[dq]
                for child in children:
                    indegrees[child] -= 1
                    if indegrees[child] == 0:
                        queue.append(child)
        # return [] if there is a cycle
        for key in indegrees:
            if indegrees[key] > 0:
                return []
        return res


print(Solution().findOrder([
    ['A', 'C'], ['B', 'C'], ['C', 'E'], [
        'B', 'D'], ['E', 'F'], ['D', 'F'], ['F', 'G']
]))
