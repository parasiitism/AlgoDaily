"""
    1st: brute force
    - try all possibilities

    Time    O(nPr)
    Space   O(nPr)
    62 ms, faster than 20.00%
"""


class Solution:
    def minimumSum(self, num: int) -> int:
        s = str(num)
        nums = [0, 1, 2, 3]
        self.combos = []
        self.dfs([], nums, 4)
        res = 2**32
        for i, j, k, l in self.combos:
            a = int(s[i] + s[j])
            b = int(s[k] + s[l])
            res = min(res, a + b)
        return res

    def dfs(self, chosen, nums, k):
        if len(chosen) == k:
            self.combos.append(chosen)
            return
        for i in range(len(nums)):
            x = nums[i]
            self.dfs(chosen + [x], nums[:i] + nums[i+1:], k)
