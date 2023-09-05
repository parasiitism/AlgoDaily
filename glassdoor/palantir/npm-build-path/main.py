from collections import *


class Solution(object):
    def findOrder(self, n: int, prereqs: List[List[int]]) -> List[int]:
        G = {}
        indegrees = {}
        for i in range(n):
            G[i] = []
            indegrees[i] = 0

        for course, prereq in prereqs:
            G[prereq].append(course)
            indegrees[course] += 1

        q = deque()
        for course in indegrees:
            if indegrees[course] == 0:
                q.append(course)

        res = []
        while len(q) > 0:
            course = q.popleft()
            res.append(course)
            children = G[course]
            for child in children:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)
        if len(res) != n:
            return []
        return res


print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2]]))

print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2], [5, 3]]))

print(Solution().findOrder(
    1, []))
