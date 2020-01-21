import sys
from typing import List
from collections import defaultdict

"""
    1st: brute force recursion
    Time    O(2^N)
    Space   O(2^N)
    TLE     62 / 102
"""
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        self.ht = defaultdict(int)
        return self.dfs(A, B, 0)

    def dfs(self, A: List[int], B: List[int], i: int) -> int:
        if i == len(A):
            return 0

        orig = sys.maxsize
        if i == 0 or (A[i-1] < A[i] and B[i-1] < B[i]):
            orig = self.dfs(A, B, i+1)

        flip = sys.maxsize
        newA = A[:i] + [B[i]] + A[i+1:]
        newB = B[:i] + [A[i]] + B[i+1:]
        if i == 0 or (newA[i-1] < newA[i] and newB[i-1] < newB[i]):
            flip = self.dfs(newA, newB, i+1) + 1
        
        res = min(orig, flip)
        return res


s = Solution()

# 1
a = [1, 3, 5, 4]
b = [1, 2, 3, 7]
print(s.minSwap(a, b))

# 1
a = [1, 2, 5, 4]
b = [1, 3, 3, 7]
print(s.minSwap(a, b))

# 1
a = [0, 3, 5, 8, 9]
b = [2, 1, 4, 6, 9]
print(s.minSwap(a, b))

# 1
a = [0, 4, 4, 5, 9]
b = [0, 1, 6, 8, 10]
print(s.minSwap(a, b))

# 1
a = [3, 3, 8, 9, 10]
b = [1, 7, 4, 6, 8]
print(s.minSwap(a, b))

# 1
a = [0, 4, 4, 5, 9]
b = [0, 1, 6, 8, 10]
print(s.minSwap(a, b))

# 1
a = [4, 4, 5]
b = [1, 6, 8]
print(s.minSwap(a, b))


a = [4,10,13,14,17,19,21,24,26,27,28,29,34,37,38,42,44,46,48,51,52,53,54,57,58,59,64,65,66,67,71,73,75,76,80,81,82,83,86,88,89,90,95,97,98,99,101,105,106,108,109,110,111,112,115,119,121,122,123,124,125,126,127,128,129,130,131,133,136,138,143,145,147,149,150,153,158,160,163,164,165,167,168,169,172,173,174,176,178,179,183,184,186,188,189,192,193,194,198,200]
b = [0,1,3,5,6,7,11,13,15,16,17,21,37,39,41,42,43,45,47,50,53,55,56,57,64,66,67,68,69,70,71,72,74,75,76,77,79,80,87,88,89,95,96,97,98,100,101,105,106,107,108,112,113,115,116,118,119,122,124,125,126,127,128,131,135,136,137,138,139,140,144,145,148,150,151,154,159,160,161,162,163,167,168,170,171,174,176,178,179,180,181,185,187,189,190,191,192,198,199,200]
# print(s.minSwap(a, b))

print("-----")

"""
    2nd: dynamic programming, learned from others
    - similar to lc122
    - use 2 arrays, fixed and swapped, to record the minimum number of swaps along the way from index 0 to index i
    - update the arrays at every index where if we swap at i-1 or/and swap at i
    - i think its a HARD question

    ref:
    - https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/119879/C%2B%2BJavaPython-DP-O(N)-Solution

    Time    O(N)
    Space   O(N)
    80 ms, faster than 98.29%
"""
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        fixed, swapped = N * [sys.maxsize], N * [sys.maxsize]
        fixed[0], swapped[0] = 0, 1
        for i in range(1, N):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                # don't swap at (i-1) and don't swap at i
                fixed[i] = fixed[i - 1]
                # swap at both (i-1) and swap at i
                swapped[i] = swapped[i - 1] + 1
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                # swap at (i-1) and do not swap at i
                fixed[i] = min(fixed[i], swapped[i - 1])
                # do not swap at (i-1) and swap at i
                swapped[i] = min(swapped[i], fixed[i - 1] + 1)
        return min(swapped[-1], fixed[-1])


s = Solution()

# 1
a = [1, 3, 5, 4]
b = [1, 2, 3, 7]
print(s.minSwap(a, b))

# 1
a = [1, 2, 5, 4]
b = [1, 3, 3, 7]
print(s.minSwap(a, b))

# 1
a = [0, 3, 5, 8, 9]
b = [2, 1, 4, 6, 9]
print(s.minSwap(a, b))

# 1
a = [0, 4, 4, 5, 9]
b = [0, 1, 6, 8, 10]
print(s.minSwap(a, b))

# 1
a = [3, 3, 8, 9, 10]
b = [1, 7, 4, 6, 8]
print(s.minSwap(a, b))

# 1
a = [0, 4, 4, 5, 9]
b = [0, 1, 6, 8, 10]
print(s.minSwap(a, b))

# 1
a = [4, 4, 5]
b = [1, 6, 8]
print(s.minSwap(a, b))


a = [4,10,13,14,17,19,21,24,26,27,28,29,34,37,38,42,44,46,48,51,52,53,54,57,58,59,64,65,66,67,71,73,75,76,80,81,82,83,86,88,89,90,95,97,98,99,101,105,106,108,109,110,111,112,115,119,121,122,123,124,125,126,127,128,129,130,131,133,136,138,143,145,147,149,150,153,158,160,163,164,165,167,168,169,172,173,174,176,178,179,183,184,186,188,189,192,193,194,198,200]
b = [0,1,3,5,6,7,11,13,15,16,17,21,37,39,41,42,43,45,47,50,53,55,56,57,64,66,67,68,69,70,71,72,74,75,76,77,79,80,87,88,89,95,96,97,98,100,101,105,106,107,108,112,113,115,116,118,119,122,124,125,126,127,128,131,135,136,137,138,139,140,144,145,148,150,151,154,159,160,161,162,163,167,168,170,171,174,176,178,179,180,181,185,187,189,190,191,192,198,199,200]
# print(s.minSwap(a, b))