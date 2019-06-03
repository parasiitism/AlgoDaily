"""
    1st approach: string slicing
    - for every substring(starting from the front), see if we can slice the str1 and str2 until they become empty strings
    
    e.g.
    str1 = ABCABC
    str2 = ABC

    slicing A from the front fails becos strings are not empty after slicing
    str1 = BCABC
    str2 = BC

    slicing AB from the front fails becos strings are not empty after slicing
    str1 = CABC
    str2 = C

    slicing ABC from the front succeeds becos strings are empty after slicing
    str1 = ''
    str2 = ''
    YEAH

    Time    O(ABB)
    Space   O(min(A, B))
    80 ms, faster than 5.08%
"""


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        gcm = ""
        for i in range(len(str2)):
            sub = str2[:i+1]
            A = str1
            B = str2
            while len(A) > 0 and len(B) > 0:
                if A[:i+1] == sub and B[:i+1] == sub:
                    A = A[i+1:]
                    B = B[i+1:]
                else:
                    break
            while len(A) > 0 and A[:i+1] == sub:
                A = A[i+1:]
            while len(B) > 0 and B[:i+1] == sub:
                B = B[i+1:]
            if len(A) == 0 and len(B) == 0:
                gcm = sub
        return gcm


print(Solution().gcd("ABCABC", "ABC"))
print(Solution().gcd("ABABAB", "ABAB"))
print(Solution().gcd("ABABAB", "ABABAB"))
print(Solution().gcd("ABCABC", "AB"))
print(Solution().gcd("leetcode", "code"))

print("-----")

"""
    2nd approach: string slicing with GCD of integers concept
    
    - this is the concept of GCD between integers
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    lets say a = 20, b = 8
    step1. 20%8 = 4
    step2. 8%4 = 0 
    therefore 4 is the CGD of 20 and 8

    - same thing happens when integers -> strings

    Time    O(AB)
    Space   O(min(A, B)) depth of recursion tree
    8 ms, faster than 99.58%
"""


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        return self.gcd(str1, str2)

    def gcd(self, a, b):
        if len(b) == 0:
            return a
        # if the first character of a and b are diff, cant slice further
        if a[0] != b[0]:
            return ""
        n = len(b)
        # imitate using divion of integers to get remainder
        reminder = a
        while len(reminder) > 0 and reminder[:n] == b:
            reminder = reminder[n:]
        return self.gcd(b, reminder)


print(Solution().gcd("ABCABC", "ABC"))
print(Solution().gcd("ABABAB", "ABAB"))
print(Solution().gcd("ABABAB", "ABABAB"))
print(Solution().gcd("ABCABC", "AB"))
print(Solution().gcd("leetcode", "code"))
