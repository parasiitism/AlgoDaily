"""
    1st approach: math + 2pointers
    1. count the number of D and I
    2. if first character is I, result start with 0, else start with N
    3. find the point to put the second integer, and use 2 pointers to expand its range

    see ./idea.jpeg

    Time    O(2n)
    Space   O(1)
    64 ms, faster than 62.52%
"""


class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)
        iCount = 0
        dCount = 0
        for c in S:
            if c == 'I':
                iCount += 1
            else:
                dCount += 1
        left = 0
        right = 0
        res = []
        if S[0] == 'I':
            res.append(0)
            iCount -= 1
            left, right = N-iCount, N-iCount
        else:
            res.append(N)
            dCount -= 1
            left, right = N-iCount-1, N-iCount-1
        for x in S:
            if x == 'I':
                res.append(right)
                if left == right:
                    left -= 1
                right += 1
            else:
                res.append(left)
                if left == right:
                    right += 1
                left -= 1
        return res


print(Solution().diStringMatch("IDID"))
print(Solution().diStringMatch("III"))
print(Solution().diStringMatch("DDI"))
print(Solution().diStringMatch("IDIDDDIDI"))
print("-----")

"""
    2nd approach: greedysuggested solution
    - similar idea as 2pointers

    Time    O(n)
    Space   O(1)
    64 ms, faster than 62.52%
"""


class Solution(object):
    def diStringMatch(self, S):
        left, right = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
        ans.append(left)
        return ans


print(Solution().diStringMatch("IDID"))
print(Solution().diStringMatch("III"))
print(Solution().diStringMatch("DDI"))
print(Solution().diStringMatch("IDIDDDIDI"))
