"""
    1st approach: zero sum subarray
    - this question is fucking similar to leetcode523, 525, 560, 930, 1124, 1171
    - learned from others: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/discuss/77807/Clean-python-solution-one-pass
    - the basic idea is to store the previous sum in a hashtable
        e.g. key: previous sum, value: index of the previous sum
    - if currentSum - target in the hastable, the result is currentIndex - hastable[previous sum]

    ref:
    - https://www.youtube.com/watch?v=hLcYp67wCcM

    Time O(n)
    Space O(n) hashtable
    36ms beats 100%
"""


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        res = 0
        pfs = 0
        ht = {}
        for i in range(len(nums)):
            pfs += nums[i]
            if pfs == k:
                res = i+1
            remain = pfs - k
            if remain in ht:
                res = max(res, i - ht[remain])
            if pfs not in ht:
                ht[pfs] = i
        return res


print(Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3))
print(Solution().maxSubArrayLen([-2, -1, 2, 1], 1))
print(Solution().maxSubArrayLen([-2, -1, 2, 1, 100], 100))
print(Solution().maxSubArrayLen([-2, -1, 2, 100, 1], 100))
print(Solution().maxSubArrayLen([-2, -1, 2, 1000], 99))

print("-----")

"""
    2nd: same logic but just shorter
"""
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ht = {0:-1}
        pfs = 0
        res = 0
        for i in range(len(nums)):
            pfs += nums[i]
            if pfs-k in ht:
                j = ht[pfs-k]
                res = max(res, i - j)
            if pfs not in ht: 
                ht[pfs] = i
        return res