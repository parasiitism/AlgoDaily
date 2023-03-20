"""
    1st: brute-force prefix sum

    Time    O(NlogN) <- mod takes logN time for big numbers
    Space   O(N)
    LTE     37 / 49 testcases passed
"""
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        num = 0
        res = n * [0]
        for i in range(n):
            x = int(word[i])
            num = 10 * num + x
            if num % m == 0:
                res[i] = 1
        return res

"""
    2nd: prefix sum + mod
    - the problem of the 1st approach was the big numbers, so we should just store the remain instead of storing the whole number during iteration

    Time    O(NlogM) <- for big numbers, logM is significant
    Space   O(N)
    LTE     37 / 49 testcases passed
"""
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        pfs = 0
        res = n * [0]
        for i in range(n):
            pfs = 10 * pfs + int(word[i])
            pfs %= m
            if pfs == 0:
                res[i] = 1
        return res