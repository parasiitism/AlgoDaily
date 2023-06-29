"""
    1st: recursion + math
    
    C: copy, P: paste
    - the worse case  is we need to CPPPPPPP...P to make a string with N * 'A'
    - in general, for example N=6, , there are 3 ways:
        - CPPPPP: paste single A 5 times
        - CPPCP: make 'AAA', paste
        - CPCPP: make 'AA', paste, paste

    Time    O(N * sqrt(N))
    Space   O(H)
"""


class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        res = n
        for i in range(2, n):
            # i = potential frequency of 'A...A' appears in N*'A'
            if n % i == 0:
                # recursively look for the minstep to come up with that substring
                # +i means CPPPP...P
                #          <-- i -->
                res = min(res, self.minSteps(n//i) + i)
        return res
