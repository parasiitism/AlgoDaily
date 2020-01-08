from collections import defaultdict

"""
    1st: recursion
    - use hashtable to find out the connections between the nodes
    - find the root(s)
    - for each root, find the lowest common ancestor using recursion

    Time    O(N)
    Space   O(N)
    260 ms, faster than 11.66%
"""


class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        self.connections = defaultdict(list)
        indegrees = defaultdict(int)
        for i in range(len(regions)):
            parent = regions[i][0]
            if parent not in indegrees:
                indegrees[parent] = 0
            for j in range(1, len(regions[i])):
                self.connections[parent].append(regions[i][j])
                indegrees[regions[i][j]] += 1

        roots = []
        for key in indegrees:
            if indegrees[key] == 0:
                roots.append(key)

        for root in roots:
            temp = self.findLCA(root, region1, region2)
            if temp != None:
                return temp

        return None

    def findLCA(self, root, a, b):
        if root == a or root == b:
            return root
        arr = []
        for node in self.connections[root]:
            temp = self.findLCA(node, a, b)
            if temp != None:
                arr.append(temp)
        if len(arr) == 2:
            return root
        elif len(arr) == 1:
            return arr[0]
        return None


s = Solution()

a = [["Earth", "North America", "South America"],
     ["North America", "United States", "Canada"],
     ["United States", "New York", "Boston"],
     ["Canada", "Ontario", "Quebec"],
     ["South America", "Brazil"]]
b = "Quebec"
c = "New York"

print(s.findSmallestRegion(a, b, c))
