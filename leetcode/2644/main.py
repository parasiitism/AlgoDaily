"""
    brute-force

    Time    O(NlogN + DN)
    Space   O(D)
"""


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors = sorted(list(set(divisors)))
        res_divisor = divisors[0]
        res_score = 0
        for i in range(len(divisors)):
            score = 0
            for x in nums:
                if x % divisors[i] == 0:
                    score += 1
            if score > res_score:
                res_score = score
                res_divisor = divisors[i]
        return res_divisor
