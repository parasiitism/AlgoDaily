from typing import List
from bisect import bisect_left, bisect_right

"""
    1st: recursion + linear search

    Time    O(2^D) ? each digit has 2 options -1 or +1
    Space   O(2^D)
    504 ms, faster than 5.00%
"""


class Solution:

    def __init__(self):
        self.candidates = []

    def countSteppingNumbers(self, low: int, high: int) -> List[int]:

        start = len(str(low))
        end = len(str(high))

        num_of_digits = start
        while num_of_digits <= end:
            for i in range(1, 10):
                self.dfs(str(i), num_of_digits)
            num_of_digits += 1

        self.candidates = sorted([int(x) for x in self.candidates])

        res = []
        for n in self.candidates:
            if low <= n <= high:
                res.append(n)
        return res

    def dfs(self, n, num_of_digits):
        if len(n) == num_of_digits:
            self.candidates.append(n)
            return
        x = int(n[-1])
        if x >= 1:
            self.dfs(n + str(x-1), num_of_digits)
        if x <= 8:
            self.dfs(n + str((x+1) % 10), num_of_digits)


s = Solution()

a = 1
b = 1000
print(s.countSteppingNumbers(a, b))

a = 1
b = 2000000000
print(s.countSteppingNumbers(a, b))

print("-----")

"""
    2nd: recursion + binary search

    Time    O(2^D) ? each digit has 2 options -1 or +1
    Space   O(2^D)
    468 ms, faster than 14.52%
"""


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:

        self.candidates = []

        if low == 0:
            self.candidates.append(0)

        start = len(str(low))
        end = len(str(high))

        num_of_digits = start
        while num_of_digits <= end:
            for i in range(1, 10):
                self.dfs(str(i), num_of_digits)
            num_of_digits += 1

        self.candidates = sorted([int(x) for x in self.candidates])

        left = bisect_left(self.candidates, low)
        right = bisect_right(self.candidates, high)
        return self.candidates[left:right]

    def dfs(self, n, num_of_digits):
        if len(n) == num_of_digits:
            self.candidates.append(n)
            return
        x = int(n[-1])
        if x >= 1:
            self.dfs(n + str(x-1), num_of_digits)
        if x <= 8:
            self.dfs(n + str((x+1) % 10), num_of_digits)


s = Solution()

a = 1
b = 1000
print(s.countSteppingNumbers(a, b))

a = 1
b = 2000000000
print(s.countSteppingNumbers(a, b))

print("-----")

"""
    3rd: BFS

    Time    O(2^D)
    Space   O(2^D)
    372 ms, faster than 32.26%
"""


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        if low == 0:
            res.append(0)
        while len(q) > 0:
            num = q.pop(0)
            if num < high:
                last = num % 10
                if last >= 1:
                    q.append(num * 10 + last - 1)
                if last <= 8:
                    q.append(num * 10 + last + 1)
            if low <= num <= high:
                res.append(num)
        return res
