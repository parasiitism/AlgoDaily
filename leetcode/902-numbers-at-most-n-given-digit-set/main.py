"""
    1st: math
    - i hate math so i learned from others

    ref:
    - https://leetcode.com/problems/numbers-at-most-n-given-digit-set/discuss/168439/C%2B%2B-O(logN)-Clear-code-with-explanation

    Time    O(N) or O(logn)
    Space   O(d)
    16 ms, faster than 100.00%
"""


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = [int(x) for x in digits]
        n_str = str(n)
        N = len(n_str)
        res = 0

        # for those less than n
        for L in range(1, N):
            res += len(digits)**L

        # for those have the same length as n
        for i in range(N):
            cur = int(n_str[i])  # cur

            # case1:
            # all the leading digits less than c must be legit
            # e.g. n = 460, digits=[1..9], 1,2,3
            for d in digits:
                if d < cur:
                    res += len(digits) ** (N - i - 1)

            # case2:
            # if current in digits
            # e.g. n = 460, digits=[1..9], 4
            # we need to think about the next digit
            if cur not in digits:
                break
            # so at the end, if the items in digits can compose entired n, res += 1
            if i+1 == N:
                res += 1

        return res
