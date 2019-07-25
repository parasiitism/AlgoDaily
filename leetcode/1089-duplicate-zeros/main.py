"""
    1st approach: dummy arr
    - create a dummy arr
    - when we see a zero, put an extra zero into the dummy arr
    - put the numbers from dummy arr to the input arr 

    Time    O(2n)
    Space   O(n)
    52 ms, faster than 88.91%
"""


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        res = []
        for x in arr:
            res.append(x)
            if x == 0:
                res.append(0)
        for i in range(len(arr)):
            arr[i] = res[i]
