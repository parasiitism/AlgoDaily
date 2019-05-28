"""
    1st approach: hashtable count
    - get the signature of the S
    - for each word in words, get its signature and compare with the signature of the S
    
    e.g.
    S = "heeellooo"
    words = ["hello", "hi", "helo"]

    signature of S:
    S =         [('h', 1), ('e', 3), ('l', 2), ('o', 3)]
    
    signature of words:
    hello =     [('h', 1), ('e', 1), ('l', 2), ('o', 1)] <- multiply the 'e' to 'eee', 'o' to 'ooo'
    hi =        [('h', 1), ('i', 1)]
    helo =      [('h', 1), ('e', 1), ('l', 1), ('o', 1)] <- CANNOT multiply because count of 'l' in S is less than 3
    heeellooo = [('h', 1), ('e', 3), ('l', 2), ('o', 3)] <- the same

    so the total count = 2

    Time    O(nk)
    Space   O(nk)
    36 ms, faster than 88.11% 
"""


class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        a = self.getSignature(S)
        count = 0
        for word in words:
            b = self.getSignature(word)
            if len(a) != len(b):
                continue
            matchCount = 0
            for i in range(len(a)):
                c1, count1 = a[i]
                c2, count2 = b[i]
                if c1 != c2:
                    break
                else:
                    if count1 == count2 or (count1 >= 3 and count1 > count2):
                        matchCount += 1
            if matchCount == len(a):
                count += 1

        return count

    def getSignature(self, S):
        prev = S[0]
        count = 1
        structure = []
        for i in range(1, len(S)):
            c = S[i]
            if c == prev:
                count += 1
            else:
                structure.append((prev, count))
                prev = c
                count = 1
        if count > 0:
            structure.append((prev, count))
        return structure


"""
    1st approach: hashtable count
    - same as above but use instances(of a class) instead of tuples

    Time    O(nk)
    Space   O(nk)
    52 ms, faster than 42.89%
"""


class Signature(object):
    def __init__(self, c, count):
        self.c = c
        self.count = count


class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        a = self.getSignature(S)
        count = 0
        for word in words:
            b = self.getSignature(word)
            if len(a) != len(b):
                continue
            matchCount = 0
            for i in range(len(a)):
                sign1 = a[i]
                sign2 = b[i]
                c1, count1 = sign1.c, sign1.count
                c2, count2 = sign2.c, sign2.count
                if c1 != c2:
                    break
                else:
                    if count1 == count2 or (count1 >= 3 and count1 > count2):
                        matchCount += 1
            if matchCount == len(a):
                count += 1

        return count

    def getSignature(self, S):
        prev = S[0]
        count = 1
        structure = []
        for i in range(1, len(S)):
            c = S[i]
            if c == prev:
                count += 1
            else:
                structure.append(Signature(prev, count))
                prev = c
                count = 1
        if count > 0:
            structure.append(Signature(prev, count))
        return structure
