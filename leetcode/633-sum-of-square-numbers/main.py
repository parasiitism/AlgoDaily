"""
    questions to ask:
    - do we count 0 as a valid a or b? yes
    - negative numbers? yes but just return me the positive number cos neg**2 == pos**2
"""

"""
    1st approach: brute force
    - iterate twice to see if i*i + j*j == c

    Time    O(sqrt(n) * sqrt(n))
    Space   O(1)
    LTE
"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        root = int(math.sqrt(c))
        for i in range(root+1):
            for j in range(i, root+1):
                if i*i + j*j == c:
                    return True
        return False


"""
    2nd approach: better brute force
    - optimze the 1st approach by checking if c - i*i is an integer

    Time    O(sqrt(n))
    Space   O(1)
    120 ms, faster than 78.10%
"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        root = int(math.sqrt(c))
        for i in range(root+1):
            temp = math.sqrt(c - i*i)
            if temp.is_integer():
                return True
        return False
