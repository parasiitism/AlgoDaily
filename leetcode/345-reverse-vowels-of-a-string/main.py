"""
    questions to ask:
    - a, e, i, o, u ony? yes
    - capital letters? yes
"""


"""
    1st approach: 2 pointers

    Time  O(n)
    Space O(n)
    68 ms, faster than 53.33%
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        for c in s:
            arr.append(c)
        i = 0
        j = len(s) - 1
        hs = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        while i < j:
            if arr[i] in hs and arr[j] in hs:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            elif arr[i] in hs:
                j -= 1
            elif arr[j] in hs:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(arr)
