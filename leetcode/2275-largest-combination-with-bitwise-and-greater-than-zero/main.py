class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for i in range(32):
            cur = 0
            for x in candidates:
                if (x >> i) & 1 == 1:
                    cur += 1
            res = max(res, cur)
        return res
