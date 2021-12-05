"""
    1st: brute force

    Time    O(N^3)
    Space   O(N^3)
    5408 ms, faster than 11.11%
"""


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res = set()
        for i in range(n):
            x = digits[i]
            for j in range(n):
                y = 10*x + digits[j]
                if i == j or y < 10:
                    continue
                for k in range(n):
                    z = 10*y + digits[k]
                    if i == k or j == k or z < 100:
                        continue
                    if z % 2 == 0:
                        res.add(z)
        return sorted(list(res))

#         self.cands = set()
#         self.dfs(0, digits)
#         res = list(self.cands)
#         return sorted(res)

#     def dfs(self, chosen, digits):
#         if chosen >= 100:
#             if chosen % 2 == 0:
#                 self.cands.add(chosen)
#             return
#         for i in range(len(digits)):
#             x = digits[i]
#             self.dfs(10*chosen+x, digits[:i] + digits[i+1:])
