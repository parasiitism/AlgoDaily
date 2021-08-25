"""
    1st: hashtable
    - use built-in bin functions
        - int(x, 2)
        - format(i, '0nb')
        to interchange binary strings and integers
    
    Time    O(N)
    Space   O(N)
    28 ms, faster than 71.43%
"""


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set()
        n = len(nums[0])
        for x in nums:
            num = int(x, 2)
            seen.add(num)
        for i in range(0, 2**n):
            if i not in seen:
                return format(i, '0'+str(n)+'b')
