"""
    1st approach: hashtable

    Time    O(n)
    Space   O(n)
    208 ms, faster than 43.22%
"""


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A) // 2
        ht = {}
        for num in A:
            if num not in ht:
                ht[num] = 1
            else:
                ht[num] += 1
            if ht[num] == n:
                return num
        return -1


"""
    2nd approach: math
    - in an array, if there is number appear n/2 times, the neightbors must be at most 2 steps away from target

    e.g.1
    [2,2,2,2,1,1,1,1] the 2 are next to each others

    e.g.2
    [1,1,2,1,1,2,2,2] at idx2, we can find any, but at idx6, neightbors is the target

    e.g.3
    [1,1,2,1,2,1,2,2] at idx2 we can find any, but at idx4, neightbors is the target

    Time    O(n)
    Space   O(1)
    180 ms, faster than 74.93%
"""


class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(2, len(A)):
            if A[i] == A[i-1] or A[i] == A[i-2]:
                return A[i]
        return A[0]
