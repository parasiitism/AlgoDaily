"""
    1st hashtable
    - the code is messy but the idea is simple, there are actually 2 main cases:
        1. xbaaabbbbc -> x:1,b:1,a:3,b:4,c:1 -> xaaaabbbbb
            we can swap one character which is just nearby the longest single-charactered string
        2. aaaabaaaca -> a:4,b:1,a:3,c:1,a:1 -> aaaaaaaacb
            there is a character between 2 long single-charactered strings
        edge case: aaabaaa -> aaaaaab
            no more other characters we can swap, we can only swap the character within the current range

    Time    O(2n)
    Space   O(n)
    56 ms, faster than 80.43%
"""


class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        counts = 26 * [0]
        counts[ord(text[0]) - ord('a')] += 1
        tuples = []
        cur, count = text[0], 1
        for i in range(1, len(text)):
            c = text[i]
            # hashtable
            counts[ord(c) - ord('a')] += 1
            # the short representation
            if c == cur:
                count += 1
            else:
                tuples.append((cur, count))
                cur, count = c, 1
        tuples.append((cur, count))

        if len(tuples) == 1:
            return tuples[0][1]
        elif len(tuples) == 2:
            return max(tuples[0][1], tuples[1][1])
        # check 2 cases
        res = 1
        for i in range(len(tuples)):
            c, n = tuples[i][0], tuples[i][1]
            idx = ord(c) - ord('a')

            a = 0
            b = 0

            if counts[idx] - n > 0:
                a = n + 1

            if i+2 < len(tuples) and tuples[i+1][1] == 1 and tuples[i+2][0] == c:
                n_ = tuples[i+2][1]
                if counts[idx] - n - n_ > 0:
                    b = n + 1 + n_
                else:
                    b = n + n_
            res = max(res, a, b)
        return res


s = Solution()

a = "ababa"
print(s.maxRepOpt1(a))  # 3

a = "aaabaaa"
print(s.maxRepOpt1(a))  # 6

a = "aaabbaaa"
print(s.maxRepOpt1(a))  # 4

a = "aaaaa"
print(s.maxRepOpt1(a))  # 5

a = "abcdef"
print(s.maxRepOpt1(a))  # 1

print('-----')

a = "xaaabaaac"
print(s.maxRepOpt1(a))  # 6

a = "axaaabaaac"
print(s.maxRepOpt1(a))  # 7

a = "xaaabaaaca"
print(s.maxRepOpt1(a))  # 7

a = "babbaaabbbbbaa"
print(s.maxRepOpt1(a))  # 6


print("=====")

"""
    2nd: hashtable, same idea but prettier
    - the code is messy but the idea is simple, there are actually 2 main cases:
        1. xbaaabbbbc -> x:1,b:1,a:3,b:4,c:1 -> xaaaabbbbb
            we can swap one character which is just nearby the longest single-charactered string
        2. aaaabaaaca -> a:4,b:1,a:3,c:1,a:1 -> aaaaaaaacb
            there is a character between 2 long single-charactered strings
        edge case: aaabaaa -> aaaaaab
            no more other characters we can swap, we can only swap the character within the current range

    Time    O(2n)
    Space   O(n)
    52 ms, faster than 87.87%
"""


class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        counts = 26 * [0]
        counts[ord(text[0]) - ord('a')] += 1
        tuples = []
        cur, count = text[0], 1
        for i in range(1, len(text)):
            # hashtable
            counts[ord(text[i]) - ord('a')] += 1
            # the short representation
            if text[i] == cur:
                count += 1
            else:
                tuples.append((cur, count))
                cur, count = text[i], 1
        tuples.append((cur, count))
        # check 2 cases
        res = 0
        for i in range(len(tuples)):
            c, n = tuples[i][0], tuples[i][1]
            idx = ord(c) - ord('a')

            a = min(n+1, counts[idx])
            b = 0

            if i+2 < len(tuples) and tuples[i+1][1] == 1 and tuples[i+2][0] == c:
                n_ = tuples[i+2][1]
                b = n + n_ + (1 if counts[idx] - n - n_ > 0 else 0)
            res = max(res, a, b)
        return res


s = Solution()

a = "ababa"
print(s.maxRepOpt1(a))  # 3

a = "aaabaaa"
print(s.maxRepOpt1(a))  # 6

a = "aaabbaaa"
print(s.maxRepOpt1(a))  # 4

a = "aaaaa"
print(s.maxRepOpt1(a))  # 5

a = "abcdef"
print(s.maxRepOpt1(a))  # 1

print('-----')

a = "xaaabaaac"
print(s.maxRepOpt1(a))  # 6

a = "axaaabaaac"
print(s.maxRepOpt1(a))  # 7

a = "xaaabaaaca"
print(s.maxRepOpt1(a))  # 7

a = "babbaaabbbbbaa"
print(s.maxRepOpt1(a))  # 6
