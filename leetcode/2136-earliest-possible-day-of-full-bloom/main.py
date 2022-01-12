"""
    1st: sort + prefix sum
    - grow the tough-growing plants first
    - plant and grow all the plants and look for the maximum bloom day

    Time    O(NlogN)
    Space   O(N)
    1828 ms, faster than 100.00%
"""
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        nums = [(plantTime[i], growTime[i]) for i in range(n)]
        nums.sort(key=lambda x: -x[1])
        pfs = 0
        res = 0
        for i in range(n):
            p = nums[i][0]
            g = nums[i][1]
            pfs += p
            res = max(res, pfs + g)
        return res
