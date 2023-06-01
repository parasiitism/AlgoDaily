from sortedcontainers import SortedList

"""
    sliding window + sort container

    Time    O(NlogN)
    Space   O(N)
"""


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        sl = SortedList()
        for i in range(n):
            cur = nums[i]
            sl.add(cur)
            if i-k >= 0:
                left = nums[i-k]
                sl.remove(left)
            if i-k+1 >= 0:
                if x-1 >= 0 and sl[x-1] < 0:
                    xth = sl[x-1]
                    res.append(xth)
                else:
                    res.append(0)
        return res
