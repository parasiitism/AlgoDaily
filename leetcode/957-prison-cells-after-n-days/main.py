"""
    1st: observation

    Time    O(14*8) -> O(1)
    Space   O(8)
    24 ms, faster than 100.00%
"""


class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        # after observation, i found out that the cells pattern repeat for every 15 iterations
        N %= 14
        if N == 0:
            N = 14
        # logic here
        newCells = [-1] + cells + [-1]
        for _ in range(N):
            clone = newCells[:]
            for j in range(1, len(clone)-1):
                if clone[j-1] == clone[j+1]:
                    newCells[j] = 1
                else:
                    newCells[j] = 0
        return newCells[1:-1]


a = [0, 1, 0, 1, 1, 0, 0, 1]
print(Solution().prisonAfterNDays(a, 0))
print(Solution().prisonAfterNDays(a, 1))
print(Solution().prisonAfterNDays(a, 2))
print(Solution().prisonAfterNDays(a, 3))
print(Solution().prisonAfterNDays(a, 4))
print("-----")
print(Solution().prisonAfterNDays(a, 5))
print(Solution().prisonAfterNDays(a, 6))
print(Solution().prisonAfterNDays(a, 7))
print(Solution().prisonAfterNDays(a, 8))
print(Solution().prisonAfterNDays(a, 9))
print("-----")
print(Solution().prisonAfterNDays(a, 10))
print(Solution().prisonAfterNDays(a, 11))
print(Solution().prisonAfterNDays(a, 12))
print(Solution().prisonAfterNDays(a, 13))
print(Solution().prisonAfterNDays(a, 14))
print("-----")
print(Solution().prisonAfterNDays(a, 15))
print(Solution().prisonAfterNDays(a, 16))
print(Solution().prisonAfterNDays(a, 17))
print(Solution().prisonAfterNDays(a, 18))
print(Solution().prisonAfterNDays(a, 19))
