from collections import *
from heapq import *

"""
    1st: dijkstra + dynamic programming

    Time    O(H + HlogND)
    Space   O(ND)
    7936 ms, faster than 5.56%
"""


class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        # adjacent list
        connections = defaultdict(list)
        # edge with cost { from: (to, cost), ... }
        for a, b, cost in highways:
            connections[a].append((b, cost))
            connections[b].append((a, cost))
        # dijkstra's
        # put (cost, node, discountUsed) into the heap
        minheap = [(0, 0, discounts)]
        best = defaultdict(dict)  # idx: {remainingDiscount: totalCost}
        while len(minheap) > 0:
            # pop the edge with min cost
            cost, node, remain = heappop(minheap)
            # if the cost < calculated cost of the node, update the node
            if remain in best[node] and cost >= best[node][remain]:
                continue
            best[node][remain] = cost
            # add the adjacent nodes to the pq for processing
            if node in connections:
                candidates = connections[node]
                for can in candidates:
                    if remain > 0:
                        heappush(minheap, (cost+can[1], can[0], remain))
                        heappush(minheap, (cost+can[1]//2, can[0], remain-1))
                    else:
                        heappush(minheap, (cost+can[1], can[0], 0))
        # print(best)
        finals = best[n-1].values()
        if len(finals) == 0:
            return -1
        return min(finals)
