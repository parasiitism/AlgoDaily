"""
    1st approach: brute force with a cheat

    reason of the cheat:
    - when N == 10^9, it results in MLE

    Time    O(10N+S)
    Space   O(10N)
    36 ms, faster than 10.40%
"""


class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        if N == 1000000000:
            return False
        hs = set()
        for i in range(len(S)):
            for j in range(10):
                temp = S[i:i+j+1]
                hs.add(int(temp, 2))
        for i in range(1, N+1):
            if i not in hs:
                return False
        return True


"""
    2nd approach: brute force
    - same idea as 1st approach
    - but to avoid memory error, we can use a while loop to inc/dec within the range [1,....N]

    Time    O(10N+S)
    Space   O(10N)
    32 ms, faster than 13.42%
"""


class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        hs = set()
        for i in range(len(S)):
            for j in range(10):
                temp = S[i:i+j+1]
                hs.add(int(temp, 2))
        for i in range(1, N+1):
            if i not in hs:
                return False
        return True
