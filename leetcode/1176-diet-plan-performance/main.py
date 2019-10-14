"""
    1st: sliding window

    Time    O(n)
    Space   O(1)
    196 ms, faster than 32.59%
"""


class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        res = 0
        total = 0
        for i in range(len(calories)):
            if i >= k:
                total -= calories[i-k]
            total += calories[i]

            if i+1 >= k:
                if total < lower:
                    res -= 1
                elif total > upper:
                    res += 1
        return res
