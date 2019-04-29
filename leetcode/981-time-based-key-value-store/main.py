"""
    1st approach: hashtable + binaray search

    Time    set:O(1), get:O(logn)
    Space   O(n)
    800 ms, faster than 20.19%
"""


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.m:
            self.m[key] = [[timestamp, value]]
        else:
            self.m[key].append([timestamp, value])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.m:
            return ""
        arr = self.m[key]
        idx = self.bsearch(arr, timestamp)
        if idx < 0:
            return ""
        return arr[idx][1]

    def bsearch(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid][0]:
                return mid
            elif target > nums[mid][0]:
                left = mid + 1
            else:
                right = mid - 1
        return right


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
