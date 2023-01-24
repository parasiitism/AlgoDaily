"""
    sliding window
    - at each index i, we calculate good arrays by subtracting non-arrays

    e.g.
    [3, 1, 4, 3, 2, 2, 4], k= 2
    
    It means e.g. when i = 6, j = 3
    <---------> good
                <------> non-good

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = Counter()
        count = 0
        res = 0
        j = 0
        for i in range(len(nums)):
            x = nums[i]
            count += freq[x]
            freq[x] += 1
            while count >= k:
                y = nums[j]
                freq[y] -= 1
                count -= freq[y]
                j += 1
            res += j
        return res
