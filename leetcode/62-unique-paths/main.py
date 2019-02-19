class Solution(object):
    def uniquePaths(self, m, n):
        """
        1st approach: brute force, bottom up recursively with memorizatin
        - intuitively go through all the path with i+1 OR j+1
        - count the path which reaches to the destination coordinate (n,m)
        - cache the count of the coordinates which we have calculated before
        - sum up all the coordinates' count

        Time    O(m*n) 0->m, 0->n. since we cache the intermediate coordinates, we dont have duplicate sets of i, j
        Space   O(m*n) depth of recursion calls
        24ms beats 46.68%
        """
        seen = {}
        return self.dfs(0, 0, m, n, seen)

    def dfs(self, i, j, m, n, seen):
        key = str(i)+","+str(j)
        if key in seen:
            return seen[key]
        if i + 1 == m and j + 1 == n:
            return 1
        elif i + 1 > m or j + 1 > n:
            return 0
        left = self.dfs(i+1, j, m, n, seen)
        right = self.dfs(i, j+1, m, n, seen)
        seen[key] = left + right
        return left + right


print(Solution().uniquePaths(-1, 1))
print(Solution().uniquePaths(0, 0))
print(Solution().uniquePaths(3, 2))
print(Solution().uniquePaths(7, 3))
print(Solution().uniquePaths(29, 45))
print(Solution().uniquePaths(100, 100))
