"""
    1st: sliding window + hashtable
    - calculate the subarray sum for each sliding window
    - 1 trick: pow(x, y, mod)

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ctr = Counter()
        res, cur = 0, 0

        def update(x, val):
            nonlocal cur
            freq = ctr[x]
            if freq > 0:
                # cur -= x**freq
                # cur %= 10**9 + 7
                cur -= pow(x, freq, 10**9 + 7)
            freq = freq + val
            ctr[x] = freq
            if freq > 0:
                cur += x**freq
                cur %= 10**9 + 7
                # cur += pow(x, freq, 10**9 + 7)

        for i in range(n):
            a = nums[i]
            update(a, 1)
            if i - k >= 0:
                b = nums[i - k]
                update(b, -1)
            if i - k + 1 >= 0:
                res = max(res, cur)
        return res
