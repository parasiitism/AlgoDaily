"""
    1st approach: 2 passes
    - form an array of waves. [-1,0,1] which -1: decrease, 0:same, 1:increase when we iterate through the array
    - iterate the 'waves' array and count the longest turbulent subarray

    e.g.
            [9, 4, 2, 10, 7, 8, 8, 1, 9, 11]
    waves = [-1, -1, 1, -1, 1, 0,-1, 1, 1]

    the longest turbulent waves is = waves[1:5] = [-1,1,-1,1], so the result = 5

    Time    O(2n)
    Space   O(n)
    504 ms, faster than 14.57% 
"""


class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        waves = []
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                waves.append(0)
            elif A[i] > A[i-1]:
                waves.append(1)
            elif A[i] < A[i-1]:
                waves.append(-1)

        res = 0
        t = 0
        for i in range(len(waves)):
            if waves[i] == 0:
                t = 0
            elif t == 0:
                t = 1
            elif waves[i] != waves[i-1]:
                t += 1
            else:
                t = 1
            res = max(res, t)
        return res+1


"""
    2nd approach: one pass without using an extra array
    - basically there are 3 cases
        - if turbulent (A[i-2] < A[i-1] > A[i]) or (A[i-2] > A[i-1] < A[i])
        - if there are 2 diff numbers at the begining, e.g.[2,4,4,...]
        - else(prev wave oscillate in same direction)

    ref:
    - https://leetcode.com/problems/longest-turbulent-subarray/discuss/222146/PythonJavaC%2B%2B-O(n)-time-O(1)-space-Simple-and-Clean-solution

    Time    O(n)
    Space   O(1)
    456 ms, faster than 61.90%
"""


class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        t, res = 0, 0
        for i in range(len(A)):
            if i >= 2 and (A[i-2] > A[i-1] < A[i] or A[i-2] < A[i-1] > A[i]):
                # if turbulent (A[i-2] < A[i-1] > A[i]) or (A[i-2] > A[i-1] < A[i])
                t += 1
            elif i >= 1 and A[i-1] != A[i]:
                # if there are 2 diff numbers at the begining, e.g.[2,4,4,...]
                t = 2
            else:
                t = 1
            res = max(res, t)
        return res
