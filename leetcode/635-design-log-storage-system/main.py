"""
    actually at the begining, i use binary search + python.datetime but its too hard to implement 
    becos the end is inclusive(need to calculate the next year, hour,....etc)
"""

"""
    1st approach: comparing timestamp strings
    - it works becos the timestamps we compare have the same length
    e.g.
    2016:01:02:03:12:00 is always less than 2016:01:02:03:13:00

    ref:
    - https://leetcode.com/problems/design-log-storage-system/discuss/105016/Python-Straightforward-with-Explanation

    Time    O(n) for retrieve()
    Space   O(n)
    68 ms, faster than 22.36%
"""


class LogSystem(object):

    def __init__(self):
        # 2d array [[timestamp1, id1], [timestamp2, idx2], ....]
        self.arr = []

    def put(self, logId, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: None
        """
        self.arr.append([timestamp, logId])

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        res = []
        t1 = self.getRange(s, gra)
        t2 = self.getRange(e, gra)
        for timestamp, logId in self.arr:
            t = self.getRange(timestamp, gra)
            if t1 <= t and t <= t2:
                res.append(logId)

        return res

    def getRange(self, t, gra):
        # cut 3, 6,... from the back
        # 2017:01:01:23:59:59
        n_time = len(t)
        m = {
            "Second": 0,
            "Minute": 1,
            "Hour": 2,
            "Day": 3,
            "Month": 4,
            "Year": 5,
        }
        i = m[gra]
        return t[:n_time-3*i]


obj = LogSystem()
obj.put(1, "2017:01:01:23:59:59")
obj.put(2, "2017:01:01:22:59:59")
obj.put(3, "2016:01:01:00:00:00")
print(obj.arr)
print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))
print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"))
