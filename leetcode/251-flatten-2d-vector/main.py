"""
    questions to ask:
    - will we have empty arrays? yes
    - all are numbers? yes
"""

"""
    naive approach: put all of the numbers into a single array

    Time  O(n) when construct
    Space O(n)
    104 ms, faster than 17.66%
"""


class Vector2D(object):

    def __init__(self, v):
        self.nums = []
        for arr in v:
            for num in arr:
                self.nums.append(num)

    def next(self):
        return self.nums.pop(0)

    def hasNext(self):
        return len(self.nums) > 0


"""
    1st approach: 2pointers
    - row starts from 0
    - col starts from -1

    Time  O(n)
    Space O(n)
    80 ms, faster than 34.20%
"""


class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.v = v
        self.row = 0
        # very important
        self.col = -1

    def next(self):
        """
        :rtype: int
        """
        nextRow = self.row + 1
        nextCol = self.col + 1
        if self.row < len(self.v):
            if nextCol < len(self.v[self.row]):
                self.col = nextCol
                return self.v[self.row][nextCol]
            else:
                while nextRow < len(self.v):
                    if len(self.v[nextRow]) > 0:
                        self.row = nextRow
                        self.col = 0
                        return self.v[nextRow][0]
                    nextRow += 1
                return -1
        return -1

    def hasNext(self):
        """
        :rtype: bool
        """
        nextRow = self.row + 1
        nextCol = self.col + 1
        if self.row < len(self.v):
            if nextCol < len(self.v[self.row]):
                return True
            else:
                while nextRow < len(self.v):
                    if len(self.v[nextRow]) > 0:
                        return True
                    nextRow += 1
                return False
        return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
