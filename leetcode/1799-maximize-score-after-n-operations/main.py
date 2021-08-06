"""
    1st: backtracking
    - it is correct but too slow, cannot cache because it is hard to do memorization

    LTE
"""


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        return self.dfs(nums, set(), 1)

    def dfs(self, nums, used, steps):
        n = len(nums)
        if steps * 2 > n:
            return 0
        res = 0
        for i in range(n):
            if i in used:
                continue
            used.add(i)

            for j in range(i+1, n):
                if j in used:
                    continue
                used.add(j)

                A = gcd(nums[i], nums[j]) * steps
                B = self.dfs(nums, used, steps + 1)
                res = max(res, A + B)

                used.remove(j)
            used.remove(i)
        return res


"""
    2nd: dynamic programming(recursion + hashtable)
    - try every possibility, cache the used patterns

    Time    O((N^2) * (2^N)) we try every possibility, and we do N^2 iteration in every recursive function
    Space   O(2^N)
    2420 ms, faster than 56.70%
"""


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        return self.dfs(tuple(nums), 1, {})

    def dfs(self, nums, steps, cache):
        n = len(nums)
        if n == 0:
            return 0
        key = (nums, steps)
        if key in cache:
            return cache[key]
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                remain = nums[:i] + nums[i+1:j] + nums[j+1:]
                A = steps * gcd(nums[i], nums[j])
                B = self.dfs(tuple(remain), steps+1, cache)
                res = max(res, A + B)
        cache[key] = res
        return res

    # slower than the built-in gcd function
    # def gcd(self, a, b):
    #     if b == 0:
    #         return a
    #     return self.gcd(b, a % b)
