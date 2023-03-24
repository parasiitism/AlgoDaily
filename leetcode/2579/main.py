"""
    math
    
    To calculate the number of squares from the middle to top: (1+2n-1)n/2 = n^2
    
    e.g. 5
                *           1
              * * *         3
            * * * * *       5
          * * * * * * *     7
        * * * * * * * * *   9
          * * * * * * *     7
            * * * * *       5
              * * *         3
                *           1

"""
class Solution:
    def coloredCells(self, n: int) -> int:
        return self.f(n) + self.f(n-1)
    
    def f(self, n):
        return n**2