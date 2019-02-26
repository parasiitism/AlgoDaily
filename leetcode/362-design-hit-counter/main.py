from collections import *

"""
    1st approach:
    - dictionary + array(perserves the order) <= there is a handy class, OrderedDict, does the same thing
    - hit() => put the keys in the orderdict, increment the count for existing keys
    - getHits() => count the result by iterating through the OrderedDict from back until the key <= timestamp - 300

    Time: hit()       O(1)
    Time: getHits()   O(1) cos it just counts 300 keys at maximum
    Space   O(n)
    16 ms, faster than 100.00%
"""


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.od = OrderedDict()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        if timestamp in self.od:
            self.od[timestamp] += 1
        else:
            self.od[timestamp] = 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0
        items = self.od.items()
        n = len(items)
        for i in range(n-1, -1, -1):
            key, cnt = items[i]
            if key > timestamp - 300:
                res += cnt
            else:
                del od[key]
        return res


# sample usage of the OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
od['e'] = 5

print(od.items()[0])
del od['a']

if 'e' in od:
    print('y')
else:
    print('n')

for k in od:
    print(k, od[k])

# test
