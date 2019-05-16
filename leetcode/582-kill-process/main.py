"""
    1st approach: bfs

    Time    O(n)
    Space   O(h)
    600 ms, faster than 22.46%
"""


class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        connections = {}
        for i in range(len(ppid)):
            if ppid[i] not in connections:
                connections[ppid[i]] = [pid[i]]
            else:
                connections[ppid[i]].append(pid[i])
        q = [kill]
        res = []
        while len(q) > 0:
            head = q.pop(0)
            res.append(head)
            if head in connections:
                children = connections[head]
                for child in children:
                    q.append(child)
        return res


"""
    2nd approach: recursive dfs

    Time    O(n)
    Space   O(h)
    440 ms, faster than 37.72%
"""


class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        connections = {}
        for i in range(len(ppid)):
            if ppid[i] not in connections:
                connections[ppid[i]] = [pid[i]]
            else:
                connections[ppid[i]].append(pid[i])

        res = []

        def dfs(node):
            res.append(node)
            if node in connections:
                children = connections[node]
                for child in children:
                    dfs(child)
        dfs(kill)

        return res
