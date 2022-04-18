"""
    1st: sort

    Time    O(N)
    Space   O(1)
    727 ms, faster than 100.00%
"""


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            prev = nums[i-1]
            curr = nums[i]
            if prev+1 != curr:
                return False
        return True
        


"""
    2nd: hashtable
    - put every element in a hashset
    - iterate from the min to see mim+i exists in the hashset
    
    Time    O(N)
    Space   O(N)
    732 ms, faster than 100.00% 
"""


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        n = len(nums)
        hs = set(nums)
        if len(hs) != n:
            return False
        mi = min(nums)
        for i in range(n):
            if mi+i not in hs:
                return False
        return True
