import copy
import collections


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]

        1st approach: top-down dfs
        - for each node, put the remaining candidates to th next iteration

        Time    O(n^2)
        Space   O(h)
        TLE
        """
        ht = {}
        for src, dest in tickets:
            if src not in ht:
                ht[src] = [dest]
            else:
                ht[src].append(dest)
        for key in ht:
            ht[key] = sorted(ht[key], reverse=True)

        res = []
        stack = [('JFK', [], ht)]
        while len(stack) > 0:
            cur, path, hm = stack.pop()
            newPath = path + [cur]
            if len(hm) == 0:
                return newPath
            if cur not in hm:
                continue
            cands = hm[cur]
            for i in range(len(cands)):
                cand = cands[i]
                newCands = cands[:]
                newCands.pop(i)
                newHm = copy.deepcopy(hm)
                newHm[cur] = newCands
                if len(newHm[cur]) == 0:
                    del newHm[cur]
                stack.append((cand, newPath, newHm))
        return res

"""
    2nd approach: sort + post order traversal
    - learned from others
    - reverse the post order traversal of the nodes is the result 

    ref:
    - https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
    - https://www.youtube.com/watch?v=4udFSOWQpdg

    Time    O(ElogE)
    Space   O(E)
    68 ms, faster than 51.01% 
"""
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a, b in tickets:
            targets[a].append(b)
        for key in targets:
            targets[key] = sorted(targets[key], reverse=True)
        res = []

        def postorder(airport):
            while len(targets[airport]) > 0:
                postorder(targets[airport].pop())
            res.insert(0, airport)
        postorder('JFK')
        return res


# ["JFK", "MUC", "LHR", "SFO", "SJC"]
a = [
    ["MUC", "LHR"],
    ["JFK", "MUC"],
    ["SFO", "SJC"],
    ["LHR", "SFO"],
]
print(Solution().findItinerary(a))

# ["JFK","ATL","JFK","SFO","ATL","SFO"]
a = [
    ["JFK", "SFO"],
    ["JFK", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "JFK"],
    ["ATL", "SFO"],
]
print(Solution().findItinerary(a))

# ["JFK","ATL","JFK","SFO","ATL","SFO"]
a = [
    ["JFK", "SFO"],
    ["JFK", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "JFK"],
]
print(Solution().findItinerary(a))

# ['JFK', 'NRT', 'JFK', 'KUL']
a = [
    ["JFK", "KUL"],
    ["JFK", "NRT"],
    ["NRT", "JFK"],
]
print(Solution().findItinerary(a))

a = [["ANU","AXA"],["AXA","EZE"],["TIA","ANU"],["JFK","BNE"],["TIA","CNS"],["JFK","EZE"],["AXA","ADL"],["AXA","JFK"],["EZE","AXA"],["ANU","BNE"],["BNE","ADL"],["CNS","AXA"],["CNS","JFK"],["JFK","ANU"],["ADL","EZE"],["CNS","JFK"],["TIA","EZE"],["ANU","CNS"],["ADL","BNE"],["JFK","AXA"],["BNE","AUA"],["TIA","CNS"],["ANU","AXA"],["AUA","ANU"],["EZE","CNS"],["TIA","CNS"],["AXA","CNS"],["AUA","JFK"],["BNE","ADL"],["EZE","JFK"],["BNE","EZE"],["EZE","AXA"],["ANU","EZE"],["JFK","ANU"],["ADL","EZE"],["EZE","BNE"],["AXA","TIA"],["JFK","AUA"],["AXA","BNE"],["TIA","ANU"],["ADL","JFK"],["EZE","TIA"],["EZE","TIA"],["AXA","ADL"],["EZE","ANU"],["AUA","AXA"],["AXA","AUA"],["BNE","ANU"],["ADL","TIA"],["AUA","AXA"],["AUA","CNS"],["ANU","BNE"],["ADL","AUA"],["JFK","EZE"],["JFK","AXA"],["EZE","ANU"],["EZE","CNS"],["JFK","ANU"],["AXA","ANU"],["TIA","AUA"],["JFK","EZE"],["ANU","TIA"],["ANU","ADL"],["JFK","AUA"],["ANU","BNE"],["AUA","JFK"],["AXA","JFK"],["JFK","AUA"],["ADL","AXA"],["ANU","AUA"],["BNE","ADL"],["EZE","CNS"],["BNE","AXA"],["ADL","JFK"],["AXA","EZE"],["AXA","TIA"],["AXA","ADL"],["ADL","AUA"],["AXA","ANU"],["JFK","TIA"],["ANU","ADL"],["ANU","CNS"],["EZE","JFK"],["ADL","AUA"],["TIA","ANU"],["AXA","EZE"],["JFK","TIA"],["CNS","AXA"],["TIA","AXA"],["ANU","JFK"],["CNS","ADL"],["ANU","BNE"],["EZE","TIA"],["JFK","ANU"],["CNS","AUA"],["ANU","EZE"],["ANU","BNE"],["AXA","BNE"],["CNS","BNE"],["ADL","ANU"],["ADL","AUA"],["ANU","ADL"],["TIA","JFK"],["AUA","EZE"],["CNS","JFK"],["ADL","AUA"],["BNE","ANU"],["ANU","TIA"],["TIA","AXA"],["BNE","AUA"],["ANU","ADL"],["EZE","JFK"],["ADL","TIA"],["ADL","TIA"],["EZE","JFK"],["BNE","ADL"],["ANU","BNE"],["BNE","EZE"],["ADL","EZE"],["AXA","EZE"],["ADL","AXA"],["AXA","BNE"],["TIA","CNS"],["CNS","EZE"],["AUA","TIA"],["EZE","JFK"],["AXA","TIA"],["JFK","AXA"],["BNE","TIA"],["BNE","ANU"],["JFK","ANU"],["JFK","ADL"],["TIA","ANU"],["ANU","ADL"],["CNS","TIA"],["AUA","BNE"],["AXA","BNE"],["JFK","ANU"],["ANU","VIE"],["EZE","AXA"],["ANU","AUA"],["JFK","BNE"],["EZE","ADL"],["EZE","AXA"],["AUA","JFK"],["ADL","ANU"],["BNE","CNS"],["EZE","AXA"],["ADL","CNS"],["EZE","JFK"],["TIA","AXA"],["AUA","AXA"],["AUA","EZE"],["AUA","ADL"],["ANU","BNE"],["TIA","ADL"],["CNS","ANU"],["TIA","EZE"],["TIA","BNE"],["CNS","ANU"],["TIA","AUA"],["AUA","JFK"],["BNE","AUA"],["AXA","ANU"],["ANU","EZE"],["AXA","TIA"],["BNE","ADL"],["AXA","EZE"],["CNS","AXA"],["ADL","TIA"],["AUA","ADL"],["EZE","TIA"],["CNS","ADL"],["ADL","JFK"],["BNE","ANU"],["ADL","ANU"],["TIA","ADL"],["JFK","AUA"],["JFK","EZE"],["BNE","AXA"],["AUA","EZE"],["EZE","JFK"],["EZE","AUA"],["AXA","JFK"],["ADL","BNE"],["BNE","ADL"],["BNE","JFK"],["ANU","TIA"],["CNS","JFK"],["AXA","ADL"],["JFK","AXA"],["JFK","AUA"],["AXA","ANU"],["AUA","EZE"],["EZE","TIA"],["AUA","AXA"],["AUA","CNS"],["AXA","AUA"],["AUA","ANU"],["TIA","AXA"],["AUA","CNS"],["TIA","EZE"],["ANU","AXA"],["AXA","EZE"],["TIA","AXA"],["AUA","TIA"],["JFK","AUA"],["EZE","BNE"]]
print(Solution().findItinerary(a))

print("-------------------------")