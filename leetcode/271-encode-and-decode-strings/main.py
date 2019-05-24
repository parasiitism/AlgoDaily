"""
    1st approach: num sum
    - count the number of characters of each string and put it to the front of each string
        e.g. ['Hello', 'World'] -> [5]Hello[5]World
    - when we see a [x], we regard the coming x characters as a string 

    Time    O(mn)
    Space   O(mn)
     332 ms, faster than 8.52%
"""


class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            res += "[" + str(len(s)) + "]" + s
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res = []
        cur = ""
        start = False
        num = 0
        i = 0
        for c in s:
            if c == '[' and num == 0:
                start = True
            elif c.isdigit() and start:
                num = num*10 + int(c)
            elif c == ']' and start:
                start = False
            else:
                cur += c
                i += 1
            if start == False and i == num:
                res.append(cur)
                # reset num and i
                cur = ""
                num = 0
                i = 0
        return res


e = Codec().encode(["Hello", "World"])
print(e)
d = Codec().decode(e)
print(d)


e = Codec().encode(["Hello", "World", ""])
print(e)
d = Codec().decode(e)
print(d)

e = Codec().encode(["_+{}:?(*&^", "", "", "World", "L}K::K"])
print(e)
d = Codec().decode(e)
print(d)
