"""
    1st: hashset

    Time    O(N)
    Space   O(N)
    149 ms, faster than 18.18%
"""


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hs = set()
        for x in nums:
            if x in hs:
                hs.remove(x)
            else:
                hs.add(x)
        return len(hs) == 0
