"""
    1st: math
    - there are 2 possibilities
        - if 1 is left of N, then the result is the steps to move 1 back the start + the steps to move N back to the end
        - if 1 is rught of N, the steps to move 1 back to start will shift N towards the end closer

    Time    O(N)
    Space   O(1) 
"""


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        one = -1
        last = -1
        for i in range(n):
            x = nums[i]
            if x == 1:
                one = i
            elif x == n:
                last = i
        if one < last:
            return one + n - last - 1
        return one + n - last - 2
