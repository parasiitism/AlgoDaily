import heapq

"""
    naive approach: brute force dfs
    - generate all ugly numbers until 2**31-1

    Time    O(2*31-1)
    LTE
"""

"""
    1st approach: hashtable
    - from 2 to inf, check if each number can be divieded by the 'primes'
    - use an array of boolean to avoid redundant calculation

    Time    O(k * 2^31-1)
    TLE
"""


class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n < 1:
            return 0
        self.seen = {}
        arr = []
        cur = 1
        while len(arr) < n:
            b = self.divide(cur, primes)
            self.seen[cur] = b
            if b == True:
                arr.append(cur)
            cur += 1
        return arr[-1]

    def divide(self, num, primes):
        if num == 1:
            return True
        if num in self.seen:
            return self.seen[num]
        for p in primes:
            if num % p == 0:
                return self.divide(num//p, primes)
        return False


s = Solution()

a = 12
b = [2, 7, 13, 19]
print(s.nthSuperUglyNumber(a, b))

a = 65
b = [2, 3, 5, 11, 13, 19, 23, 29, 43, 47]
print(s.nthSuperUglyNumber(a, b))

a = 70
b = [2, 3, 13, 17, 19, 37, 41, 43, 47, 53]
print(s.nthSuperUglyNumber(a, b))

a = 100000
b = [7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127,
     131, 137, 139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]
# print(s.nthSuperUglyNumber(a, b))

"""
    2nd approach: hashtable
    - from 2 to inf, check if each number can be divieded by the 'primes'
    - use an array of boolean to avoid redundant calculation

    ugly number                  k sorted list
    1                            2     7    13   19     1 * [2,7,13,19]
    |                            |     |    |    |
    2                            4     14   26   38     2 * [2,7,13,19]
    |                            |     |    |    |
    4                            8     28   52   76     4 * [2,7,13,19]
    |                            |     |    |    |              
    7                            14    49   91   133    7 * [2,7,13,19]
    |                            |     |    |    |
    8                            16    56   ...   ...   8 * [2,7,13,19]
    |                            |     |    |     |
    ...

    ref:
    - https://leetcode.com/problems/super-ugly-number/discuss/277313/My-view-of-this-question-hope-it-can-help-you-understand!!!

    Time    O(kN)
    Space   O(N)
    1592 ms, faster than 12.65%
"""


class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        pq = []
        hs = set()
        while len(uglies) < n:
            for p in primes:
                temp = p*uglies[-1]
                if temp not in hs:
                    hs.add(temp)
                    heapq.heappush(pq, temp)
            pop = heapq.heappop(pq)
            uglies.append(pop)
        return uglies[-1]


s = Solution()

a = 12
b = [2, 7, 13, 19]
print(s.nthSuperUglyNumber(a, b))

a = 65
b = [2, 3, 5, 11, 13, 19, 23, 29, 43, 47]
print(s.nthSuperUglyNumber(a, b))

a = 70
b = [2, 3, 13, 17, 19, 37, 41, 43, 47, 53]
print(s.nthSuperUglyNumber(a, b))

a = 100000
b = [7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127,
     131, 137, 139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]
print(s.nthSuperUglyNumber(a, b))
