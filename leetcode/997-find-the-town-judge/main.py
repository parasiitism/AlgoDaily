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
    2nd approach: array
    - for each person, establish a table of followings
    - for each person, establish a table of followers
    - if there is a person that he has N-1 followers and he trusts no one, he is the result

    Time    O(T+2n)
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
        trustIn = (N+1)*[0]
        trustBy = (N+1)*[0]
        
        for x, y in trust:
            trustIn[x] += 1
            trustBy[y] += 1

        for i in range(1, N+1):
            if trustBy[i] == N-1:
                if trustIn[i] == 0:
                    return i
                else:
                    return -1
        return -1