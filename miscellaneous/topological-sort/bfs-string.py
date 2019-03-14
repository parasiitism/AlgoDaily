# node values are not limited to numbers
# 1->5 works
# a->b works too


class Solution(object):
    def findOrder(self, prerequisites):
        """
        :type prerequisites: List[List[int/string]] e.g. [[to1, from1], [to2, from2],...]
        :rtype: List[int/string]

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
        # get all the nodes
        nodesSet = set()
        for src, dest in prerequisites:
            nodesSet.add(src)
            nodesSet.add(dest)
        nodes = list(nodesSet)
        # init adjacents and indegrees for all nodes
        connections = {}
        indegrees = {}
        for node in nodes:
            connections[node] = []
            indegrees[node] = 0
        # get all the adjacents list and indegree
        for src, dest in prerequisites:
            # add node to the adjacent list
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
            node = queue.pop(0)
            res.append(node)
            children = connections[node]
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
    ('A', 'C'),
    ('B', 'C'),
    ('C', 'E'),
    ('B', 'D'),
    ('E', 'F'),
    ('D', 'F'),
    ('F', 'G'),
]))
