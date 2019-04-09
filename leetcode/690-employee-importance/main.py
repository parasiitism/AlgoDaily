"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

"""
    1st approach: iterative dfs + hashtable

    Time    O(n)
    Space   O(n)
    168 ms, faster than 71.01%
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        ht = {}
        for em in employees:
            ht[em.id] = em
        res = 0
        stack = [ht[id]]
        while len(stack) > 0:
            e = stack.pop()
            res += e.importance
            for subId in e.subordinates:
                stack.append(ht[subId])
        return res


"""
    2nd approach: recursive dfs + hashtable

    Time    O(n)
    Space   O(n)
    164 ms, faster than 82.38%
"""


class Solution(object):

    def __init__(self):
        self.res = 0

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        ht = {}
        for em in employees:
            ht[em.id] = em
        self.dfs(id, ht)
        return self.res

    def dfs(self, eId, ht):
        if eId not in ht:
            return
        em = ht[eId]
        self.res += em.importance
        for subId in em.subordinates:
            self.dfs(subId, ht)
