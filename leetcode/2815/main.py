"""
    1st: brute-force

    Time    O(N^2)
    Space   O(1)
"""


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        for i in range(n):
            a = self.getMax(nums[i])
            for j in range(i+1, n):
                b = self.getMax(nums[j])
                if a == b:
                    res = max(res, nums[i] + nums[j])
        return res

    def getMax(self, N):
        res = 0
        while N > 0:
            d = N % 10
            res = max(res, d)
            N //= 10
        return res


"""
    2nd: hashtable

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        ht = {}
        for i in range(n):
            a = self.getMax(nums[i])
            if a in ht:
                res = max(res, nums[i] + ht[a])
            else:
                ht[a] = nums[i]

            ht[a] = max(ht[a], nums[i])
        return res

    def getMax(self, N):
        res = 0
        while N > 0:
            d = N % 10
            res = max(res, d)
            N //= 10
        return res
