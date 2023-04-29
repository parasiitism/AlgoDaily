"""
    Learned from others
    - add at most 2 edges, it means there are at most 5 cases
    
    cases:
    - all even
        - True, don't need to add any edge
    - 1 edge
        - impossible
    - 2 egdes
        - if 2 nodes are not connected, connect them
        - else find a random even nodes and connect a and b with it
    - 3 edges
        - impossible
    - 4 edges
        build 2 edges for each pair if possible 
        - (a, b) and (c,d)
        - (a, c) and (b,d)
        - (a, d) and (b,c)

    ref:
    - https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/solutions/2923720/python-stright-forward-with-explanation/
    - https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/solutions/2927397/python-3-14-lines-w-analysis-t-m-1647-ms-55-9-mb-100-100/

    Time    O(E+V)
    Space   O(V)
"""


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:

        # G = defaultdict(set) # we cannot use hashtable because some nodes dont even have an edge
        G = [set() for _ in range(n)]

        for u, v in edges:
            G[u-1].add(v-1)
            G[v-1].add(u-1)
        odd_nodes = []
        for node in range(n):
            if len(G[node]) % 2 == 1:
                odd_nodes.append(node)

        def isNotConnected(u, v):
            return u not in G[v]

        if len(odd_nodes) == 0:
            return True
        elif len(odd_nodes) == 2:
            a, b = odd_nodes
            if isNotConnected(a, b):
                return True
            for any_node in range(n):
                if isNotConnected(any_node, a) and isNotConnected(any_node, b):
                    return True
            return False
        elif len(odd_nodes) == 4:
            a, b, c, d = odd_nodes
            if (isNotConnected(a, b) and isNotConnected(c, d)) or \
                (isNotConnected(a, c) and isNotConnected(b, d)) or \
                    (isNotConnected(a, d) and isNotConnected(b, c)):
                return True

        return False  # if # of odd nodes = 1,3,5...etc
