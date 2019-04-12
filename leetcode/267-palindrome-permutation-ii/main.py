"""
    1st approach:
    1. check if we can form palidrome
    2. generate permuation by inserting the characters in the middle

    Time    O(N+N!+N) => O(N!)
    Space   O(N!)
    36 ms, faster than 20.46%
"""


class Solution(object):

    def __init__(self):
        self.res = []

    def generatePalindromes(self, s):
        # check if we can form a palindrom
        ht = {}
        for c in s:
            if c not in ht:
                ht[c] = 1
            else:
                ht[c] += 1
        hasOdd = False
        for k in ht:
            if ht[k] % 2 > 0:
                if hasOdd == True:
                    return []
                hasOdd = True
        # transform hashtable into candidates for permutation
        remain = []
        oddChar = ""
        for k in ht:
            if ht[k] % 2 == 0:
                remain.append((k, ht[k]))
            else:
                if ht[k]-1 > 0:
                    remain.append((k, ht[k]-1))
                oddChar = k

        # generate permuation
        self.dfs(0, "", remain)

        # for odd number, we should add the lonely character in the middle
        if len(oddChar) > 0:
            newRes = []
            for x in self.res:
                mid = len(x)/2
                newRes.append(x[:mid] + oddChar + x[mid:])
            return newRes

        return self.res

    def dfs(self, idx, prefix, remain):
        if len(remain) == 0:
            self.res.append(prefix)
        else:
            for i in range(len(remain)):
                c, count = remain[i]
                # generate permutation
                # e.g. aa, {b:2} -> add 2 characters in the middle -> a|bb|a
                s = prefix[:idx] + c + c + prefix[idx:]
                count -= 2

                if count >= 2:
                    # copy the candidates, mutate the count and generate permuation in the next recursion
                    newRemain = remain[:]
                    newRemain[i] = (remain[i][0], count)
                    self.dfs(idx+1, s, newRemain)
                elif count == 0:
                    self.dfs(idx+1, s, remain[:i]+remain[i+1:])


a = "aabb"
print(Solution().generatePalindromes(a))

a = "abc"
print(Solution().generatePalindromes(a))

a = "aabbcc"
print(Solution().generatePalindromes(a))

a = "aaabb"
print(Solution().generatePalindromes(a))

a = "aaaabb"
print(Solution().generatePalindromes(a))

a = "aaaabbc"
print(Solution().generatePalindromes(a))

a = "aaaaaabbbbc"
print(Solution().generatePalindromes(a))
