"""
    1st: for each number, convert it to a string and check if the length is en even

    Time    O(NM)
    Space   O(1)
    44 ms, faster than 97.65%
"""


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            s = str(x)
            if len(s) % 2 == 0:
                res += 1
        return res
