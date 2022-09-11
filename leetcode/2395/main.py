"""
    hashtable
    - 2sum variation 

    Time    O(N)
    Space   O(N)
    66 ms, faster than 59.47%
"""


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(1, len(nums)):
            s = nums[i-1] + nums[i]
            if s in seen:
                return True
            seen.add(s)
        return False
