import math

"""
    1st approach: recursion
    - for every number from 2 to n-1, if it can divide the current number, it is one of the factors
    
    e.g. 252

    252%2 = 0
    252%3 = 0
    252%4 != 0
    ....

    Time    I am not sure
    Space   I am not sure
    LTE
"""


class Solution(object):

    def __init__(self):
        self.res = []

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.dfs(n, 2, [])
        return self.res

    def dfs(self, num, start, path):
        if num == 1:
            if len(path) > 1:
                self.res.append(path)
            return
        for i in range(start, num+1):
            if num % i == 0:
                self.dfs(num/i, i, path+[i])


print(Solution().getFactors(252))

"""
    2nd approach: recursion
    - for every number from 2 to n-1, if it can divide the current number, it is one of the factors
    - the diffrence from the 1st approach is THAT all prime factors must be less than/equal to a sqrt of a number 
    
    e.g. 252

    252%2 = 0
    252%3 = 0
    252%4 != 0
    ....

    Time    I am not sure
    Space   I am not sure
    16 ms, faster than 97.78%
"""


class Solution(object):

    def __init__(self):
        self.res = []

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.dfs(n, 2, [])
        return self.res

    def dfs(self, num, start, path):
        # the num never gets down to 1, because we use sqrt to factorize
        # e.g. 9 => 3 * 3 when it comes to 3, since sqrt(3) = 1, we cant factorize any more
        if len(path) > 0:
            self.res.append(path+[num])
        n = int(math.sqrt(num))
        for i in range(start, n+1):
            if num % i == 0:
                self.dfs(num/i, i, path+[i])


print(Solution().getFactors(252))
