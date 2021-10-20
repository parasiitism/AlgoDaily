from collections import *

"""
    1st: BFS + math
    - learned from others
    - read the steps

    Time    O(N)
    Space   O(N)
    2384 ms, faster than 77.78% 
"""


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # build an adjency list
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # BFS to get the shortest route from every node to master.
        shortest = {}
        q = deque([(0, 0)])
        seen = set()
        while len(q) > 0:
            node, dist = q.popleft()
            if node in seen:
                continue
            seen.add(node)
            shortest[node] = dist

            for nb in g[node]:
                q.append((nb, dist+1))

        # calculate answer using shortest paths.
        res = 0
        for i in range(1, len(patience)):
            resendInterval = patience[i]

            # the server will stop sending requests after it's been sent to the master node and back.
            shutOffTime = shortest[i] * 2

            # shutOffTime-1 == Last second the server can send a re-request.
            lastSecond = shutOffTime-1

            # calculate the last time a packet is actually resent.
            lastResentTime = (lastSecond // resendInterval) * resendInterval

            # at the last resent time, the packet still must go through 2 more cycles to the master node and back.
            lastPacketTime = lastResentTime + shutOffTime

            res = max(lastPacketTime, res)

        # Add +1, the current answer is the last time the packet is recieved by the target server (still active).
        # We must return the first second the network is idle, therefore + 1
        return res + 1
