"""
    1st approach: math
    - create a 2d array
    - use 2 variables, row and col to indicate the cell for placing the characters
    - when col % (numRows-1), we put the next 'numRows' characters vertically downward
    - when row goes out of bound, we are going to place the next character diagonally toward upper-right

    Time    O(mn)
    Space   O(nm)
    1416 ms, faster than 5.04%
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        m = []
        for i in range(numRows):
            m.append(len(s) * [' '])
        row, col = 0, 0
        for i in range(len(s)):
            c = s[i]
            m[row][col] = c
            if col % (numRows-1) == 0:
                row += 1
                if row == numRows:
                    row -= 2
                    col += 1
            else:
                row -= 1
                col += 1
        res = ''
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] != ' ':
                    res += m[i][j]
        return res


s = Solution()

print(s.convert('PAYPALISHIRING', 3))
print(s.convert('PAYPALISHIRING', 4))
print(s.convert('A', 1))
