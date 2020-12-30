from collections import defaultdict

"""
    1st: union find
    - get all the emails
    - map each email with a name
    - union find all the emails using the input
    - iterate the input again: map each of the email to its corresponding root

    Time    O(nlogn)
    Space   O(n)
    224 ms, faster than 46.85% 
"""


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        emailToName = {}
        for a in accounts:
            name = a[0]
            emails = a[1:]
            for email in emails:
                emailToName[email] = name
        # union
        uf = UnionFind(emailToName.keys())
        for a in accounts:
            emails = a[1:]
            first = emails[0]
            for i in range(1, len(emails)):
                uf.union(first, emails[i])
        # group the emails
        ht = defaultdict(list)
        for e in emailToName:
            root = uf.find(e)
            ht[root].append(e)
        # construct the result
        res = []
        for key in ht:
            name = emailToName[key]
            emails = sorted(ht[key])
            res.append([name] + emails)
        return res


class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.ids = {}
        self.caps = {}
        for vertex in vertices:
            self.ids[vertex] = vertex
            self.caps[vertex] = 1

    def find(self, key):
        # loop to find to ultimate root
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        # attach to the larger tree
        if self.caps[pId] < self.caps[qId]:
            self.ids[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.ids[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1


s = Solution()
r = s.accountsMerge([
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
])
print(r)
