"""
    1st: just sort

    Time    O(NlogN)
    Space   O(N)
    332 ms, faster than 72.27%
"""


class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        if veganFriendly == 1:
            arr = []
            for x in restaurants:
                if x[2] == 1:
                    arr.append(x)
            restaurants = arr

        arr = []
        for x in restaurants:
            if x[3] <= maxPrice and x[4] <= maxDistance:
                arr.append(x)

        def cmpter(a, b):
            if a[1] == b[1]:
                return b[0]-a[0]
            return b[1]-a[1]
        sortedArr = sorted(arr, cmp=cmpter)

        return [x[0] for x in sortedArr]
