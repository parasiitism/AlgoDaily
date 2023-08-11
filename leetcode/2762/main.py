from sortedcontainers import SortedList

"""
    2 pointers + SortedList
    - use the handy data structure SortedList in python so that we can always maintain a sorted list in O(logN) time
    - for every iteration, basically if sortedlist[tail] - sortedlist[head] > 2, we move forward to left pointer

    Time    O(NlogN)
    Space   O(N)
"""


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList()
        res = 0
        j = 0
        for i in range(n):
            sl.add(nums[i])
            while j <= i and sl[-1] - sl[0] > 2:
                sl.remove(nums[j])
                j += 1
            res += i - j + 1
        return res
