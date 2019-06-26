"""
    1st approach:
	- intuitive approach inspired by the desc
    
	Time		O(n!)
	Space		O(n!) the result
	16jan2019
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            arr = (i+1) * [1]
            for j in range(1, i):
                arr[j] = res[i-1][j-1] + res[i-1][j]
            res.append(arr)
        return res
