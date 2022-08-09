"""
    1st: hashtable
    - transform the formula
        j - i != nums[j] - nums[i]
        nums[i] - i != nums[j] - j

    Time    O(N)
    Space   O(N)
    1556 ms, faster than 33.33%
"""


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        seen = defaultdict(int)
        res = 0
        for i in range(n):
            target = nums[i] - i
            occurence = seen[target]
            res += i - occurence
            seen[target] += 1
        return res
