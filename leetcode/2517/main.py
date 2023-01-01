"""
    sort + binary

    Time    O(N log10^9)
    Space   O(1)
"""


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        # skip the numbers if price[i] - prev < mid, the goal is to find >= k numbers which match such condition
        def check(mid):
            prev = price[0]
            count = 1
            i = 1
            while count < k and i < len(price):
                if price[i] - prev >= mid:
                    prev = price[i]
                    count += 1
                i += 1
            return count == k

        left = 0
        right = 10**9
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1
