"""
    1st: stack + math
    - in fact, since the number of [ and ] are the same, 
        we must end up with a pattern ]]...]] followed by [[...[[
    - an observation is that, the result of pattern N is (N+1)//2

    pattern                 result
    "]["                    1
    "]][["                  1
    "]]]][[[["              2
    "]]]]][[[[["            2
    "]]]]]][[[[[["          3
    "]]]]]]][[[[[[["        3
    "]]]]]]]][[[[[[[["      4
    "]]]]]]]]][[[[[[[[["    4
    ..                      (N+1)//2

    Time    O(N)
    Spce    O(1)
    512 ms, faster than 11.11%
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        openCount = 0
        closeCount = 0
        for i in range(n):
            c = s[i]
            if c == '[':
                openCount += 1
            elif c == ']':
                if openCount > 0:
                    openCount -= 1
                else:
                    closeCount += 1
        return (openCount+1) // 2
