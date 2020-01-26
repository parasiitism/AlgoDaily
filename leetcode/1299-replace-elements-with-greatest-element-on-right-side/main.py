"""
    1st:
    1. iterate the array from the back
    2. put the running max value into the result array
    3. update the running max value if the current item is larger

    Time    O(N)
    Space   O(1)
    84 ms, faster than 55.42%
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        maxVal = -1
        for i in range(len(arr)-1, -1, -1):
            res.append(maxVal)
            maxVal = max(maxVal, arr[i])
        return res[::-1]
