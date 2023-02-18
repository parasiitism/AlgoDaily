"""
    1st: recursion

    Time    O(5^d) d = number of digits of N
    Space   O(5^d)
"""
class Solution:
    def confusingNumberII(self, n: int) -> int:
        self.res = 0
        for c in '1689':
            self.dfs(n, c)
        return self.res

    def reverse(self, S):
        mapping = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6' 
        }
        T = ''
        for i in range(len(S)-1, -1, -1):
            T += mapping[S[i]]
        return T
        
    def dfs(self, n, s):
        x = int(s)
        if x > n:
            return
        t = self.reverse(s)
        if t != s:
            self.res += 1
        for d in '01689':
            self.dfs(n, s+d)
