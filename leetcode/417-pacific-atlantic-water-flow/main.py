"""
    1st approach: bfs

    LTE: works in golang but failed in python cos there is a much more faster method
"""

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                p, a = self.bfs(matrix, i, j, matrix[i][j])
                if p == True and a == True:
                    res.append([i, j])
        return res

    def bfs(self, matrix, x, y, height):

        m = []
        for k in range(len(matrix)):
            m.append(len(matrix[0]) * [False])

        p = False
        a = False
        q = [(x, y, height)]
        while len(q) > 0:
            i, j, h = q.pop(0)
            if i == -1 or j == -1:
                p = True
                continue
            if i == len(matrix) or j == len(matrix[0]):
                a = True
                continue
            if matrix[i][j] <= h:
                if m[i][j] == True:
                    continue
                m[i][j] = True
                q.append((i-1, j, matrix[i][j]))
                q.append((i+1, j, matrix[i][j]))
                q.append((i, j-1, matrix[i][j]))
                q.append((i, j+1, matrix[i][j]))
        return p, a


a = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(Solution().pacificAtlantic(a))

a = [
    [1, 2, 2, 3, 5],
    [3, 1, 1, 4, 4],
    [2, 1, 3, 3, 1],
    [6, 1, 9, 9, 9],
    [5, 1, 1, 1, 1],
    [5, 9, 9, 9, 9],
]
print(Solution().pacificAtlantic(a))

a = [[8,13,11,18,14,16,16,4,4,8,10,11,1,19,7],[2,9,15,16,14,5,8,15,9,5,14,6,10,15,5],[15,16,17,10,3,6,3,4,2,17,0,12,4,1,3],[13,6,13,15,15,16,4,10,7,4,19,19,4,9,13],[7,1,9,14,9,11,5,4,15,19,6,0,0,13,5],[9,9,15,12,15,5,1,1,18,1,2,16,15,18,9],[13,0,4,18,12,0,11,0,1,15,1,15,4,2,0],[11,13,12,16,9,18,6,8,18,1,5,12,17,13,5],[7,17,2,5,0,17,9,18,4,13,6,13,7,2,1],[2,3,9,0,19,6,6,15,14,4,8,1,19,5,9],[3,10,5,11,7,14,1,5,3,19,12,5,2,13,16],[0,8,10,18,17,5,5,8,2,11,5,16,4,9,14],[15,9,16,18,9,5,2,5,13,3,10,19,9,14,3],[12,11,16,1,10,12,6,18,6,6,18,10,9,5,2],[17,9,6,6,14,9,2,2,13,13,15,17,15,3,14],[18,14,12,6,18,16,4,10,19,5,6,8,9,1,6],]
print(Solution().pacificAtlantic(a))

print("---")

"""
    2nd approach: search from boundaries
    - search from 4 boundaries with dfs

    Time    O(5mn)
    Space   O()
    284 ms, faster than 34.05%
"""
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []

        p_visited = []
        for k in range(len(matrix)):
            p_visited.append(len(matrix[0]) * [False])
        a_visited = []
        for k in range(len(matrix)):
            a_visited.append(len(matrix[0]) * [False])
        
        
        for i in range(len(matrix)):
            # from left
            self.dfs(matrix, i, 0, matrix[i][0], p_visited)
            # from right
            self.dfs(matrix, i, len(matrix[0])-1, matrix[i][len(matrix[0])-1], a_visited)
        for j in range(len(matrix[0])):
            # from top
            self.dfs(matrix, 0, j, matrix[0][j], p_visited)
            # from bottom
            self.dfs(matrix, len(matrix)-1, j, matrix[len(matrix)-1][j], a_visited)
            
        result = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i,j])
        return result
                
                
    def dfs(self, matrix, i, j, height,visited):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            return
        if matrix[i][j] >= height:
            # we mark visited here becos we might stop other paths visting if we mark outside(too early)
            # we want TRUELY visiting
            if visited[i][j] == True:
                return
            visited[i][j] = True
            h = matrix[i][j]
            self.dfs(matrix, i-1, j, h, visited)
            self.dfs(matrix, i+1, j, h, visited)
            self.dfs(matrix, i, j-1, h, visited)
            self.dfs(matrix, i, j+1, h, visited)

a = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(Solution().pacificAtlantic(a))

a = [
    [1, 2, 2, 3, 5],
    [3, 1, 1, 4, 4],
    [2, 1, 3, 3, 1],
    [6, 1, 9, 9, 9],
    [5, 1, 1, 1, 1],
    [5, 9, 9, 9, 9],
]
print(Solution().pacificAtlantic(a))

a = [[8,13,11,18,14,16,16,4,4,8,10,11,1,19,7],[2,9,15,16,14,5,8,15,9,5,14,6,10,15,5],[15,16,17,10,3,6,3,4,2,17,0,12,4,1,3],[13,6,13,15,15,16,4,10,7,4,19,19,4,9,13],[7,1,9,14,9,11,5,4,15,19,6,0,0,13,5],[9,9,15,12,15,5,1,1,18,1,2,16,15,18,9],[13,0,4,18,12,0,11,0,1,15,1,15,4,2,0],[11,13,12,16,9,18,6,8,18,1,5,12,17,13,5],[7,17,2,5,0,17,9,18,4,13,6,13,7,2,1],[2,3,9,0,19,6,6,15,14,4,8,1,19,5,9],[3,10,5,11,7,14,1,5,3,19,12,5,2,13,16],[0,8,10,18,17,5,5,8,2,11,5,16,4,9,14],[15,9,16,18,9,5,2,5,13,3,10,19,9,14,3],[12,11,16,1,10,12,6,18,6,6,18,10,9,5,2],[17,9,6,6,14,9,2,2,13,13,15,17,15,3,14],[18,14,12,6,18,16,4,10,19,5,6,8,9,1,6],]
print(Solution().pacificAtlantic(a))