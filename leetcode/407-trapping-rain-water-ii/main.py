class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        forward = self.createZeroArray(len(heightMap), len(heightMap[0]))
        for i in range(len(heightMap)):
            maxH = 0
            for j in range(len(heightMap[0])):
                forward[i][j] = maxH
                maxH = max(maxH, heightMap[i][j])

        backward = self.createZeroArray(len(heightMap), len(heightMap[0]))
        for i in range(len(heightMap)):
            maxH = 0
            for j in range(len(heightMap[0])-1, -1, -1):
                backward[i][j] = maxH
                maxH = max(maxH, heightMap[i][j])

        downward = self.createZeroArray(len(heightMap), len(heightMap[0]))
        for j in range(len(heightMap[0])):
            maxH = 0
            for i in range(len(heightMap)):
                downward[i][j] = maxH
                maxH = max(maxH, heightMap[i][j])

        upward = self.createZeroArray(len(heightMap), len(heightMap[0]))
        for j in range(len(heightMap[0])):
            maxH = 0
            for i in range(len(heightMap)-1, -1, -1):
                upward[i][j] = maxH
                maxH = max(maxH, heightMap[i][j])

        res = 0

        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                f = forward[i][j]
                b = backward[i][j]
                d = downward[i][j]
                u = upward[i][j]
                m = min(f, min(b, min(d, u)))
                if m > heightMap[i][j]:
                    res += m - heightMap[i][j]

        return res

    def createZeroArray(self, r, c):
        res = []
        for i in range(r):
            res.append(c*[0])
        return res


a = [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1],
]
print(Solution().trapRainWater(a))
