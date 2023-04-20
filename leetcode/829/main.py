"""
    Math
    - iterate from 2 to sqrt(2N), for every candidate, the middle is roughly at N/i, 
    then we just need to sum all the numbers between mid-radius and mid+radius
    - don't forget that the sum calculation is slightly different for odds and evens

    e.g.
        5 / 1 = 5
        5 / 2 = 2 + 3
                ^ middle

        9 / 1 = 9
        9 / 2 = 4 + 5
                ^ middle
        9 / 3 = 2 + 3 + 4
                    ^ middle

        15 / 1 = 15
        15 / 2 = 7 + 8
                 ^ middle
        15 / 3 = 4 + 5 + 6
                     ^ middle
        15 / 5 = 1 + 2 + 3 + 4 + 5
                         ^ middle

        30 / 1 = 30
        30 / 3 = 9 + 10 + 11
                     ^ middle
        30 / 4 = 6 + 7 + 8 + 9
                     ^ middle
        30 / 5 = 4 + 5 + 6 + 7 + 8
                         ^ middle

    Time    O(sqrt(2N))
    Space   O(1)
"""


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 1
        root = int(math.sqrt(2 * N))
        for w in range(2, root+1):
            mid = N // w
            if w % 2 == 0:
                r = w // 2
                temp = self.get_sum_between(mid-r+1, mid+r)
                if temp == N:
                    res += 1
            else:
                r = w // 2
                temp = self.get_sum_between(mid-r, mid+r)
                if temp == N:
                    res += 1
        return res

    def get_sum_between(self, L, R):
        return (R+L)*(R-L+1)//2
