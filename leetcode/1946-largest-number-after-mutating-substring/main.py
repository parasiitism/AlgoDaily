"""
    1st: greedy
    - the description is somewhate confusing
    - basically it just means if we can replace digits within a continous portion to make the whole string largest

    Time    O(N)
    Space   O(N)
    676 ms, faster than 22.78%
"""


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        N = len(num)
        mutated = False
        nums = []
        for i in range(N):
            nums.append(int(num[i]))
        for i in range(N):
            d = nums[i]
            nums[i] = max(d, change[d])
            if change[d] < d and mutated:
                break
            mutated = mutated or change[d] > d
        return "".join(map(str, nums))
