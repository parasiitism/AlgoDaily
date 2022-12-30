"""
    math
    - https://www.youtube.com/watch?v=Uun4z0EqMLc


    Time    O(N * k! / a!b!...) N = number of words
    Space   O(N)
"""


class Solution:
    def countAnagrams(self, s: str) -> int:
        words = s.split(" ")
        res = 1
        for w in words:
            res *= self.count_permutation(w)
            res %= 10**9 + 7
        return res

    def count_permutation(self, word):
        ctr = Counter(word)
        n_fac = self.factorial(len(word))
        for key in ctr:
            cnt = ctr[key]
            if cnt > 1:
                n_fac //= self.factorial(cnt)
        return n_fac

    def factorial(self, n):
        x = 1
        for i in range(2, n+1):
            x *= i
        return x
