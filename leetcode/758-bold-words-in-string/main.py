class Solution(object):
    def boldWords(self, words, S):
        """
        32 ms, faster than 94.95%
        """
        # find the positions for the bold tags
        intervals = []
        for word in set(words):
            t = S.find(word)
            while t > -1:
                intervals.append([t, t+len(word)])
                t = S.find(word, t+1)
        # sort the intervals, O(nlogn)
        intervals = sorted(intervals, key=lambda x: x[0])
        if len(intervals) == 0:
            return S
        # merge the intervals
        merged = [intervals[0]]
        for interval in intervals:
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        # put the intervals into sets
        opens = set()
        closes = set()
        for m in merged:
            opens.add(m[0])
            closes.add(m[1])
        # construct result
        res = ""
        stack = 0
        for i in range(len(S)):
            if i in opens:
                res += "<b>"
                stack += 1
            if i in closes:
                res += "</b>"
                stack -= 1
            res += S[i]
        if stack > 0:
            res += "</b>"
        return res


a = ["ab", "bc"]
b = "aabcd"
# a<b>abc</b>d
print(Solution().boldWords(a, b))

a = ["ab", "cd"]
b = "aabcd"
# a<b>abcd</b>
print(Solution().boldWords(a, b))

a = ["ccb", "b", "d", "cba", "dc"]
b = "eeaadadadc"
# "eeaa<b>d</b>a<b>d</b>a<b>dc</b>"
print(Solution().boldWords(a, b))

a = ["ae", "a", "a", "a", "e"]
b = "cdccccbaab"
# "cdccccb<b>aa</b>b"
print(Solution().boldWords(a, b))

a = ["e", "ad", "ce", "a", "b"]
b = "adcaddeced"
# "<b>ad</b>c<b>ad</b>d<b>ece</b>d"
print(Solution().boldWords(a, b))

a = ["ccb", "a", "cc", "dc", "d"]
b = "bacdcbcced"
# "b<b>a</b>c<b>dc</b>b<b>cc</b>e<b>d</b>"
print(Solution().boldWords(a, b))

# I think Leetcode is incorrect
a = ["e", "cab", "de", "cc", "db"]
b = "cbccceeead"
# "cb<b>ccceee</b>ad"
print(Solution().boldWords(a, b))
