"""
    1st appraoch:
    - check adjacent cells

    similar to lc957

    Time    O(n)
    Space   O(1)
    160 ms, faster than 30.61%
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if self.isValid(flowerbed, i):
                    flowerbed[i] = 1
                    n -= 1
                if n == 0:
                    return True
        return False
    
    def isValid(self, flowerbed, i):
        if i == 0:
            if i + 1 < len(flowerbed):
                if flowerbed[i+1] == 0:
                    return True
            else:
                return True
        elif i+1 < len(flowerbed):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                return True
        else:
            if flowerbed[i-1] == 0:
                return True
        return False

"""
    2nd appraoch:
    - check adjacent cells

    similar to lc957, place zeros in the fron and the end

    Time    O(n)
    Space   O(1)
    144 ms, faster than 52.54%
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return True
        clone = [0] + flowerbed[:] + [0]
        for i in range(1, len(clone)-1):
            if clone[i] == 0 and clone[i-1] == 0 and clone[i+1] == 0:
                clone[i] = 1
                n -= 1
            if n == 0:
                return True
        return False