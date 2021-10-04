"""
    1st: brute force

    Time    O(N^2)
    Space   O(1)
    76 ms, faster than 100.00%
"""


from collections import *


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                temp = nums[i] + nums[j]
                if temp == target:
                    res += 1
        return res


"""
    2nd: hashtable

    Time    O(N)
    Space   O(N)
    40 ms, faster than 100.00%
"""


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        cache = defaultdict(list)
        for i in range(n):
            x = nums[i]
            cache[x].append(i)
        res = 0
        for i in range(n):
            x = nums[i]
            a = target[:len(x)]
            b = target[len(x):]
            if a == x and b in cache:
                indices = cache[b]
                if i in indices:
                    res += len(indices) - 1
                else:
                    res += len(indices)
        return res
