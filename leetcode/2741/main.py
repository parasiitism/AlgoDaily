"""
    1st: brute-force Permutation: lc46 variation

    Time    O(N! * NlogD) because for big numbers we need logD to calculate if A and B are divisible
    Space   O(N!)

    TLE     529 / 587 testcases passed
"""


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        self.res = 0
        self.dfs([], nums)
        return self.res

    def dfs(self, chosen, cands):
        if len(cands) == 0:
            # print(chosen)
            self.res += 1
        for i in range(len(cands)):
            x = cands[i]
            if len(chosen) == 0:
                self.dfs(chosen + [x], cands[:i] + cands[i+1:])
            else:
                if chosen[-1] % x == 0 or x % chosen[-1] == 0:
                    self.dfs(chosen + [x], cands[:i] + cands[i+1:])


"""
    2nd Permutation + cache

    Time    O(N^2 + N*N!)
    Space   O(N!)

    TLE     529 / 587 testcases passed
"""


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        self.res = 0
        cache = {}
        for i in range(n):
            for j in range(i+1, n):
                a, b = nums[i], nums[j]
                cache[(a, b)] = a % b
                cache[(b, a)] = b % a

        self.dfs([], nums, cache)
        return self.res

    def dfs(self, chosen, cands, cache):
        if len(cands) == 0:
            # print(chosen)
            self.res += 1
        for i in range(len(cands)):
            x = cands[i]
            if len(chosen) == 0:
                self.dfs(chosen + [x], cands[:i] + cands[i+1:], cache)
            else:
                y = chosen[-1]
                if cache[(x, y)] == 0 or cache[(y, x)] == 0:
                    self.dfs(chosen + [x], cands[:i] + cands[i+1:], cache)


"""
    3rd: permutation + DP
    - imagine we have [3,6,9,12,15]
        - if we have [3,6,9] and [6,3,9], 
            let's say that we already calculated that the suffixes +[12,15] or +[15,12] can are special,
            we don't need to calculate again. 
            We can just use the key = (chosen[-1], suffix) as a key in hash the result to avoid redundant calculation
        
    Time    O(N * 2^N)
    Space   O(N * 2^N)
"""


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        used = len(nums) * [0]
        return self.dfs([], nums, used, {})

    def dfs(self, chosen, nums, used, cache):
        n = len(nums)
        if len(chosen) == n:
            return 1

        a, b = -1, tuple(used)
        if len(chosen) > 0:
            a = chosen[-1]
        key = tuple([a, b])
        if key in cache:
            return cache[key]

        res = 0
        for i in range(n):
            if used[i] == 1:
                continue
            used[i] = 1

            x = nums[i]
            if len(chosen) == 0:
                res += self.dfs(chosen + [x], nums, used, cache)
            else:
                if chosen[-1] % x == 0 or x % chosen[-1] == 0:
                    res += self.dfs(chosen + [x], nums, used, cache)

            used[i] = 0

        res %= 10**9+7
        cache[key] = res
        return res
