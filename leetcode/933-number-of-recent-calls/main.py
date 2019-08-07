"""
    1st approach: queue
    - similar to lc362
    - remove the items (if x < t-3000) from the queue every time we enqueue new item

    Time of ping()      O(n)
    Space               O(n)
    316 ms, faster than 27.34%
"""


class RecentCounter(object):

    def __init__(self):
        self.arr = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.arr.append(t)
        while len(self.arr) > 0 and self.arr[0] < t-3000:
            self.arr.pop(0)
        return len(self.arr)
