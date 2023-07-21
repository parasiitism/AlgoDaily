"""
    DFS + topo sort

    Learned from others
    - https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/solution/can-jia-hui-yi-de-zui-duo-yuan-gong-shu-u8e8u/
    - there 2 possibilites to make a meeting
        1. 2 nodes like each other + we add the longest follower chain for each of the 2nodes
        2. 3 >= nodes form a circle, then we cannot add any followers in the circle
    - see case1.png, case2.png
        
    Time    O(N)
    Space   O(N)
"""


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)

        # find the heads of a chain using topo-sort idea
        indegrees = n * [0]
        for i in range(n):
            j = favorite[i]
            indegrees[j] += 1

        # from every node, calculate the longest chain
        lengths = n * [1]
        visited = n * [False]

        q = []
        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)
        while len(q) > 0:
            u = q.pop(0)
            visited[u] = True
            v = favorite[u]
            lengths[v] = max(lengths[u]+1, lengths[v])
            indegrees[v] -= 1
            if indegrees[v] == 0:
                q.append(v)

        # For every node, calculate 2 possibilities
        twoNodesRing = 0
        moreNodesRing = 0
        for i in range(n):
            if visited[i]:
                continue
            j = favorite[i]
            if favorite[j] == i:
                # 2 nodes like each other
                twoNodesRing += lengths[i] + lengths[j]
                visited[i] = True
                visited[j] = True
            else:
                # ring that more than 2 nodes
                cnt = 0
                x = i
                while True:
                    cnt += 1
                    x = favorite[x]
                    visited[x] = True
                    if x == i:
                        break
                moreNodesRing = max(moreNodesRing, cnt)

        return max(twoNodesRing, moreNodesRing)
