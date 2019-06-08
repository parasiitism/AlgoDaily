class Solution(object):
    def canFormPalindrome(self, A, B):
        """
        Given 2 strings a and b with the same length. Strings are alligned one under the other. 
        We can choose an index and split both strings into 4 subtrings: 
        a1 + a2 and b1 + b2. Find out if it's possible to split a and b such that a1 + b2 or a2 + b1 forms a palindrome.

        Input: A = "abcbbbb", B = "xxxbcba"
        Output: true

        Explanation:
        abc|bbbb
        xxx|bcba

        We can split the strings at index 3. We will get a1 = "abc", a2 = "bbbb" and b1 = "xxx", b2 = "bcba"
        a1 + b2 forms a palidnrome "abcbcba" so return true.
        """
        for i in range(len(A)):
            a1 = A[:i+1]
            a2 = A[i+1:]
            b1 = B[:i+1]
            b2 = B[i+1:]
            temp1 = a1 + b2
            temp2 = b1 + a2
            if self.isPalindrome(temp1) or self.isPalindrome(temp2):
                return True
        return False

    def isPalindrome(self, s):
        return s == s[::-1]

    def longestPalindrome(self, A, B):
        """
        Find the longest palindrome if we can split and combine the strings at any position

        abcbbbb
        xxxbcba

        - aa is a palindrome
        - abba is a palindrome
        - abccba is a palindrome
        .
        .
        .
        - abcbbbbbcba is the longest palindrome

        """
        res = ""
        for i in range(len(A)):
            a1 = A[:i+1]
            a2 = A[i+1:]
            for j in range(len(B)):
                b1 = B[:j+1]
                b2 = B[j+1:]
                temp1 = a1 + b2
                temp2 = b1 + a2
                if self.isPalindrome(temp1) and len(temp1) > len(res):
                    res = temp1
                if self.isPalindrome(temp2) and len(temp2) > len(res):
                    res = temp2
        return res


a = "abcbbbb"
b = "xxxbcba"
print(Solution().canFormPalindrome(a, b))

a = "abcbbbb"
b = "xxxbcba"
print(Solution().longestPalindrome(a, b))
