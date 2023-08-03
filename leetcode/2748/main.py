"""
    1st: math

    Time    O(NM) N: nums length, M: average length of a number
    Space   O(N)
"""


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ctr = Counter()
        res = 0
        for i in range(n):
            x = nums[i]
            for j in range(1, 11):
                if math.gcd(j, x % 10) == 1:
                    res += ctr[j]
            first_char = int(str(x)[0])
            ctr[first_char] += 1
        return res
