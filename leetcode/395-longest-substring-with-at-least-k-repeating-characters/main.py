"""
    1st approach: better brute forece
    - generate all the substrings, check if each substring has at least k characters for each character
    - i optimized it by holding a qualifiedKeyCnt during the inner loop 
        such that i can skip counting the unique character in another inner loop

    Time    O(n^2)
    Space   O(1)
    6060 ms, faster than 5.12%
"""


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
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
                    if len(temp) > len(resStr):
                        resStr = temp
        return len(resStr)


a = "aaabb"
b = 3
print(Solution().longestSubstring(a, b))

a = "ababbc"
b = 2
print(Solution().longestSubstring(a, b))

a = "cababb"
b = 2
print(Solution().longestSubstring(a, b))

a = "cababbc"
b = 2
print(Solution().longestSubstring(a, b))

a = "ababcabbabacdddfgh"
b = 3
print(Solution().longestSubstring(a, b))

a = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrsssstttt"
b = 5
print(Solution().longestSubstring(a, b))

print("--------------------")


"""
    2nd approach: divide and conquer, learned from others
    - split the string by using characters which appear less than k times
    - if all characters in the substring appear >=k times, override the result in needed
    - if a character appears < k times, do 1) and 2)

    e.g. "ababcabbabacdddfgh", k=3

    - for the input, since c appears twice only, we split c
    ['abab', 'abbaba', 'dddfgh']

    - for abab, since a and b both appear less than k times, we split a and then b
    ['', 'b', 'b']
    ['', '']

    return 0

    - for abbaba, all numbers appear 3 times, return 6

    - for dddfgh, f appears 1 time, we split and get
    ['ddd', 'gh'] <- we recursively split gh and get 0 from the recursion

    - but since d appears 3 times 'ddd' is one of the result

    - but len('ddd') < len('abbaba'), so result is still 'abbaba'


    ref:
    - https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87768/4-lines-Python

    Time    O(nlogn)
    Space   O(h)
    28 ms, faster than 55.92%
"""


class Solution(object):

    def longestSubstring(self, s, k):
        # count the characters
        ht = {}
        for c in s:
            if c not in ht:
                ht[c] = 1
            else:
                ht[c] += 1
        # for each character: if count < k, we dump the character and explore the occurences in the remaining strings
        for c in ht:
            if ht[c] < k:
                maxCnt = 0
                splits = s.split(c)
                for t in splits:
                    temp = self.longestSubstring(t, k)
                    maxCnt = max(maxCnt, temp)
                return maxCnt
        # if empty string or all characters appear >= k
        # return its length to parent for comparison
        return len(s)


a = "aaabb"
b = 3
print(Solution().longestSubstring(a, b))

a = "ababbc"
b = 2
print(Solution().longestSubstring(a, b))

a = "cababb"
b = 2
print(Solution().longestSubstring(a, b))

a = "cababbc"
b = 2
print(Solution().longestSubstring(a, b))

a = "ababcabbabacdddfgh"
b = 3
print(Solution().longestSubstring(a, b))

a = "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrsssstttt"
b = 5
print(Solution().longestSubstring(a, b))
