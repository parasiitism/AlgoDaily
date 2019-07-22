"""
    learned from others: coloring problem
    - for any map, u can just use 4 colors to paint the map
    - in this case, the question said one region can only have at most 3 adjacent regions but we got 4 colors to choose
    , so actually i can just choose any one of the remaining colors 

    ref:
    - https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/291192/ChineseC%2B%2B-1042.
    - https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/290858/JavaC%2B%2BPython-Greedily-Paint

    Time    O(n)
    Space   O(n)
    388 ms, faster than 95.05%
"""


class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * N
        connections = [[] for i in range(N)]

        for x, y in paths:
            connections[x - 1].append(y - 1)
            connections[y - 1].append(x - 1)

        for i in range(N):
            connected = set()
            for to in connections[i]:
                connected.add(res[to])
            res[i] = ({1, 2, 3, 4} - connected).pop()
            # res[i] = ({1, 2, 3, 4} - {res[j] for j in connections[i]}).pop()
        return res


s = Solution()


a = 3
b = [[1, 2], [2, 3], [3, 1]]
print(s.gardenNoAdj(a, b))

a = 4
b = [[1, 2], [3, 4]]
print(s.gardenNoAdj(a, b))

a = 4
b = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
print(s.gardenNoAdj(a, b))
