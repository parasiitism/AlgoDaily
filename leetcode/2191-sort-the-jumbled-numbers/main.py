"""
    1st: hashtable + sort

    Time    O(NlogN)
    Space   O(N)
    3046 ms, faster than 33.33%
"""


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            x = nums[i]
            s = ''
            for c in str(x):
                s += str(mapping[int(c)])
            y = int(s)
            arr.append((y, i, x))
        keys = []
        arr.sort(key=lambda x: (x[0], x[1]))
        for y, i, x in arr:
            keys.append(x)
        return keys
