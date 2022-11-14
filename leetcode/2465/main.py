"""
    2 pointers

    Time    O(N)
    Space   O(N/2)
    61 ms, faster than 25.00%
"""
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        hs = set()
        while i < j:
            avg = (nums[i] + nums[j]) / 2.0
            hs.add(avg)
            i += 1
            j -= 1
        return len(hs)
