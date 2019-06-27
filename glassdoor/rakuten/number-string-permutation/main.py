"""
    1st approach: permuation2
    - sort to avoid redundant selection
    - check leading digit to avoid leading zeros
"""


class Solution(object):

    def __init__(self):
        self.result = []

    def permuteUnique(self, s):
        nums = []
        for c in s:
            nums.append(c)
        nums = sorted(nums)
        self.dfs(nums, [])
        print(self.result)
        return len(self.result)

    def dfs(self, cands, chosen):
        if len(cands) == 0:
            if chosen[0] != '0':
                self.result.append(chosen)
        for i in range(len(cands)):
            if i == 0 or cands[i-1] != cands[i]:
                self.dfs(cands[:i] + cands[i+1:], chosen + [cands[i]])


print(Solution().permuteUnique("0"))
print(Solution().permuteUnique("123"))
print(Solution().permuteUnique("1213"))
print(Solution().permuteUnique("1000"))
print(Solution().permuteUnique("10010"))
