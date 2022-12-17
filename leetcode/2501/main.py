"""
    Sort + hashtable
    1. Sort the array (descending)
    2. Iterate the sorted array and for each idx
        - See if we have seen arr[i]^2 in the past; If yes, accumulate the length at this index
    3. Result is the largest value in the "seen" hashtable

    Time    O(NlogN + N)
    Space   O(N)
"""


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: -x)
        seen = defaultdict(int)
        for x in nums:
            y = x*x
            seen[x] = seen[y] + 1
        res = max(seen.values())
        if res == 1:
            return -1
        return res
