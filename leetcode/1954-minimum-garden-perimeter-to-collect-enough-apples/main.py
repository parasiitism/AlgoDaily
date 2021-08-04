"""
    1st: binary search + math
    - the way to do the math is to split the area into 4 grid
    - for each grid, the area = r*(r+1)*(r+1)/2 + r*r*(r+1)/2, where the r = radius
    - see idea.png

    Time    O(log(2**32))
    Space   O(1)
    32 ms, faster than 75.00% 
"""


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left = 0
        right = 2**32
        while left < right:
            m = (left + right)//2
            appleCounts = 2 * (m*(m+1)*(m+1) + m*m*(m+1))
            if neededApples <= appleCounts:
                right = m
            else:
                left = m + 1
        return right * 8
