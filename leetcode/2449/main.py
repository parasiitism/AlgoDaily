"""
    Sort + math
    
    - If simplify the Q: A[i] = A[i] + 1 AND A[j] = A[j] - 1
        - We can sort A and B, and accumulate the diffs at every index, sum(A[i] - B[i]), then the result is diffSum/2
    - Now with nums[i] = nums[i] +/- 2:
        - if an even number +/-2, then it will be still an even number
        - if an odd number +/-2, then it will be still an odd number
    - So we can just separate the the calculation of odds and evens

    Time    O(NlogN)
    Space   O(N)
    2250 ms, faster than 33.33%
"""


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums_odd = sorted([x for x in nums if x % 2 == 0])
        nums_even = sorted([x for x in nums if x % 2 == 1])
        target_odd = sorted([x for x in target if x % 2 == 0])
        target_even = sorted([x for x in target if x % 2 == 1])
        res = 0
        for x, y in zip(nums_odd, target_odd):
            res += abs(x - y)
        for x, y in zip(nums_even, target_even):
            res += abs(x - y)
        return res // 4
