"""
    1st approach:
	- start traversing the input array from the below index and i-=1, j+=1

    e.g.
    [1,2,3]
    [4,5,6]
    [7,8,9]
    
    start from:
    row idx 0, [1] 			
    row idx 1, [4,2] 		   then reverse
    row idx 2, [7,5,3] 	    
    col idx 1, [8,6] 		   then reverse
    col idx 2, [9] 			

	- put the items to the result array
	- for odd rows, put reversely
    
	Time		O(m*n)
	Space		O(m*n) the 2D array
	184 ms, faster than 33.62%
"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        res = []
        count = 0
        for i in range(len(matrix)):
            _i = i
            j = 0
            temp = []
            while _i >= 0 and j < len(matrix[0]):
                cell = matrix[_i][j]
                if count % 2 == 0:
                    temp.append(cell)
                else:
                    temp.insert(0, cell)
                _i -= 1
                j += 1
            res += temp
            count += 1
        for j in range(1, len(matrix[0])):
            i = len(matrix)-1
            _j = j
            temp = []
            while i >= 0 and _j < len(matrix[0]):
                cell = matrix[i][_j]
                if count % 2 == 0:
                    temp.append(cell)
                else:
                    temp.insert(0, cell)
                i -= 1
                _j += 1
            res += temp
            count += 1
        return res
