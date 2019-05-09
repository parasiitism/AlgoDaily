"""
    1st approach: hashtable, hashset
    - create a trusted people set for each person
    - find the potential judge
    - check if the potential judge is trusted by everyone

    Time    O(T + n^2)
    Space   O(n)
    708 ms, faster than 23.56%
"""
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """

        # create a set for every person
        hs = {}
        for i in range(1, N+1):
            hs[i] = set()
        # for each person, add the people that he trusts
        for x, y in trust:
            hs[x].add(y)
        # find the potential judge
        judge = -1
        for i in range(1, N+1):
            if len(hs[i]) == 0:
                judge = i
                break
        if judge == -1:
            return -1
        # check if the potential judge is trusted by every one
        for key in hs:
            if key != judge:
                s = hs[key]
                if judge not in s:
                    return -1
        return judge

"""
    2nd approach: array, hashset
    - create a trusted people set for each person
    - find the potential judge
    - check if the potential judge is trusted by everyone

    Time    O(T + n^2)
    Space   O(n)
    708 ms, faster than 23.56%
"""
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        hs = [None]
        for i in range(1, N+1):
            hs.append(set())
        
        for x, y in trust:
            hs[x].add(y)
        
        judge = -1
        for i in range(1, N+1):
            if len(hs[i]) == 0:
                judge = i
                break
        if judge == -1:
            return -1
        
        for i in range(1, len(hs)):
            if i != judge:
                s = hs[i]
                if judge not in s:
                    return -1
        return judge