from sortedcontainers import SortedList

"""
    1st: sorted list to simulate self-balancing BST

    Time    O(2 * NlogN)
    Space   O(2 * N)
"""


class Solution:
    def minAbsoluteDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        forward = SortedList()
        forwaid_min = 2**32
        for i in range(k, n):
            prev = nums[i-k]
            cur = nums[i]
            forward.add(prev)
            j = forward.bisect_left(cur)
            if j < len(forward):
                diff = abs(cur - forward[j])
                forwaid_min = min(forwaid_min, diff)

        backward = SortedList()
        backward_min = 2**32
        for i in range(n-k-1, -1, -1):
            prev = nums[i+k]
            cur = nums[i]
            backward.add(prev)
            j = backward.bisect_left(cur)
            if j < len(backward):
                diff = abs(cur - backward[j])
                backward_min = min(backward_min, diff)

        return min(forwaid_min, backward_min)
