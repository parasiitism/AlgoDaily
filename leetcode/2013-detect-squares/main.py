from collections import *

"""
    1st: hashtable
    
    add:
    - put coordinates into a hashtable counter
    
    count:
    - see if (_x, y), (x, _y), (_x, _y) are in the counter
    - accumulate the squares we can count

    Time    O(N^2) worst for count()
    Space   O(N)
    1980 ms, faster than 7.14%
"""


class DetectSquares:

    def __init__(self):
        self.ht = Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.ht[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        for _x, _y in self.ht:
            if abs(x - _x) == abs(y - _y) and x - _x != 0:
                res += self.ht[(_x, _y)] * self.ht[(_x, y)] * self.ht[(x, _y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
