"""
    1st: math
    - an evens can only be sumed-up by evens, so result = [] for all odds  
    - try 2, 4, 6, 8...
    - mind the case that
    e.g. 14 = [2, 4, 6] + 2(remain due to redundancy)
    we can just add the 2 into last item in the result

    Time    O(sqrtN)
    Space   O(N)
    584 ms, faster than 66.67%
"""


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        even = 2
        res = []
        while finalSum - even >= 0:
            res.append(even)
            finalSum -= even
            even += 2
        res[-1] += finalSum
        return res
