import heapq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int

        It can be solved by DFS, but the main purpose of this attempt is to understand Dijkstra's Algorithm
        - Time  O(NlogN) logN due to the heap
        - Space O(N) result dict
        116ms beats 61.11%
        27jan2019
        """
        # put times into a hashtable for lookup, time = (from, to, weight)
        timesMap = {}
        for time in times:
            key = time[0]
            if key in timesMap:
                timesMap[key].append(time)
            else:
                timesMap[key] = [time]

        # dijkstra's
        heap = [(0, K)]
        seen = {}
        while len(heap) > 0:
            weight, fromLoc = heapq.heappop(heap)

            if fromLoc in seen:
                continue
            seen[fromLoc] = weight

            if fromLoc in timesMap:
                candidates = timesMap[fromLoc]
                for can in candidates:
                    heapq.heappush(heap, (weight+can[2], can[1]))

        # the max travel time is the result
        maximum = 0
        for i in range(1, N+1):
            if i not in seen:
                return -1
            if seen[i] > maximum:
                maximum = seen[i]
        return maximum


a = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
print(Solution().networkDelayTime(a, 4, 2))  # 2

a = [[2, 1, 1], [2, 3, 1], [1, 4, 3], [2, 4, 7]]
print(Solution().networkDelayTime(a, 4, 2))  # 4

a = [[1, 2, 3], [3, 4, 5]]
print(Solution().networkDelayTime(a, 4, 1))  # -1
