"""
    string
    
    Time    O(N)
    Space   O(N)
    57 ms, faster than 45.45%
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        for i in range(len(words)):
            if words[i-1][-1] != words[i][0]:
                return False
        return True
