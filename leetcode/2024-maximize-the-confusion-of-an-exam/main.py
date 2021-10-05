"""
    1st: 2 pointers
    - maintain a running window containing at most K truths. Shorten the window if there are more then K truths.
    - same concept for falses

    Time    O(2N)
    Space   O(1)
    472 ms, faster than 66.67%
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        res = 0

        j = 0
        change2true = 0
        for i in range(n):
            c = answerKey[i]
            if c == 'F':
                change2true += 1
            while change2true > k:
                if answerKey[j] == 'F':
                    change2true -= 1
                j += 1
            res = max(res, i-j+1)

        j = 0
        change2false = 0
        for i in range(n):
            c = answerKey[i]
            if c == 'T':
                change2false += 1
            while change2false > k:
                if answerKey[j] == 'T':
                    change2false -= 1
                j += 1
            res = max(res, i-j+1)

        return res
