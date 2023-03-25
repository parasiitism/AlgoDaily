"""
    Math

    e.g. n = 15, time = 5
    1 -> 2 -> 3 -> 4 -> 5 -> 4 -> 3 -> 2 -> 1 -> 2 -> 3 -> 4 -> 5 -> 4 -> 3 -> 2
      #    #    #    #    @    @    @    @    #    #    #    #    @    @    @
    
    Time    O(1)
    Space   O(1)
"""
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        d = time // (n-1) 
        r = time % (n-1)
        if d % 2 == 0:
            return 1 + r
        return n - r