"""
    binary search

    Time    O(NlogN)
    Space   O(N)
    2467 ms, faster than 25.00%
"""


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        n = len(tiles)
        tiles.sort()
        res = 0
        pfs = 0
        pfss = []
        for i in range(n):
            pfs += tiles[i][1] - tiles[i][0] + 1
            pfss.append(pfs)
        for i in range(n):
            s = tiles[i][0]
            j = self.upperBsearch(tiles, s+carpetLen-1)

            # fully covered
            covered = pfss[j-1] - (pfss[i-1] if i > 0 else 0)

            # partially covered
            if 0 < j < n and s+carpetLen-1 > tiles[j][0]:
                covered += s+carpetLen - tiles[j][0]

            res = max(res, covered)
        return res

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid][1]:
                left = mid + 1
            else:
                right = mid
        return right
