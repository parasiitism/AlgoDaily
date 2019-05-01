import heapq

"""
    1st approach: brute force, reuse lc263

    Time    O(nlogn)
    Space   O(n)
    LTE
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        res = [1]
        cur = 2
        while len(res) < n:
            if self.isUgly(cur):
                res.append(cur)
            cur += 1
        return res[-1]

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return 0
        while num % 2 == 0:
            num /= 2
        if num == 1:
            return True

        while num % 3 == 0:
            num /= 3
        if num == 1:
            return True

        while num % 5 == 0:
            num /= 5
        if num == 1:
            return True

        return False


print(Solution().nthUglyNumber(1))
print(Solution().nthUglyNumber(2))
print(Solution().nthUglyNumber(10))
# print(Solution().nthUglyNumber(500))
print("-----")

"""
    2nd approach: recursion + memorization (dynamic programming)

    Time    O(n) n=2^31 becos i dont know how big the number is supposed to be at the beginning
    Space   O(n)
    1620 ms, faster than 5.02%
"""


class Solution(object):

    def __init__(self):
        self.nums = [1]

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        heapq.heapify(self.nums)
        self.dfs(1, set())
        res = 1
        for i in range(n+1):
            res = heapq.heappop(self.nums)
        return res

    def dfs(self, num, seen):
        if num in seen:
            return
        seen.add(num)
        if num > 2**31:
            return
        heapq.heappush(self.nums, num)
        self.dfs(num*2, seen)
        self.dfs(num*3, seen)
        self.dfs(num*5, seen)


"""
1
2
12
2123366400
"""
print(Solution().nthUglyNumber(1))
print(Solution().nthUglyNumber(2))
print(Solution().nthUglyNumber(10))
print(Solution().nthUglyNumber(1690))
