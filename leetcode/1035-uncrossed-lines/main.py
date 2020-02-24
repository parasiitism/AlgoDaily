from typing import List

"""
    1st: brute forece combinations
    Time    O(2^N)
    LTE
"""


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        self.res = 0
        self.dfs(A, B, 0, 0, 0)
        return self.res

    def dfs(self, A: List[int], B: List[int], aIdx: int, bIdx: int, count: int) -> None:
        self.res = max(self.res, count)
        if aIdx == len(A) or bIdx == len(B):
            return
        for i in range(bIdx, len(B)):
            if A[aIdx] == B[i]:
                self.dfs(A, B, aIdx+1, i+1, count + 1)
        self.dfs(A, B, aIdx+1, bIdx, count)


s = Solution()

a = [1, 4, 2]
b = [1, 2, 4]
print(s.maxUncrossedLines(a, b))

a = [2, 5, 1, 2, 5]
b = [10, 5, 2, 1, 5, 2]
print(s.maxUncrossedLines(a, b))

a = [1, 3, 7, 1, 7, 5]
b = [1, 9, 2, 5, 1]
print(s.maxUncrossedLines(a, b))

a = [1, 4, 3, 5, 6]
b = [1, 3, 5, 6, 4]
print(s.maxUncrossedLines(a, b))

print("==========")

"""
    2nd: dynamic programming
    - recursion + hashtable, bottom up
    - recursion to generate all possibilities
    - use a hashtable to cache the max number of feasible crosses from the end to avoid redundant calculations

    Time    O(N^2)
    Space   O(N^2)
    1164 ms, faster than 5.10%
"""


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        self.cache = {}
        return self.dfs(A, B, 0, 0)

    def dfs(self, A: List[int], B: List[int], aIdx: int, bIdx: int) -> int:
        if aIdx == len(A) or bIdx == len(B):
            return 0
        if (aIdx, bIdx) in self.cache:
            return self.cache[(aIdx, bIdx)]
        maxCount = 0
        for i in range(bIdx, len(B)):
            if A[aIdx] == B[i]:
                temp = self.dfs(A, B, aIdx+1, i+1) + 1
                maxCount = max(maxCount, temp)
        temp = self.dfs(A, B, aIdx+1, bIdx)
        maxCount = max(maxCount, temp)
        self.cache[(aIdx, bIdx)] = maxCount
        return maxCount


s = Solution()

a = [1, 4, 2]
b = [1, 2, 4]
print(s.maxUncrossedLines(a, b))

a = [2, 5, 1, 2, 5]
b = [10, 5, 2, 1, 5, 2]
print(s.maxUncrossedLines(a, b))

a = [1, 3, 7, 1, 7, 5]
b = [1, 9, 2, 5, 1]
print(s.maxUncrossedLines(a, b))

a = [1, 4, 3, 5, 6]
b = [1, 3, 5, 6, 4]
print(s.maxUncrossedLines(a, b))

a = [3, 1, 2, 1, 4, 1, 2, 2, 5, 3, 2, 1, 1, 4, 5, 2, 3, 2, 5, 5]
b = [2, 4, 1, 2, 3, 4, 2, 4, 5, 5, 1, 1, 2, 1, 1,
     1, 5, 4, 1, 4, 2, 1, 5, 4, 2, 3, 1, 5, 2, 1]
print(s.maxUncrossedLines(a, b))


print("==========")

"""
    3rd: similar as 2nd, but more concise
    - recursion + hashtable, bottom up
    - recursion to generate all possibilities
    - use a hashtable to cache the max number of feasible crosses from the end to avoid redundant calculations

    Time    O(N^2)
    Space   O(N^2)
    616 ms, faster than 6.46%
"""


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        self.cache = {}
        return self.dfs(A, B, 0, 0)

    def dfs(self, A: List[int], B: List[int], aIdx: int, bIdx: int) -> int:
        if aIdx == len(A) or bIdx == len(B):
            return 0
        if (aIdx, bIdx) in self.cache:
            return self.cache[(aIdx, bIdx)]
        if A[aIdx] == B[bIdx]:
            self.cache[(aIdx, bIdx)] = self.dfs(A, B, aIdx+1, bIdx+1) + 1
        else:
            x = self.dfs(A, B, aIdx+1, bIdx)
            y = self.dfs(A, B, aIdx, bIdx+1)
            self.cache[(aIdx, bIdx)] = max(x, y)
        return self.cache[(aIdx, bIdx)]


s = Solution()

a = [1, 4, 2]
b = [1, 2, 4]
print(s.maxUncrossedLines(a, b))

a = [2, 5, 1, 2, 5]
b = [10, 5, 2, 1, 5, 2]
print(s.maxUncrossedLines(a, b))

a = [1, 3, 7, 1, 7, 5]
b = [1, 9, 2, 5, 1]
print(s.maxUncrossedLines(a, b))

a = [1, 4, 3, 5, 6]
b = [1, 3, 5, 6, 4]
print(s.maxUncrossedLines(a, b))

a = [3, 1, 2, 1, 4, 1, 2, 2, 5, 3, 2, 1, 1, 4, 5, 2, 3, 2, 5, 5]
b = [2, 4, 1, 2, 3, 4, 2, 4, 5, 5, 1, 1, 2, 1, 1,
     1, 5, 4, 1, 4, 2, 1, 5, 4, 2, 3, 1, 5, 2, 1]
print(s.maxUncrossedLines(a, b))


print("==========")
