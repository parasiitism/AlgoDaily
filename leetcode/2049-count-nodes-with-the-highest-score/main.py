from collections import *

"""
    1st: DFS
    - learned from others

    ref:
    - https://leetcode.com/problems/count-nodes-with-the-highest-score/discuss/1537603/Python-3-or-Graph-DFS-Post-order-Traversal-O(N)-or-Explanation

    Time    O(N)
    Space   O(N)
    2276 ms, faster than 9.09%
"""


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        g = defaultdict(list)

        for node, parent in enumerate(parents):     # build a graph
            g[parent].append(node)

        n = len(parents)                            # total number of nodes
        d = Counter()

        def count_nodes(node):                      # number of children node + self
            product, total = 1, 0                   # p: product, s: sum

            for child in g[node]:
                cnt = count_nodes(child)            # get count for every child
                product *= cnt                      # take the product
                total += cnt                        # take the sum

            # times parent-branch (n - 1 - left - right)
            product *= max(1, n - 1 - total)
            # count the product to get the result
            d[product] += 1

            # return number of children node + 1 (self)
            return total + 1

        count_nodes(0)                           # starting from root (0)
        return d[max(d.keys())]
