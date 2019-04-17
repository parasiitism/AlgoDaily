"""
    1st approach: better brute forece
    - generate all the substrings, check if each substring has at least k characters for each character
    - i optimized it by holding a qualifiedKeyCnt during the inner loop 
        such that i can skip counting the unique character in another inner loop

    Time    O(n^2)
    Space   O(1)
    6256 ms, faster than 5.05%
"""


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        resStr = ""
        for i in range(len(s)):
            ht = {}
            qualifiedKeyCnt = 0
            for j in range(i, len(s)):
                c = s[j]
                # count the characters using a hashtable
                if c not in ht:
                    ht[c] = 1
                else:
                    ht[c] += 1

                # if ht[c] reaches to k, it means that that character has been qualified
                if ht[c] == k:
                    qualifiedKeyCnt += 1

                # if qualifiedKeyCnt == num of unique characters in hashtable,
                # over the result if needed
                if qualifiedKeyCnt == len(ht):
                    temp = s[i:j+1]
                    if len(temp) > res:
                        res = len(temp)
                        resStr = temp
        # return (res, resStr)
        return res


a = "aaabb"
b = 3
print(Solution().longestSubstring(a, b))

a = "ababbc"
b = 2
print(Solution().longestSubstring(a, b))

a = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrsssstttt"
b = 5
print(Solution().longestSubstring(a, b))
