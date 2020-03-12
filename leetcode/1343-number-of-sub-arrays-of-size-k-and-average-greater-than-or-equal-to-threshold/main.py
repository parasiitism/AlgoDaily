from typing import List

"""
    1st: window sum
    Time    O(N)
    Space   O(1)
    708 ms, faster than 31.66%
"""


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        windowSum = 0
        for i in range(len(arr)):
            if i < k:
                windowSum += arr[i]
                if i == k - 1 and windowSum / (k*1.0) >= threshold:
                    res += 1
            else:
                windowSum -= arr[i-k]
                windowSum += arr[i]
                if windowSum / (k*1.0) >= threshold:
                    res += 1
        return res
